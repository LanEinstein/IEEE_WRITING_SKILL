#!/usr/bin/env bash
# (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite.
# Compile a manuscript (pdflatex x3 with bibtex) and report:
#   pages / warning count / undefined references / Overfull boxes with
#   NEW-vs-LEGACY attribution against a stored baseline.
# Usage:
#   verify_tex.sh <main.tex> [--set-baseline]
# The baseline (.ieee_baseline.txt next to the tex file) is created on first
# run automatically; --set-baseline overwrites it with the current state.
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

LOG="$BASE.log"
if [ ! -f "$LOG" ]; then
  echo "ERROR: no log file produced" >&2
  exit 1
fi

PAGES=$(grep -oE 'Output written on .*\(([0-9]+) page' "$LOG" | grep -oE '[0-9]+ page' | grep -oE '[0-9]+' | tail -1)
WARNINGS=$(grep -c 'Warning' "$LOG" || true)
UNDEFINED=$(grep -c 'undefined' "$LOG" || true)
OVERFULL_LINES=$(grep -E '^(Overfull|Underfull) \\[hv]box' "$LOG" || true)
OVERFULL_COUNT=$(printf '%s' "$OVERFULL_LINES" | grep -c . || true)

echo "pages: ${PAGES:-UNKNOWN}"
echo "warnings: $WARNINGS"
echo "undefined-mentions: $UNDEFINED"
echo "over/underfull-boxes: $OVERFULL_COUNT"

# Signatures: "at lines N--M" plus badness/size, for baseline comparison.
SIGS=$(printf '%s\n' "$OVERFULL_LINES" | sed -E 's/.*\(([^)]*)\).* at lines ([0-9-]+).*/\2|\1/;t;s/.*/misc/' | sort -u | grep -v '^$' || true)

if [ ! -f "$BASELINE" ] || [ "$SETBASE" = "--set-baseline" ]; then
  printf '%s\n' "$SIGS" > "$BASELINE"
  echo "baseline: written to $BASELINE ($(printf '%s' "$SIGS" | grep -c . || true) box signatures)"
else
  echo "-- Overfull/Underfull attribution vs baseline --"
  NEW=0; LEGACY=0
  while IFS= read -r sig; do
    [ -z "$sig" ] && continue
    if grep -qF "$sig" "$BASELINE"; then
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

echo "== Done. Report the numbers above verbatim; never paraphrase counts. =="
