#!/usr/bin/env bash
# (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite.
# Zero-tolerance prose sweep for a .tex manuscript. Counts and locates
# violations of the sweepable global rules (see core/rules/prose-rules.md).
# Output = per-rule count + up to 20 locations. A human confirms edge cases;
# "zero" claims must cite this script's output (V5).
# Usage: sweep_prose.sh <file.tex>
set -u

if [ $# -lt 1 ] || [ ! -f "$1" ]; then
  echo "ERROR: usage: sweep_prose.sh <file.tex>" >&2
  exit 2
fi

SRC="$1"
TMP=$(mktemp)
trap 'rm -f "$TMP"' EXIT

# Strip LaTeX comment tails (keep escaped \%), preserve line numbers.
sed -E 's/(^|[^\\])%.*/\1/' "$SRC" > "$TMP"

report() {
  local label="$1" pattern="$2" flags="${3:--nE}"
  local hits count
  hits=$(grep $flags "$pattern" "$TMP" || true)
  count=$(printf '%s' "$hits" | grep -c . || true)
  echo "[$label] count: $count"
  if [ "$count" -gt 0 ]; then
    printf '%s\n' "$hits" | head -20 | sed 's/^/    /'
  fi
}

echo "== Prose sweep: $SRC =="

# G1 banned pronouns (word-boundary, case-insensitive)
report "G1 banned-pronouns (this/these/it/its/they/their/them)" \
  '\b(this|these|it|its|they|their|them)\b' '-inE'

# G2 sentence-initial connective missing its comma
report "G2 connective-without-comma" \
  '(^|\. )(However|Therefore|Moreover|Furthermore|Finally|In addition)( [a-z])' '-nE'

# G9 repeated lead words after one verb
report "G9 repeated-lead-clauses (how X and how Y / that A and that B)" \
  '\b(how|that|whether)\b[^.;]{0,80}\band (how|that|whether)\b' '-inE'

# G10 semicolons (manual confirm: list-type vs clause-joining)
report "G10 semicolons" ';' '-n'

# G11 em-dashes
report "G11 em-dashes" -- '---|\xe2\x80\x94' '-nP'

# S-EXP-8 / D5 banned words and purity labels
report "BANNED puffery/purity (fully proves|fully demonstrates|excellent|strong overall|leakage-free|no-leak|leak-free|bias-free|Pareto-dominan)" \
  'fully proves|fully demonstrates|excellent|strong overall|leakage-free|leakage free|no-leak|leak-free|bias-free|Pareto-dominan' '-inE'

# S-EXP-7 significance language (manual check against primary metric + test)
report "CHECK significance-language (manual: primary metric + stated test only)" \
  '\bsignificant(ly)?\b' '-inE'

# L5 unresolved citation placeholders
report "L5 CITE-placeholders" 'CITE:' '-n'

# G14 and-density: lines with 3+ " and "
report "G14 and-dense-lines (3+ ' and ' on one line; judgment call)" \
  '( and .* and .* and )' '-nE'

echo "== Sweep complete. Zero-tolerance rules: G1 G2 G9 G10 G11 BANNED L5. =="
echo "== Confirm flagged edge cases by reading context; then report counts verbatim. =="
