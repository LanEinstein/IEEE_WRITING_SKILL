#!/usr/bin/env bash
# (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite.
# Measured word count of the abstract environment (V1: measure, never
# estimate). Usage: wordcount_abstract.sh <main.tex>
set -u

if [ $# -lt 1 ] || [ ! -f "$1" ]; then
  echo "ERROR: usage: wordcount_abstract.sh <main.tex>" >&2
  exit 2
fi

ABS=$(sed -n '/\\begin{abstract}/,/\\end{abstract}/p' "$1" \
  | sed -e 's/\\begin{abstract}//' -e 's/\\end{abstract}//' \
        -e 's/\(^\|[^\\]\)%.*/\1/' \
        -e 's/\\[a-zA-Z@]*//g' -e 's/[{}~]//g')

if [ -z "$(printf '%s' "$ABS" | tr -d '[:space:]')" ]; then
  echo "ERROR: no abstract environment found in $1" >&2
  exit 1
fi

COUNT=$(printf '%s\n' "$ABS" | wc -w)
echo "abstract-words: $COUNT"
if [ "$COUNT" -lt 150 ] || [ "$COUNT" -gt 250 ]; then
  echo "GATE: FAIL (outside 150-250; see core/templates/ieee-facts.md)"
  exit 1
else
  echo "GATE: PASS (150-250; target 230-250)"
fi
