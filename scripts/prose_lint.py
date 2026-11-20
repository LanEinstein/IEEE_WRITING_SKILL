#!/usr/bin/env python3
"""Structural prose lint for a LaTeX manuscript (dependency-free).

Reports candidates for the rules in core/rules/translation-discipline.md,
sentence-craft.md, lexicon.md and paragraph-architecture.md. It detects
structures, not meaning: a zero count means "no known defect pattern", never
"good English".

Usage:
    prose_lint.py DRAFT.tex [MORE.tex ...] [options]

Options:
    --include-floats     also scan figure/table bodies (captions are always scanned)
    --quiet              hide I-level prompts
    --json               machine-readable output
    --banned FILE        project lexicon: one "pattern => reason" per line (regex left side)
    --max-words N        sentence length limit (default 38)
    --no-color

Levels:
    H  hard fault (known rejected structure, house ban, or near-absent in published
       prose): rewrite before delivery.
    S  soft: a candidate for manual review; keep it only with a stated reason.
    I  information: prompts for the manual tests (linking, causal reading).

Exit status: 0 when no H hit and no file error, 1 when an H hit remains,
2 on a usage or file error.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# --------------------------------------------------------------------------- LaTeX to sentences
FLOAT_ENV = r"figure\*?|table\*?|algorithm\*?|algorithmic|equation\*?|align\*?|tabular\*?|longtable"
ABBREV = [
    (r"Sec\.", "Sec<d>"), (r"Secs\.", "Secs<d>"), (r"Fig\.", "Fig<d>"), (r"Figs\.", "Figs<d>"),
    (r"Supp\.", "Supp<d>"), (r"Eq\.", "Eq<d>"), (r"Eqs\.", "Eqs<d>"), (r"et al\.", "et al<d>"),
    (r"e\.g\.", "e<d>g<d>"), (r"i\.e\.", "i<d>e<d>"), (r"vs\.", "vs<d>"), (r"cf\.", "cf<d>"),
    (r"No\.", "No<d>"), (r"approx\.", "approx<d>"), (r"resp\.", "resp<d>"),
]


def strip_comments(tex: str) -> str:
    out = []
    for line in tex.splitlines():
        i = 0
        while True:
            j = line.find("%", i)
            if j < 0:
                out.append(line)
                break
            backslashes = 0
            k = j - 1
            while k >= 0 and line[k] == "\\":
                backslashes += 1
                k -= 1
            if backslashes % 2 == 0:
                out.append(line[:j])
                break
            i = j + 1
    return "\n".join(out)


def capture_floats(tex: str) -> tuple[str, list[str]]:
    """Return the caption text of every float, so captions can be linted separately."""
    caps = []
    body = []
    end = 0
    for m in re.finditer(r"\\caption(?:\[[^\]]*\])?\{", tex):
        depth, start = 1, m.end()
        i = start
        while i < len(tex) and depth:
            if tex[i] == "{" and tex[i - 1] != "\\":
                depth += 1
            elif tex[i] == "}" and tex[i - 1] != "\\":
                depth -= 1
            i += 1
        if m.start() < end:
            continue
        caps.append(tex[start:i - 1])
        body.extend([tex[end:m.start()], " "])
        end = i
    body.append(tex[end:])
    return "".join(body), caps


def detex(tex: str) -> str:
    tex = re.sub(r"\\(?:mbox|emph|textbf|textit|texttt|mathrm|text|textrm)\{([^{}]*)\}", r"\1", tex)
    tex = re.sub(r"~?\\cite[tp]?\{[^}]*\}", "", tex)
    tex = re.sub(r"\\ref\*?\{[^}]*\}|\\eqref\{[^}]*\}", "1", tex)
    tex = re.sub(r"\\label\{[^}]*\}", "", tex)
    tex = re.sub(r"\\(?:sub)*section\*?\{[^}]*\}", "\n\n", tex)
    tex = re.sub(r"\\paragraph\{[^}]*\}", "\n\n", tex)
    tex = re.sub(r"\\item\b", "\n", tex)
    tex = re.sub(r"\$\\?[A-Z][A-Za-z]*\$\s*|\$([^$]{0,20})\$", lambda m: " X ", tex)
    tex = tex.replace("~", " ").replace("---", " ").replace("--", "-")
    tex = tex.replace("\\%", "%").replace("\\\\", "\n")
    tex = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?", " ", tex)
    tex = re.sub(r"[{}]", "", tex)
    for pat, rep in ABBREV:
        tex = re.sub(pat, rep, tex)
    return tex


SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z(])")


def paragraphs(tex: str) -> list[list[str]]:
    text = detex(tex)
    text = re.sub(r"[ \t]+", " ", text)
    out = []
    for block in re.split(r"\n\s*\n", text):
        block = block.strip()
        if not block:
            continue
        paragraph = []
        for s in SENT_SPLIT.split(block):
            s = s.strip()
            if s:
                paragraph.append(s.replace("<d>", "."))
        if paragraph:
            out.append(paragraph)
    return out


# --------------------------------------------------------------------------- word lists
OPENERS_H = ["Because", "Since", "Like", "Relative to", "In terms of", "On this basis", "With the help of",
             "Compared with", "Compared to", "Due to", "Owing to", "Thanks to", "Together with", "Without",
             "As for", "Regarding", "In view of", "Along with", "Apart from", "With respect to"]
OPENERS_S = ["Under", "Beyond", "Through", "With", "Given", "Based on", "By", "Unlike", "After", "Upon",
             "Besides", "As"]
FORMULAIC = re.compile(r"^(As (shown|illustrated|reported|listed|described|in|a result|expected|opposed)|"
                       r"Based on|Given|Following|According to|In contrast|In addition|In particular)\b")
NOT_PARTICIPLE = {"When", "Then", "Even", "Often", "Seven", "Ten", "Between", "Indeed", "Open", "Using"}
SUBJECT_START = re.compile(r"(the|a|an|our|we|each|every|both|all|one|two|three|this|these|it)\b|^[A-Z][\w-]*\b")

CALQUES = [
    (r"\bearlier (methods?|work|studies|approaches)\b", "'earlier X' renders a Chinese time frame; write 'prior'"),
    (r"\bin favou?r of\b", "name the setting instead of 'in favour of'"),
    (r"\bfrom the original papers?\b", "say 'from the source records' or name the source"),
    (r"\bclos(e|es|ed|ing) (identities|over)\b", "'close identities/over' renders a Chinese metaphor; use 'separates'"),
    (r"\bnumbers? +\d", "'number' as a verb; use 'contains' or state the count"),
    (r"\b(do|does|did) +(?!not\b|so\b|this\b|that\b|the\b|a\b|an\b|we\b|it\b|they\b|well\b|better\b|worse\b)[a-z]+ed\b",
     "emphatic 'do' renders a Chinese intensifier"),
    (r"\bso as to\b", "'so as to' renders a purpose clause; use 'to'"),
    (r"\bplays? an? (important|key|vital|crucial) role\b", "empty role phrase"),
    (r"\bmore and more\b", "use 'increasingly'"),
    (r"\bwith the (development|help|rapid development) of\b", "translated frame"),
    (r"\bthe reason is (that|because)\b|\bit is because\b", "translated causal frame"),
    (r"\ba first classifier layer\b", "decorative qualifier"),
    (r"\bby itself\b|\bper se\b", "decorative emphasis"),
    (r"\bneutral\b", "check whether 'neutral' carries information"),
]

BANNED = [
    (r"\brather than\b", "'rather than': state results positively (project default)"),
    (r"\binstead of\b", "'instead of': prefer a positive statement"),
    (r"\bvia\b", "'via': name the operation"),
    (r"\b(use|uses|used)\b(?!\s+to\b)", "low-register 'use' for introducing a component"),
    (r"\b(get|gets|got|gotten|lose|loses|lost)\b", "low-register get/lose"),
    (r"\b(recipes?|registered|refits?|twin arms?|run plans?|training runs?|packages?)\b", "engineering vocabulary"),
    (r"\b(the|a) fits?\b|\bfitted\b", "'fit' as a noun/verb of model training"),
    (r"\bmarkedly\b", "rare adverb; 'substantially' is commoner in the field"),
    (r"\bTo test whether\b", "repeated opening frame"),
    (r"\b(on par|on bar) with\b", "informal comparison"),
]

SOFT = [
    (r"\b(significant|significantly)\b", "'significant' needs a stated test"),
    (r"\b(very|quite|really|a lot|lots of|huge|big)\b", "informal intensifier"),
    (r"\b(clearly|obviously|of course)\b", "claim smuggled in as obviously"),
    (r"\b(always|never)\b", "absolute"),
    (r"\b(any)\b", "absolute quantifier: check whether the evidence covers all"),
    (r"\b(every|all)\b", "universal quantifier: check the tested scope"),
]

CAUSAL = ["therefore", "thus", "hence", "so", "consequently", "accordingly", "thereby", "as a result"]
LIMITER_H = ["only", "also", "alone", "still", "nearly", "even", "again", "indeed"]
LIMITER_S = ["every", "each", "all", "both", "exactly", "entirely"]
CONNECTIVE_H = ["however", "therefore", "thus", "hence", "so", "moreover", "furthermore", "consequently",
                "similarly", "likewise", "whereas", "although", "only", "alone"]
CONNECTIVE = CONNECTIVE_H + ["yet", "but", "meanwhile", "conversely", "still", "then", "besides", "finally",
                             "specifically", "also"]
LINK_OPEN = re.compile(r"^(However|Therefore|Thus|Hence|Yet|But|So|Also|Moreover|Furthermore|In contrast|"
                       r"Conversely|Similarly|Likewise|Consequently|Accordingly|Nevertheless|Although|"
                       r"Though|While|Whereas|To |In addition|Beyond|Unlike|Overall|In particular|"
                       r"Specifically|Notably|This [a-z]+|These [a-z]+|The results|The same|Both)\b")
LINK_INSIDE = re.compile(r"\b(thus|therefore|hence|likewise|similarly|also|however|in contrast|as well|"
                         r"thereby|consequently|accordingly|nevertheless)\b")
STOP = set("""a an the of in on at to for from by with and or but nor yet as is are was were be been being
that which who whom whose what when where while than then thus therefore hence also both each every all any
no not only same other another one two three four five six seven its it this these those their they them we
our us into onto over under between within without across through per up down out about after before more
most less least much many few far such can may might must should would could will has have had do does did
fig sec secs supp table eq et al""".split())


def words(s: str) -> list[str]:
    return [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'-]*", s)]


# --------------------------------------------------------------------------- sentence rules
def opener_hits(s: str) -> list[tuple[str, str, str]]:
    hits = []
    for o in OPENERS_H:
        if re.match(re.escape(o) + r"\b", s):
            hits.append(("O1", "H", f"sentence-initial '{o}': condition or cause before the main clause"))
            break
    else:
        for o in OPENERS_S:
            if re.match(re.escape(o) + r"\b", s) and not FORMULAIC.match(s):
                hits.append(("O1", "S", f"sentence-initial '{o}': keep the frame short"))
                break
    head, _, rest = s.partition(",")
    if rest and SUBJECT_START.match(rest.strip()) and len(head.split()) <= 15 and not FORMULAIC.match(s):
        first = s.split()[0].strip(",")
        long_head = len(head.split()) >= 6
        if re.fullmatch(r"[A-Z][a-z]+(ed|en)", first) and first not in NOT_PARTICIPLE:
            hits.append(("O2", "H" if long_head else "S",
                         f"participial opener '{head},': modifiers before the subject"
                         + ("" if long_head else " (short frame: acceptable if the participle's subject is the main subject)")))
        elif re.fullmatch(r"[A-Z][a-z]+ing", first) and first not in NOT_PARTICIPLE:
            hits.append(("O2", "H" if long_head else "S", f"-ing opener '{head},': dangling or abstract?"))
    if rest and len(head.split()) >= 9 and re.match(
            r"(In|On|At|For|With|Under|Beyond|Through|By|After|When|If|While|Although|To|As|Since|Because|"
            r"Without|Given|Unlike|Relative)\b", s):
        hits.append(("O3", "S", f"{len(head.split())} words before the first comma"))
    if len(re.findall(r"\bwithout\b", s, re.I)) >= 2 or re.search(r"\bwhereas (without|with|under)\b", s, re.I):
        hits.append(("O4", "H", "parallel conditional heads; take the operation as subject"))
    return hits


def connective_hits(s: str) -> list[tuple[str, str, str]]:
    hits, low = [], s.lower()
    if re.search(r"\b(because|since)\b.*\b(so|therefore|thus|hence)\b", low) or \
            re.search(r"\b(so|therefore|thus|hence)\b.*\bbecause\b", low):
        hits.append(("C1", "H", "paired cause-effect connectives in one sentence"))
    if re.search(r"\b(although|though|even though)\b[^.]*\b(but|yet)\b", low):
        hits.append(("C1", "H", "'although ... but/yet' in one sentence"))
    if re.search(r"\b(therefore|thus|hence|so)\b", low) and re.search(r"\((Fig|Table|Tab|Sec)\b", s):
        hits.append(("C2", "S", "consequence connective in an evidence sentence"))
    for c in CAUSAL:
        for m in re.finditer(r"\b%s\b" % re.escape(c), low):
            left = s[max(0, m.start() - 60):m.start()].strip()
            right = s[m.end():m.end() + 60].strip()
            hits.append(("C3", "I", f"'{c}': ...{left} -> {right}... (follows from the premise?)"))
    return hits


def lexical_hits(s: str, banned_extra: list[tuple[str, str]]) -> list[tuple[str, str, str]]:
    hits = []
    for pat, why in CALQUES:
        m = re.search(pat, s, 0 if pat.startswith(r"\b(do") else re.I)
        if m:
            hits.append(("W1", "H", f"'{m.group(0)}': {why}"))
    if re.search(r"\b(what|which|how|whether)\b[^.;:,]{0,60}\b(how (much|many|far|well)|what|which|whether)\b",
                 s, re.I):
        hits.append(("W2", "H", "stacked wh-clauses; use a noun-phrase object"))
    for pat, why in BANNED + banned_extra:
        for m in re.finditer(pat, s, 0 if pat.startswith(r"\bTo") else re.I):
            hits.append(("L1", "H", f"'{m.group(0)}': {why}"))
    for pat, why in SOFT:
        for m in re.finditer(pat, s, re.I):
            hits.append(("L2", "S", f"'{m.group(0)}': {why}"))
    return hits


def structure_hits(s: str, max_words: int) -> list[tuple[str, str, str]]:
    hits = []
    n = len(s.split())
    if n > max_words:
        hits.append(("S1", "S", f"{n} words: one point per sentence"))
    k = len(re.findall(r"\b(in|on)\b", s, re.I))
    if k >= 4 or re.search(r"\bin \w+(?: \w+)? and in\b", s):
        hits.append(("S2", "S", f"{k} x in/on: preposition pile"))
    if s.count(":") >= 1:
        hits.append(("S3", "H", "colon in prose; use a full stop or reorder"))
    if s.count(",") >= 5:
        hits.append(("S4", "S", f"{s.count(',')} commas: stacked insertions"))
    if re.search(r"^[^,]{3,60}, which [^,]{5,80}, the\b", s):
        hits.append(("S4", "S", "relative clause inserted before the subject"))
    if s.count(";") >= 1:
        hits.append(("S5", "S", "semicolon in prose: split the sentence"))
    return hits


# --------------------------------------------------------------------------- paragraph rules
def paragraph_hits(sents: list[str]) -> dict[int, list[tuple[str, str, str]]]:
    out: dict[int, list[tuple[str, str, str]]] = defaultdict(list)
    seen: Counter = Counter()
    for i, s in enumerate(sents):
        w = words(s)
        low = s.lower()
        for c in CONNECTIVE:
            k = len(re.findall(r"\b%s\b" % c, low))
            if k and (seen[c] or k > 1):
                lvl = "H" if c in CONNECTIVE_H else "S"
                out[i].append(("R1", lvl, f"'{c}' twice in one paragraph"))
            seen[c] += k
        for lim in LIMITER_H:
            if w.count(lim) > 1:
                out[i].append(("R2", "H", f"'{lim}' twice in one sentence"))
        for lim in LIMITER_S:
            if w.count(lim) > 1:
                out[i].append(("R2", "S", f"'{lim}' twice in one sentence"))
        pairs = Counter(zip(w, w[1:]))
        for g, k in pairs.items():
            if k > 1 and not set(g) & STOP and all(len(x) > 2 for x in g):
                out[i].append(("R2", "S", f"phrase '{' '.join(g)}' twice in one sentence"))
        if not i:
            continue
        prev = words(sents[i - 1])
        for lim in LIMITER_H:
            if lim in w and lim in prev:
                out[i].append(("R3", "H", f"'{lim}' in adjacent sentences"))
        for lim in LIMITER_S:
            if lim in w and lim in prev:
                out[i].append(("R3", "S", f"'{lim}' in adjacent sentences"))
        if not (LINK_OPEN.match(s) or LINK_INSIDE.search(re.split(r"[:;]", low)[0])):
            prev_content = {x for x in prev if x not in STOP and len(x) > 3}
            head = {x for x in w[:6] if x not in STOP and len(x) > 3}
            if not head & prev_content:
                out[i].append(("F1", "I", "no visible link to the previous sentence or its object"))
    starts = Counter(" ".join(s.split()[:2]) for s in sents)
    for i, s in enumerate(sents):
        if starts[" ".join(s.split()[:2])] > 1 and not s.startswith("The "):
            out[i].append(("F2", "S", f"opening '{' '.join(s.split()[:2])}' repeated in the paragraph"))
    return out


def repetition_report(sents: list[str], top: int = 5) -> list[str]:
    content = [w for s in sents for w in words(s) if w not in STOP and len(w) > 3]
    counts = Counter(content)
    flag = [(w, c) for w, c in counts.most_common(top) if c >= 3]
    return [f"{w} x{c} in the unit" for w, c in flag]


# --------------------------------------------------------------------------- driver
def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--include-floats", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--no-color", action="store_true")
    parser.add_argument("--banned", type=Path)
    parser.add_argument("--max-words", type=int, default=38)
    args = parser.parse_args(argv)

    extra: list[tuple[str, str]] = []
    if args.banned:
        try:
            for line in args.banned.read_text().splitlines():
                if not line.strip() or line.lstrip().startswith("#"):
                    continue
                pat, _, why = line.partition("=>")
                re.compile(pat.strip(), re.I)
                extra.append((pat.strip(), why.strip() or "project lexicon"))
        except (OSError, UnicodeError, re.error) as exc:
            parser.error(str(exc))

    report, totals = [], Counter()
    for path in args.files:
        p = Path(path)
        if not p.is_file():
            print(f"ERROR: {path} is not a file", file=sys.stderr)
            return 2
        tex = strip_comments(p.read_text(errors="replace"))
        tex, caps = capture_floats(tex)
        if not args.include_floats:
            tex = re.sub(r"\\begin\{(%s)\}.*?\\end\{\1\}" % FLOAT_ENV, "\n\n", tex, flags=re.S)
        # Caption bodies are scanned as their own units; never fold them into prose paragraphs.
        prose = paragraphs(tex)
        units = [("prose", prose)] + [("caption", paragraphs(c)) for c in caps]
        file_items = []
        for unit, blocks in units:
            for idx, s, hits in lint_unit(blocks, extra, args.max_words):
                hits = [h for h in hits if not (args.quiet and h[1] == "I")]
                for rid, lvl, _ in hits:
                    totals[lvl] += 1
                    totals[rid + lvl] += 1
                if hits:
                    file_items.append({"unit": unit, "index": idx,
                                       "sentence": s, "hits": hits})
        rep = repetition_report([s for block in prose for s in block])
        report.append({"file": str(p), "items": file_items, "repetition": rep})

    if args.json:
        print(json.dumps({"report": report, "summary": dict(totals)}, indent=1))
    else:
        for block in report:
            print(f"== {block['file']}")
            for it in block["items"]:
                where = f"{it['unit']}#{it['index']}"
                s = it["sentence"]
                print(f"  {where}: {s[:120]}{'...' if len(s) > 120 else ''}")
                for rid, lvl, msg in it["hits"]:
                    print(f"      [{lvl} {rid}] {msg}")
            if block["repetition"]:
                print("  repetition: " + "; ".join(block["repetition"]))
        print("summary: H=%d S=%d I=%d" % (totals["H"], totals["S"], totals["I"]))
        if totals["H"]:
            print("H hits must be rewritten or justified before delivery.")
    return 1 if totals["H"] else 0


def lint_unit(blocks, extra, max_words):
    offset = 0
    for sents in blocks:
        para = paragraph_hits(sents)
        for i, s in enumerate(sents):
            hits = (opener_hits(s) + connective_hits(s) + lexical_hits(s, extra)
                    + structure_hits(s, max_words) + para.get(i, []))
            yield offset + i + 1, s, hits
        offset += len(sents)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
