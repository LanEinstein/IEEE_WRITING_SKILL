<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Review Report Format

One report per review run, written to `paper/REVIEW_<date>.md` in the user's
project. The report has two strictly separated layers. Layer A simulates what
external reviewers would say; Layer B is the house compliance audit that only
the author sees. Never mix the layers: Layer B vocabulary (disclosure
strategy, internal rules) must not leak into Layer A, and nothing in Layer B
is ever quoted in a response letter.

## Layer A: Simulated external review

### A1. Per-reviewer reports (R-EIC, R-METH, R-DOM, R-LANG, R-DA)
For each reviewer:
- Committed scoring plan (from the paper-blind phase) and any plan dissent.
- Dimension scores (1-5) with confidence, score written before
  justification.
- Findings list, most severe first. Each finding:
  - `[SEVERITY][DIMENSION] one-sentence defect statement`
  - Evidence: verbatim quote + location (section/paragraph or line).
  - Actionable fix: the concrete change that would resolve the finding.
- R-DA additionally: the Strongest Counter-Narrative section.

### A2. Editorial synthesis
- Cross-reviewer matrix: finding clusters, who found what, agreements and
  conflicts. Resolve conflicts by evidence, never by seniority of persona.
- Blind-spot pass: for each persona's declared blind spot, state what was
  checked to compensate.
- Deduplicated master finding list, severity-ranked.
- **Decision estimate**: Accept / Minor / Major / Reject per the rubric's
  decision guidance, with the two or three findings that drive the decision.

## Layer B: House compliance audit (author-only)
- Script outputs, verbatim counts (never impressions):
  - `sweep_prose.sh`: per-rule counts and locations (G1/G2/G9/G10/G11,
    banned-word hits, and-density, CITE placeholders).
  - `wordcount_abstract.sh`: measured abstract length vs the 150-250 gate.
  - `verify_tex.sh`: pages vs venue cap, warnings, undefined references,
    Overfull boxes with NEW/LEGACY attribution.
  - `verify_citations.py`: per-entry verification, venue-tier violations,
    arXiv-only list.
- Disclosure audit (D1-D6): every passage that volunteers a weakness,
  hedges conspicuously, uses purity self-labels, or leaks internal-verdict
  vocabulary, each with a suggested D-compliant rewrite.
- Consistency audit: quantifier drift across abstract/intro/conclusion vs
  tables (D7 evidence).

## Re-review mode (after a revision round)
Input: the prior report plus the revised manuscript (and the response letter
if one exists). Output adds:
- **Traceability matrix**: one row per prior finding with status
  `FULLY_ADDRESSED / PARTIALLY_ADDRESSED / NOT_ADDRESSED / MADE_WORSE`,
  each status justified by a quote from the revised text (independently
  verified; author claims of "fixed" are checked, not trusted).
- New findings introduced by the revision, same format as A1.
- Updated decision estimate.

## Output discipline
- Reviewers are read-only; the report contains proposals, never applied
  edits. Users take findings to ieee-polish for gated application.
- Every number in the report comes from observed tool output (V4).
- If any script could not run, say so explicitly; never fill in an expected
  result.
