#!/usr/bin/env bash
# (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite.
# Compile a manuscript (pdflatex x3 with bibtex) and report:
#   pages / warning count / unresolved references / Overfull boxes with
#   NEW-vs-LEGACY attribution against a stored baseline.
# The log is removed before compiling, so results can never come from a
# stale log, and a failed final pass is reported as COMPILE FAILED instead
# of being parsed as truth.
# Usage:
#   verify_tex.sh <main.tex> [--set-baseline]
set -u

if [ $# -lt 1 ] || [ ! -f "$1" ]; then
  echo "ERROR: usage: verify_tex.sh <main.tex> [--set-baseline]" >&2
  exit 2
fi

TEXFILE=$(readlink -f "$1")
TEXDIR=$(dirname "$TEXFILE")
BASE=$(basename "$TEXFILE" .tex)
BASELINE="$TEXDIR/.ieee_baseline.txt"
SETBASE="${2:-}"

command -v pdflatex >/dev/null 2>&1 || { echo "ERROR: pdflatex not found" >&2; exit 2; }

cd "$TEXDIR" || exit 2
LOG="$BASE.log"
rm -f "$LOG"

run_latex() {
  pdflatex -interaction=nonstopmode "$BASE.tex" >/dev/null 2>&1
}

echo "== Compiling $BASE.tex (pdflatex, bibtex, pdflatex x2) =="
run_latex
if [ -f "$BASE.aux" ] && grep -q '\\citation' "$BASE.aux" 2>/dev/null; then
  if command -v bibtex >/dev/null 2>&1; then
    bibtex "$BASE" >/dev/null 2>&1 || echo "NOTE: bibtex returned nonzero (check $BASE.blg)"
  else
    echo "NOTE: bibtex not found, skipping bibliography pass"
  fi
fi
run_latex
run_latex
FINAL_STATUS=$?

if [ ! -f "$LOG" ]; then
  echo "ERROR: no log file produced" >&2
  exit 1
fi

# Pages: prefer PDF metadata (immune to log line wrapping), log as fallback.
PAGES=""
if command -v pdfinfo >/dev/null 2>&1 && [ -f "$BASE.pdf" ]; then
  PAGES=$(pdfinfo "$BASE.pdf" 2>/dev/null | sed -n 's/^Pages:[[:space:]]*//p')
fi
if [ -z "$PAGES" ]; then
  PAGES=$(grep -oE 'Output written on .*\(([0-9]+) page' "$LOG" | grep -oE '[0-9]+ page' | grep -oE '[0-9]+' | tail -1)
fi

# Real warning records only ("LaTeX Warning:", "Package x Warning:",
# "pdfTeX warning (ext4):"), not package descriptions that mention the word.
WARNINGS=$(grep -ciE 'warning( \([a-z0-9]+\))?:' "$LOG")
[ "$WARNINGS" = "" ] && WARNINGS=0
UNRESOLVED=$(grep -cE 'Warning: (Reference|Citation) .* undefined' "$LOG")
[ "$UNRESOLVED" = "" ] && UNRESOLVED=0
OVERFULL_LINES=$(grep -E '^(Overfull|Underfull) \\[hv]box' "$LOG")
OVERFULL_COUNT=$(printf '%s' "$OVERFULL_LINES" | grep -c .)

echo "pages: ${PAGES:-UNKNOWN}"
echo "warnings: $WARNINGS"
echo "unresolved-references: $UNRESOLVED"
echo "over/underfull-boxes: $OVERFULL_COUNT"

# Signatures: "at line(s) N(--M)" plus badness/size. Not deduplicated, so a
# repeated identical box stays visible.
SIGS=$(printf '%s\n' "$OVERFULL_LINES" | sed -E 's/.*\(([^)]*)\).* at lines? ([0-9-]+).*/\2|\1/;t;s/.+/misc/' | grep -v '^$' | sort || true)

if [ ! -f "$BASELINE" ] || [ "$SETBASE" = "--set-baseline" ]; then
  printf '%s\n' "$SIGS" > "$BASELINE"
  echo "baseline: written to $BASELINE ($(printf '%s' "$SIGS" | grep -c .) box signatures)"
else
  echo "-- Overfull/Underfull attribution vs baseline --"
  NEW=0; LEGACY=0
  while IFS= read -r sig || [ -n "$sig" ]; do
    [ -z "$sig" ] && continue
    if grep -Fxq -- "$sig" "$BASELINE"; then
      echo "LEGACY: $sig"
      LEGACY=$((LEGACY+1))
    else
      echo "NEW:    $sig"
      NEW=$((NEW+1))
    fi
  done <<EOF_SIGS
$SIGS
EOF_SIGS
  echo "attribution: $NEW new, $LEGACY legacy"
fi

if [ "$FINAL_STATUS" -ne 0 ]; then
  echo "RESULT: COMPILE FAILED (final pdflatex exit $FINAL_STATUS); numbers above describe the failed run"
  exit 1
fi
echo "== Done. Report the numbers above verbatim; never paraphrase counts. =="
