<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Verification Protocol (V1-V6)

Every compliance claim in the suite comes from tool output. Impressions do
not count. These rules bind all three workflows.

## V1. Word counts are measured, never estimated
Report abstract and section word counts only from
`scripts/wordcount_abstract.sh` (or `wc -w` on an extracted region). Derived
numbers (ratios, percentages) are computed with a tool (python), never
mentally. Real-world calibration: successive drafts "felt" under the limit
and measured 405, 310, 274, and 261 words; only the measured number is real.

## V2. Check figure text before renaming terms
Before renaming any term in prose, extract the text of every figure with
`scripts/check_figures_text.sh` and grep for the old term. A term change that
leaves stale text inside a figure ships an inconsistency the compiler will
never flag.

## V3. Compilation report with old-versus-new attribution
After each editing session (and at every section boundary in drafting):
1. Run `scripts/verify_tex.sh <main.tex>`: pdflatex, bibtex, pdflatex,
   pdflatex, non-interactive.
2. Report: page count, warning count, undefined-reference count, and every
   Overfull/Underfull box with line numbers.
3. Attribute each Overfull to NEW (introduced by the session) or LEGACY
   (present in the baseline). The script stores a baseline on first run; a
   legacy artifact must never be reported as a new regression, and a new one
   must never hide behind the legacy list.

## V4. The numbers iron rule
The turn (or step) that launches a number-producing command does not also
write those numbers into the manuscript, a table, or a report. Observe the
real stdout first, then write, in a later step. Purpose: makes fabricated or
pre-committed numbers structurally impossible.

## V5. Zero is a sweep result
Any "zero violations" claim (pronouns, semicolons, em-dashes, banned words,
CITE placeholders) must come from `scripts/sweep_prose.sh` counts on the
final text, run AFTER the last edit. A sweep lists count plus location per
rule; a human confirms flagged edge cases. Never declare zero from memory.

## V6. Page-limit gate
Check the compiled page count against the target journal's limits from
`core/templates/ieee-facts.md` (reference journal: 13 double-column pages at
initial submission, 16 at revision) at every compilation. A page-limit breach
blocks submission readiness regardless of content quality.
