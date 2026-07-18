#!/usr/bin/env bash
# (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite.
# Measured word count of the abstract environment (V1: measure, never
# estimate). Usage: wordcount_abstract.sh <main.tex>
set -u

if [ $# -lt 1 ] || [ ! -f "$1" ]; then
  echo "ERROR: usage: wordcount_abstract.sh <main.tex>" >&2
  exit 2
fi

# Comments are stripped BEFORE locating the abstract, so a commented-out
# \begin{abstract} can never select the wrong region.
ABS=$(perl -pe 's/((?:^|[^\\])(?:\\\\)*)%.*/$1/' "$1" \
  | sed -n '/\\begin{abstract}/,/\\end{abstract}/p' \
  | sed -e 's/\\begin{abstract}//' -e 's/\\end{abstract}//' \
        -e 's/\\[a-zA-Z@]*//g' -e 's/[{}]//g' -e 's/~/ /g')

if [ -z "$(printf '%s' "$ABS" | tr -d '[:space:]')" ]; then
  echo "ERROR: no abstract environment found in $1" >&2
  exit 1
fi

COUNT=$(printf '%s\n' "$ABS" | wc -w)
echo "abstract-words: $COUNT"

# Secondary, informational only: a TeX-aware count when texcount exists.
# The gate stays on the primary stripped-wc metric (the project's
# established counting convention).
if command -v texcount >/dev/null 2>&1; then
  RAWTMP=$(mktemp --suffix=.tex)
  perl -pe 's/((?:^|[^\\])(?:\\\\)*)%.*/$1/' "$1" \
    | sed -n '/\\begin{abstract}/,/\\end{abstract}/p' > "$RAWTMP"
  TCOUNT=$(texcount -1 -sum -q "$RAWTMP" 2>/dev/null | grep -oE '^[0-9]+' | head -1)
  rm -f "$RAWTMP"
  [ -n "${TCOUNT:-}" ] && echo "texcount-words: $TCOUNT (informational)"
fi
if [ "$COUNT" -lt 150 ] || [ "$COUNT" -gt 250 ]; then
  echo "GATE: FAIL (outside 150-250; see core/templates/ieee-facts.md)"
  exit 1
else
  echo "GATE: PASS (150-250; target 230-250)"
fi
