#!/usr/bin/env python3
# (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite.
"""Verify every entry of a .bib file against live bibliographic indexes.

Backends: Crossref (primary), OpenAlex (fallback). Both work without an API
key. For each entry the script reports one of:
  VERIFIED      title, year, and venue all consistent with the index
  CHECK_VENUE   title+year match, but the bib venue reads differently
  PARTIAL       title matched, a year was unavailable on one side
  MISMATCH      title matched, years differ
  ARXIV_ONLY    the bib entry itself cites arXiv with no published venue
  NOT_FOUND     no index locates the title (searches completed)
  LOOKUP_ERROR  no backend completed a search; absence NOT established
Nothing is ever guessed (L1). The bib parser handles braced and
parenthesized entries, @comment/@string/@preamble blocks, nested braces,
quoted values, and # concatenation; malformed input is reported, never
silently skipped.

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
VENUE_TOKEN_THRESHOLD = 0.6
USER_AGENT = "ieee-paper-suite-citation-check/1.2"
SKIP_TYPES = {"comment", "string", "preamble"}
VENUE_STOPWORDS = {"the", "of", "on", "in", "and", "for", "a", "an"}


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


def parse_fields(body):
    """Parse 'name = value' pairs from an entry body. Values may be braced
    groups (nested), quoted strings, bare words, and #-concatenations."""
    fields = {}
    i, n = 0, len(body)
    name_re = re.compile(r"\s*(\w+)\s*=\s*")
    word_re = re.compile(r"[\w.+:/-]+")
    concat_re = re.compile(r"\s*#\s*")
    comma_re = re.compile(r"\s*,\s*")
    while i < n:
        match = name_re.match(body, i)
        if not match:
            nxt = body.find(",", i)
            if nxt == -1:
                break
            i = nxt + 1
            continue
        name = match.group(1).lower()
        i = match.end()
        parts = []
        while True:
            if i < n and body[i] == "{":
                depth, j = 1, i + 1
                while j < n and depth > 0:
                    if body[j] == "{":
                        depth += 1
                    elif body[j] == "}":
                        depth -= 1
                    j += 1
                parts.append(body[i + 1:j - 1])
                i = j
            elif i < n and body[i] == '"':
                j = i + 1
                while j < n and not (body[j] == '"' and body[j - 1] != "\\"):
                    j += 1
                parts.append(body[i + 1:j])
                i = j + 1
            else:
                word = word_re.match(body, i)
                if word:
                    parts.append(word.group(0))
                    i = word.end()
                else:
                    i += 1
            cont = concat_re.match(body, i)
            if cont:
                i = cont.end()
                continue
            break
        fields[name] = re.sub(r"\s+", " ", "".join(parts)).strip()
        comma = comma_re.match(body, i)
        if comma:
            i = comma.end()
        else:
            nxt = body.find(",", i)
            if nxt == -1:
                break
            i = nxt + 1
    return fields


def parse_bib(text):
    """Sequential tokenizer. Returns (entries, errors). Text between
    entries (including % comment lines) is ignored by construction, and
    @comment bodies are consumed so entry-like text inside cannot leak."""
    entries, errors = [], []
    i, n = 0, len(text)
    head_re = re.compile(r"@\s*(\w+)\s*([({])")
    while True:
        at = text.find("@", i)
        if at == -1:
            break
        head = head_re.match(text, at)
        if not head:
            i = at + 1
            continue
        etype, open_ch = head.group(1).lower(), head.group(2)
        body_start = head.end()
        if open_ch == "{":
            depth, pos = 1, body_start
            while pos < n and depth > 0:
                if text[pos] == "{":
                    depth += 1
                elif text[pos] == "}":
                    depth -= 1
                pos += 1
            if depth != 0:
                errors.append(f"unbalanced braces in @{etype} near offset {at}")
                break
            body, i = text[body_start:pos - 1], pos
        else:
            brace, pos = 0, body_start
            while pos < n:
                ch = text[pos]
                if ch == "{":
                    brace += 1
                elif ch == "}":
                    brace -= 1
                elif ch == ")" and brace == 0:
                    break
                pos += 1
            if pos >= n:
                errors.append(f"unterminated @{etype}(...) near offset {at}")
                break
            body, i = text[body_start:pos], pos + 1
        if etype in SKIP_TYPES:
            continue
        key_match = re.match(r"\s*([^,\s]+)\s*,", body)
        if not key_match:
            errors.append(f"@{etype} near offset {at} has no citation key")
            continue
        entries.append({"key": key_match.group(1), "type": etype,
                        "fields": parse_fields(body[key_match.end():])})
    return entries, errors


def normalize_latex(text):
    """Best-effort LaTeX-to-plain normalization for queries and matching."""
    t = re.sub(r"\$[^$]*\$", " ", text)
    t = t.replace(r"\&", "&").replace(r"\%", "%").replace(r"\_", "_")
    t = re.sub(r"\\[`'^\"~=.uvHtcdb]\s*\{?([a-zA-Z])\}?", r"\1", t)
    t = re.sub(r"\\[a-zA-Z]+\s*", " ", t)
    t = t.replace("{", "").replace("}", "").replace("~", " ")
    t = t.replace("``", " ").replace("''", " ")
    return re.sub(r"\s+", " ", t).strip()


def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def venue_similar(bib_venue, index_venue):
    """Prefix-token heuristic tolerant of IEEE abbreviations
    ('Trans.' vs 'Transactions'). Returns True/False, or None when either
    side is missing (no judgment possible)."""
    if not bib_venue or not index_venue:
        return None
    bib_tokens = [w.rstrip(".") for w in
                  re.split(r"[^a-zA-Z0-9.]+", normalize_latex(bib_venue).lower())
                  if w and w.rstrip(".") not in VENUE_STOPWORDS]
    idx_tokens = [w for w in re.split(r"[^a-z0-9]+", index_venue.lower())
                  if w and w not in VENUE_STOPWORDS]
    if not bib_tokens or not idx_tokens:
        return None
    matched = sum(1 for w in bib_tokens
                  if any(x.startswith(w) for x in idx_tokens))
    return matched / len(bib_tokens) >= VENUE_TOKEN_THRESHOLD


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
        year = None
        for date_field in ("published-print", "published-online", "issued"):
            parts = item.get(date_field, {}).get("date-parts", [[None]])
            if parts and parts[0] and parts[0][0]:
                year = parts[0][0]
                break
        results.append({"title": " ".join(item.get("title", []) or [""]),
                        "venue": " ".join(item.get("container-title", []) or [""]),
                        "year": year, "doi": item.get("DOI"),
                        "source": "crossref"})
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
        results.append({"title": item.get("title") or "",
                        "venue": loc.get("display_name") or "",
                        "year": item.get("publication_year"),
                        "doi": (item.get("doi") or "").replace(
                            "https://doi.org/", ""),
                        "source": "openalex"})
    return results


def best_match(title, candidates):
    scored = [(similarity(title, normalize_latex(c["title"])), c)
              for c in candidates if c["title"]]
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


def classify(fields, cand):
    if is_arxiv(fields):
        return "ARXIV_ONLY"
    bib_year = fields.get("year", "")
    if not bib_year or not cand["year"]:
        return "PARTIAL"
    if str(cand["year"]) != str(bib_year):
        return "MISMATCH"
    similar = venue_similar(fields.get("journal") or fields.get("booktitle"),
                            cand["venue"])
    if similar is False:
        return "CHECK_VENUE"
    return "VERIFIED"


def verify_entry(entry, mailto):
    fields = entry["fields"]
    title = normalize_latex(fields.get("title", ""))
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
                return {"key": entry["key"],
                        "status": classify(fields, cand),
                        "score": round(score, 2),
                        "index_venue": cand["venue"],
                        "index_year": cand["year"], "doi": cand["doi"],
                        "bib_year": fields.get("year", ""),
                        "source": cand["source"]}
        time.sleep(SLEEP_BETWEEN)
    if backend_errors == 2:
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
    entries, errors = parse_bib(text)
    for err in errors:
        print(f"[PARSE_ERROR] {err}")
    if not entries:
        print("ERROR: no bib entries parsed", file=sys.stderr)
        sys.exit(1)
    if limit:
        entries = entries[:limit]
    print(f"== Citation verification: {len(entries)} entries from {path} ==")
    counts = {}
    if errors:
        counts["PARSE_ERROR"] = len(errors)
    for entry in entries:
        result = verify_entry(entry, mailto)
        counts[result["status"]] = counts.get(result["status"], 0) + 1
        line = f"[{result['status']}] {result['key']}"
        if "index_venue" in result:
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
          "user ruling (L3). MISMATCH entries need a year fix, and "
          "CHECK_VENUE entries need a venue-name check (L4). PARTIAL means "
          "a year was unavailable on one side; confirm manually. "
          "LOOKUP_ERROR means no backend completed the search; re-run "
          "before drawing any conclusion.")


if __name__ == "__main__":
    main()
