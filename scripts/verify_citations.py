#!/usr/bin/env python3
# (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite.
"""Verify every entry of a .bib file against live bibliographic indexes.

Backends: Crossref (primary), OpenAlex (fallback). Both work without an API
key. For each entry the script reports VERIFIED / MISMATCH / ARXIV_ONLY /
NOT_FOUND with the index's (venue, year, DOI). Nothing is ever guessed: an
entry no index can locate is reported as NOT_FOUND, full stop (L1).

Usage:
    verify_citations.py <references.bib> [--mailto you@example.org] [--limit N]
"""

import json
import re
import sys
import time
import urllib.parse
import urllib.request
from difflib import SequenceMatcher

TIMEOUT = 20
SLEEP_BETWEEN = 1.0
MATCH_THRESHOLD = 0.85
USER_AGENT = "ieee-paper-suite-citation-check/1.0"


def parse_args(argv):
    if len(argv) < 2:
        print("ERROR: usage: verify_citations.py <references.bib> "
              "[--mailto addr] [--limit N]", file=sys.stderr)
        sys.exit(2)
    path, mailto, limit = argv[1], None, None
    args = argv[2:]
    while args:
        flag = args.pop(0)
        if flag == "--mailto" and args:
            mailto = args.pop(0)
        elif flag == "--limit" and args:
            limit = int(args.pop(0))
        else:
            print(f"ERROR: unknown argument {flag}", file=sys.stderr)
            sys.exit(2)
    return path, mailto, limit


def parse_bib(text):
    """Return a list of entry dicts. Regex-based, tolerant of nested braces
    one level deep; a malformed entry is reported, never silently dropped."""
    entries = []
    for match in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", text):
        etype, key = match.group(1).lower(), match.group(2)
        if etype in ("comment", "string", "preamble"):
            continue
        start = match.end()
        depth, pos = 1, match.start() + text[match.start():].index("{") + 1
        pos = start
        while pos < len(text) and depth > 0:
            if text[pos] == "{":
                depth += 1
            elif text[pos] == "}":
                depth -= 1
            pos += 1
        body = text[start:pos - 1]
        fields = {}
        for fm in re.finditer(
                r"(\w+)\s*=\s*(\{(?:[^{}]|\{[^{}]*\})*\}|\"[^\"]*\"|\w+)",
                body):
            raw = fm.group(2).strip("{}\"")
            fields[fm.group(1).lower()] = re.sub(r"\s+", " ", raw).strip()
        entries.append({"key": key, "type": etype, "fields": fields})
    return entries


def clean_title(title):
    return re.sub(r"\s+", " ", title.replace("{", "").replace("}", "")).strip()


def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def http_get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.load(resp)


def query_crossref(title, mailto):
    params = {"query.bibliographic": title, "rows": "3"}
    if mailto:
        params["mailto"] = mailto
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    results = []
    for item in data.get("message", {}).get("items", []):
        cand_title = clean_title(" ".join(item.get("title", []) or [""]))
        venue = " ".join(item.get("container-title", []) or [""])
        year = None
        for date_field in ("published-print", "published-online", "issued"):
            parts = item.get(date_field, {}).get("date-parts", [[None]])
            if parts and parts[0] and parts[0][0]:
                year = parts[0][0]
                break
        results.append({"title": cand_title, "venue": venue, "year": year,
                        "doi": item.get("DOI"), "source": "crossref"})
    return results


def query_openalex(title, mailto):
    params = {"search": title, "per-page": "3"}
    if mailto:
        params["mailto"] = mailto
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    results = []
    for item in data.get("results", []):
        loc = (item.get("primary_location") or {}).get("source") or {}
        results.append({"title": clean_title(item.get("title") or ""),
                        "venue": loc.get("display_name") or "",
                        "year": item.get("publication_year"),
                        "doi": (item.get("doi") or "").replace(
                            "https://doi.org/", ""),
                        "source": "openalex"})
    return results


def best_match(title, candidates):
    scored = [(similarity(title, c["title"]), c) for c in candidates
              if c["title"]]
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return scored[0] if scored else (0.0, None)


def is_arxiv(fields):
    """arXiv-only means an arXiv trace AND no published venue field."""
    venue = (fields.get("journal", "") + fields.get("booktitle", "")).lower()
    if venue and "arxiv" not in venue:
        return False
    joined = " ".join(fields.get(k, "") for k in
                      ("journal", "booktitle", "archiveprefix", "eprint",
                       "note", "howpublished", "url")).lower()
    return "arxiv" in joined


def verify_entry(entry, mailto):
    fields = entry["fields"]
    title = clean_title(fields.get("title", ""))
    if not title:
        return {"key": entry["key"], "status": "NO_TITLE"}
    backend_errors = 0
    for backend in (query_crossref, query_openalex):
        try:
            candidates = backend(title, mailto)
        except Exception as exc:  # network errors are reported, not hidden
            print(f"  note: {backend.__name__} failed for {entry['key']}: "
                  f"{exc}", file=sys.stderr)
            backend_errors += 1
            candidates = []
        if candidates:
            score, cand = best_match(title, candidates)
            if cand and score >= MATCH_THRESHOLD:
                bib_year = fields.get("year", "")
                if is_arxiv(fields):
                    status = "ARXIV_ONLY"
                elif not bib_year or not cand["year"]:
                    status = "PARTIAL"  # year comparison impossible
                elif str(cand["year"]) == str(bib_year):
                    status = "VERIFIED"
                else:
                    status = "MISMATCH"
                return {"key": entry["key"], "status": status,
                        "score": round(score, 2), "index_title": cand["title"],
                        "index_venue": cand["venue"],
                        "index_year": cand["year"], "doi": cand["doi"],
                        "bib_year": bib_year, "source": cand["source"]}
        time.sleep(SLEEP_BETWEEN)
    if backend_errors == 2:
        # No backend completed a search: absence of evidence only.
        return {"key": entry["key"], "status": "LOOKUP_ERROR",
                "bib_title": title}
    return {"key": entry["key"], "status": "NOT_FOUND", "bib_title": title}


def main():
    path, mailto, limit = parse_args(sys.argv)
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        print(f"ERROR: cannot read {path}: {exc}", file=sys.stderr)
        sys.exit(2)
    entries = parse_bib(text)
    if not entries:
        print("ERROR: no bib entries parsed", file=sys.stderr)
        sys.exit(1)
    if limit:
        entries = entries[:limit]
    print(f"== Citation verification: {len(entries)} entries from {path} ==")
    counts = {}
    for entry in entries:
        result = verify_entry(entry, mailto)
        counts[result["status"]] = counts.get(result["status"], 0) + 1
        line = f"[{result['status']}] {result['key']}"
        if result["status"] in ("VERIFIED", "MISMATCH", "ARXIV_ONLY",
                                "PARTIAL"):
            line += (f"  -> {result['index_venue']} ({result['index_year']}) "
                     f"doi:{result['doi']} score:{result['score']} "
                     f"via:{result['source']}")
            if result["status"] == "MISMATCH":
                line += f"  [bib year: {result['bib_year']}]"
        print(line)
        time.sleep(SLEEP_BETWEEN)
    print("== Summary ==")
    for status in sorted(counts):
        print(f"{status}: {counts[status]}")
    print("Policy: NOT_FOUND entries do not exist for manuscript purposes "
          "(L1). ARXIV_ONLY entries need a published-version search or a "
          "user ruling (L3). MISMATCH entries need a year/venue fix (L4). "
          "PARTIAL means a year was unavailable on one side; confirm "
          "manually. LOOKUP_ERROR means no backend completed the search; "
          "re-run before drawing any conclusion.")


if __name__ == "__main__":
    main()
