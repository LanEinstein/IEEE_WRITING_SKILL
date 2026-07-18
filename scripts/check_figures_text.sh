#!/usr/bin/env bash
# (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite.
# Extract the embedded text of every figure PDF, so a term rename in prose
# can be checked against figure content BEFORE editing (V2).
# Zero PDFs found or a failed extraction yields INCONCLUSIVE, never "safe".
# Usage:
#   check_figures_text.sh <figure-dir>          # preview text of every PDF
#   check_figures_text.sh <figure-dir> <term>   # fixed-string search per PDF
set -u

if [ $# -lt 1 ] || [ ! -d "$1" ]; then
  echo "ERROR: usage: check_figures_text.sh <figure-dir> [term]" >&2
  exit 2
fi
command -v pdftotext >/dev/null 2>&1 || { echo "ERROR: pdftotext not found" >&2; exit 2; }

DIR="$1"
TERM="${2:-}"
FOUND_ANY=0
PDF_COUNT=0
EXTRACT_FAIL=0

while IFS= read -r pdf; do
  PDF_COUNT=$((PDF_COUNT+1))
  if ! TEXT=$(pdftotext "$pdf" - 2>/dev/null); then
    echo "[$(basename "$pdf")] EXTRACTION FAILED"
    EXTRACT_FAIL=1
    continue
  fi
  if [ -n "$TERM" ]; then
    HITS=$(printf '%s\n' "$TEXT" | grep -inF -- "$TERM")
    COUNT=$(printf '%s' "$HITS" | grep -c .)
    echo "[$(basename "$pdf")] matching lines for '$TERM': $COUNT"
    [ "$COUNT" -gt 0 ] && { printf '%s\n' "$HITS" | head -10 | sed 's/^/    /'; FOUND_ANY=1; }
  else
    echo "===== $(basename "$pdf") (first 40 nonblank lines, preview) ====="
    printf '%s\n' "$TEXT" | grep -vE '^\s*$' | head -40
  fi
done < <(find "$DIR" -maxdepth 1 -type f -iname '*.pdf' | sort)

if [ "$PDF_COUNT" -eq 0 ]; then
  echo "RESULT: INCONCLUSIVE (no PDF files found in $DIR)"
  exit 2
fi
if [ "$EXTRACT_FAIL" -ne 0 ]; then
  echo "RESULT: INCONCLUSIVE (at least one PDF failed text extraction; check manually)"
  exit 2
fi
if [ -n "$TERM" ]; then
  if [ "$FOUND_ANY" -eq 1 ]; then
    echo "RESULT: term appears inside figures; renaming the term in prose alone would ship a text-figure mismatch."
  else
    echo "RESULT: term not found in any of the $PDF_COUNT figure PDFs; prose rename is figure-safe."
  fi
fi
