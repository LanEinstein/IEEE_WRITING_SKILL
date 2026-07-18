#!/usr/bin/env bash
# (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite.
# Zero-tolerance prose sweep for a .tex manuscript. Counts and locates
# violations of the sweepable global rules (see core/rules/prose-rules.md).
# Counts are OCCURRENCES (grep -o), not matching lines. A grep error marks
# the run INVALID instead of printing a false zero. Known limit: matching is
# line-based, so a multiword phrase wrapped across source lines can be
# missed; keep one sentence per source line where practical.
# Usage: sweep_prose.sh <file.tex>
set -u

if [ $# -lt 1 ] || [ ! -f "$1" ]; then
  echo "ERROR: usage: sweep_prose.sh <file.tex>" >&2
  exit 2
fi

SRC="$1"
TMP=$(mktemp)
trap 'rm -f "$TMP"' EXIT
ERRORS=0

# Strip LaTeX comments: a % is a comment unless preceded by an odd run of
# backslashes (perl handles the even-backslash case sed cannot).
perl -pe 's/((?:^|[^\\])(?:\\\\)*)%.*/$1/' "$SRC" > "$TMP"

report() {
  local label="$1" pattern="$2" flags="${3:--nE}"
  local out status count
  out=$(grep $flags -o -- "$pattern" "$TMP")
  status=$?
  if [ "$status" -gt 1 ]; then
    echo "[$label] SCAN ERROR (grep exit $status)"
    ERRORS=1
    return
  fi
  count=$(printf '%s' "$out" | grep -c .)
  echo "[$label] count: $count"
  if [ "$count" -gt 0 ]; then
    printf '%s\n' "$out" | head -20 | sed 's/^/    /'
  fi
}

echo "== Prose sweep: $SRC =="

# G1 banned pronouns (word-boundary, case-insensitive; occurrences)
report "G1 banned-pronouns (this/these/it/its/they/their/them; self-reference 'this paper/work' exempt on human review)" \
  '\b(this|these|it|its|they|their|them)\b' '-inE'

# G2 sentence-initial connective missing its comma
report "G2 connective-without-comma" \
  '(^|\.\s+)(However|Therefore|Moreover|Furthermore|Finally|In addition)(?!,)' '-nP'

# G9 repeated lead word after one verb (same lead word, back-referenced)
report "G9 repeated-lead-clauses (how X and how Y / that A and that B)" \
  '\b(how|that|whether)\b[^.!?;]*\band \1\b' '-inP'

# G10 semicolons (manual confirm: math/list vs clause-joining)
report "G10 semicolons" ';' '-n'

# G11 em-dashes (--- or the Unicode em dash)
report "G11 em-dashes" '---|\x{2014}' '-nP'

# S-EXP-8 / D5 banned words and purity labels
report "BANNED puffery/purity" \
  'fully proves|fully demonstrates|excellent|strong overall|leakage-free|leakage free|no-leak|leak-free|bias-free|Pareto-dominan' '-inE'

# S-EXP-7 significance language (manual check against primary metric + test)
report "CHECK significance-language (manual: primary metric + stated test only)" \
  '\bsignificant(ly)?\b' '-inE'

# L5 unresolved citation placeholders
report "L5 CITE-placeholders" 'CITE:' '-n'

# G14 and-density: lines with 3+ " and "
report "G14 and-dense-lines (3+ ' and ' on one line; judgment call)" \
  '( and .* and .* and )' '-nE'

if [ "$ERRORS" -ne 0 ]; then
  echo "== SWEEP INVALID: at least one scan errored; fix before trusting any count. =="
  exit 2
fi
echo "== Sweep complete. Zero-tolerance rules: G1 G2 G9 G10 G11 BANNED L5. =="
echo "== Confirm flagged edge cases by reading context; then report counts verbatim. =="
