#!/usr/bin/env python3
"""Referent check for demonstratives and pronouns (dependency-free).

Lists every this/these/those/such/it/its/they/their/them and every sentence-type
", which" in a LaTeX manuscript, with the candidate antecedents from the same
sentence and the previous sentence, so each can be confirmed or replaced by a
noun. Implements the referent test of core/rules/sentence-craft.md SC6.

Usage:
    pronoun_check.py DRAFT.tex [MORE.tex ...] [--json] [--quiet]

Levels:
    H  bare demonstrative ("This shows ..."), no candidate in
       the sentence or the previous one, or a pronoun in a paragraph-opening
       sentence pointing backwards.
    S  more than one candidate, or "This/These + noun" whose noun is absent from
       the previous sentence.
    I  exactly one candidate: confirm and move on.

Exit status 1 when an H remains, 2 on a usage or file error.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PRONOUN = re.compile(r"\b(this|these|those|such|it|its|they|their|them)\b", re.I)
DET = re.compile(r"\b(this|these|those|such)\s+([a-z][a-z-]*)", re.I)
NOUN = re.compile(r"\b([a-z][a-z-]{2,})\b")
STOP = set("""the a an of in on at to for from by with and or but not no all any each every this that these
those it its they their them we our us is are was were be been being has have had do does did can may might
must should would could will than then thus therefore also only same other another one two three four five
six seven more most less least much many few such as if when while where which who whom whose what how very
still even yet so but fig sec supp table eq not here there""".split())


def strip_comments(tex: str) -> str:
    out = []
    for line in tex.splitlines():
        i = 0
        while True:
            j = line.find("%", i)
            if j < 0:
                out.append(line)
                break
            b = 0
            k = j - 1
            while k >= 0 and line[k] == "\\":
                b += 1
                k -= 1
            if b % 2 == 0:
                out.append(line[:j])
                break
            i = j + 1
    return "\n".join(out)


def plain(tex: str) -> str:
    tex = re.sub(r"\\begin\{(figure\*?|table\*?|equation\*?|align\*?)\}.*?\\end\{\1\}", " ", tex, flags=re.S)
    tex = re.sub(r"\\(?:mbox|emph|textbf|textit|texttt|mathrm|text)\{([^{}]*)\}", r"\1", tex)
    tex = re.sub(r"~?\\cite[tp]?\{[^}]*\}|\\ref\*?\{[^}]*\}|\\label\{[^}]*\}", " ", tex)
    tex = re.sub(r"\\(?:sub)*section\*?\{[^}]*\}|\\(?:sub)*section\*?\{[^}]*\}", "\n\n", tex)
    tex = re.sub(r"\$[^$]{0,40}\$", " X ", tex)
    tex = tex.replace("~", " ").replace("\\\\", "\n")
    tex = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?", " ", tex)
    tex = re.sub(r"[{}]", "", tex)
    return re.sub(r"[ \t]+", " ", tex)


SENT = re.compile(r"(?<=[.!?])\s+(?=[A-Z(])")


def paragraphs(text: str) -> list[list[str]]:
    out = []
    for block in re.split(r"\n\s*\n", text):
        block = block.strip()
        if not block:
            continue
        sents = [s.strip() for s in SENT.split(block) if s.strip()]
        if sents:
            out.append(sents)
    return out


def nouns(s: str) -> list[str]:
    return [w for w in NOUN.findall(s.lower()) if w not in STOP]


def check(path: Path) -> list[dict]:
    items = []
    for para in paragraphs(plain(strip_comments(path.read_text(errors="replace")))):
        for i, s in enumerate(para):
            prev = para[i - 1] if i else ""
            prev_nouns = nouns(prev)
            for m in PRONOUN.finditer(s):
                w = m.group(1).lower()
                d = DET.match(s[m.start():])
                if d and d.group(2).lower() in {"is", "are", "was", "were", "shows", "show", "means", "suggests", "implies", "indicates", "confirms"}:
                    items.append(level(path, i, s, w, "H", f"bare '{w}': name the object"))
                    continue
                if d:
                    noun = d.group(2)
                    if prev and noun not in prev.lower() and noun not in s.lower()[:m.start()].lower():
                        items.append(level(path, i, s, w, "S",
                                           f"'{w} {noun}': the noun is not in the previous sentence"))
                    else:
                        items.append(level(path, i, s, w, "I", f"'{w} {noun}': confirm the antecedent"))
                    continue
                same = nouns(s[:m.start()])
                if not prev and not same:
                    items.append(level(path, i, s, w, "H",
                                       f"'{w}' points outside the paragraph (paragraph opening)"))
                    continue
                cand = sorted(set(same) | set(prev_nouns))
                if not cand:
                    items.append(level(path, i, s, w, "H",
                                       f"'{w}': no candidate antecedent in this or the previous sentence"))
                elif len(cand) > 1:
                    items.append(level(path, i, s, w, "S",
                                       f"'{w}': candidates {', '.join(cand[:5])}"))
                else:
                    items.append(level(path, i, s, w, "I", f"'{w}' -> {cand[0]}"))
            m = re.search(r",\s+which\s", s)
            if m:
                items.append(level(path, i, s, "which", "S", "sentence-type ', which': name the object"))
    return items


def level(path, i, s, word, lvl, msg):
    return {"file": str(path), "paragraph_sentence": i + 1, "word": word,
            "level": lvl, "message": msg, "sentence": s[:160]}


def main(argv: list[str]) -> int:
    as_json = "--json" in argv
    quiet = "--quiet" in argv
    files = [a for a in argv if not a.startswith("-")]
    if not files:
        print("usage: pronoun_check.py DRAFT.tex [--json] [--quiet]", file=sys.stderr)
        return 2
    all_items = []
    for f in files:
        p = Path(f)
        if not p.is_file():
            print(f"ERROR: {f} is not a file", file=sys.stderr)
            return 2
        all_items.extend(check(p))
    shown = [x for x in all_items if not (quiet and x["level"] == "I")]
    if as_json:
        print(json.dumps({"items": shown, "summary": {
            lv: sum(1 for x in all_items if x["level"] == lv) for lv in "HSI"}}, indent=1))
    else:
        for x in shown:
            print(f"{x['file']} s{x['paragraph_sentence']} [{x['level']}] {x['message']}")
            print(f"    {x['sentence'][:140]}")
        print("summary: H=%d S=%d I=%d" % tuple(sum(1 for x in all_items if x["level"] == lv) for lv in "HSI"))
    return 1 if any(x["level"] == "H" for x in all_items) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
