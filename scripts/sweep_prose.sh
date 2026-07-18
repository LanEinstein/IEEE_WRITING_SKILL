#!/usr/bin/env bash
# (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite.
# Zero-tolerance prose sweep for a .tex manuscript. Counts and locates
# violations of the sweepable global rules (see core/rules/prose-rules.md).
# Counts are OCCURRENCES (grep -o), not matching lines. A grep error marks
# the run INVALID instead of printing a false zero.
# Single-token rules run line-by-line (exact line numbers). Multiword rules
# run on a paragraph-unwrapped stream (source wrapping cannot hide a
# phrase); their locations are the source line where the paragraph starts.
# Usage: sweep_prose.sh <file.tex>
set -u

if [ $# -lt 1 ] || [ ! -f "$1" ]; then
  echo "ERROR: usage: sweep_prose.sh <file.tex>" >&2
  exit 2
fi

SRC="$1"
TMP=$(mktemp)
TMPPARA=$(mktemp)
trap 'rm -f "$TMP" "$TMPPARA"' EXIT
ERRORS=0

# Strip LaTeX comments: a % is a comment unless preceded by an odd run of
# backslashes (perl handles the even-backslash case sed cannot).
perl -pe 's/((?:^|[^\\])(?:\\\\)*)%.*/$1/' "$SRC" > "$TMP"

# Paragraph-unwrapped stream: each paragraph becomes one line prefixed with
# the source line number where the paragraph starts ("N| text").
awk '
  function flush() { if (buf != "") { print start "| " buf; buf = "" } }
  /^[ \t]*$/ { flush(); next }
  { line = $0; sub(/^[ \t]+/, "", line)
    if (buf == "") { start = NR; buf = line } else { buf = buf " " line } }
  END { flush() }
' "$TMP" > "$TMPPARA"

# report <label> <pattern> <grep-flags> <file>
report() {
  local label="$1" pattern="$2" flags="$3" file="$4"
  local out status count
  out=$(grep $flags -o -- "$pattern" "$file")
  status=$?
  if [ "$status" -gt 1 ]; then
    echo "[$label] SCAN ERROR (grep exit $status)"
    ERRORS=1
    return
  fi
  count=$(printf '%s' "$out" | grep -c .)
  echo "[$label] count: $count"
  if [ "$count" -gt 0 ]; then
    if [ "$file" = "$TMPPARA" ]; then
      # Show the matched phrase plus the starting line of its paragraph.
      grep $flags -- "$pattern" "$file" | head -10 | cut -c1-160 | sed 's/^/    para@/'
    else
      printf '%s\n' "$out" | head -20 | sed 's/^/    /'
    fi
  fi
}

echo "== Prose sweep: $SRC =="

# Line-based single-token rules (exact line numbers).
report "G1 banned-pronouns (this/these/it/its/they/their/them; self-reference 'this paper/work' exempt on human review)" \
  '\b(this|these|it|its|they|their|them)\b' '-inE' "$TMP"
report "G10 semicolons" ';' '-n' "$TMP"
report "G11 em-dashes" '---|\x{2014}' '-nP' "$TMP"
report "CHECK significance-language (manual: primary metric + stated test only)" \
  '\bsignificant(ly)?\b' '-inE' "$TMP"
report "L5 CITE-placeholders" 'CITE:' '-n' "$TMP"

# Paragraph-based multiword rules (immune to source-line wrapping).
report "G2 connective-without-comma" \
  '(^[0-9]+\| |\.\s+)(However|Therefore|Moreover|Furthermore|Finally|In addition)(?!,)' '-nP' "$TMPPARA"
report "G9 repeated-lead-clauses (how X and how Y / that A and that B)" \
  '\b(how|that|whether)\b[^.!?;]*\band \1\b' '-inP' "$TMPPARA"
report "BANNED puffery/purity" \
  'fully proves|fully demonstrates|excellent|strong overall|leakage-free|leakage free|no-leak|leak-free|bias-free|Pareto-dominan' '-inE' "$TMPPARA"
report "G14 and-dense-paragraphs (3+ ' and ' in one paragraph; judgment call)" \
  '( and .* and .* and )' '-nE' "$TMPPARA"

if [ "$ERRORS" -ne 0 ]; then
  echo "== SWEEP INVALID: at least one scan errored; fix before trusting any count. =="
  exit 2
fi
echo "== Sweep complete. Zero-tolerance rules: G1 G2 G9 G10 G11 BANNED L5. =="
echo "== Confirm flagged edge cases by reading context; then report counts verbatim. =="
