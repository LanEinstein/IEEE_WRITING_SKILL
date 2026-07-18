<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Review Rubric

One scoring scale for the whole panel. Scores are ordinal, not cardinal:
useful for ranking concerns, not for arithmetic. The decision comes from the
findings and the decision guidance below, never from averaging alone.

## Dimensions (score 1-5 each, with a confidence 1-5 per reviewer)

| Dim | Name | What 5 looks like | What 2 looks like |
|---|---|---|---|
| D1 | Novelty and positioning | A precise, defensible delta over the closest prior work, positioned against the current literature | Incremental tweak, or the delta is asserted but not argued |
| D2 | Technical soundness | Method is correct, assumptions stated, derivations check out | Gaps or errors in the core derivation or design logic |
| D3 | Statistical discipline | Primary metric pre-declared; every significance claim carries the stated test; intervals where claimed; honest tie handling | Loose "significant", cherry-picked cells, no variability reporting |
| D4 | Experimental completeness | Baselines fair and current, ablations isolate every claimed component, protocol stated once and exactly | Missing obvious baselines, bundled ablations, protocol ambiguity |
| D5 | Literature quality | Top-venue, verified, current references; no unnecessary arXiv; no fabricated or unverifiable entries | Stale, thin, or unverifiable bibliography |
| D6 | Presentation | House prose canon holds (topic sentences, zero banned constructions, symbol continuity, table lead-ins) | Systematic violations that impede reading |
| D7 | Claims-evidence match | Every claim in abstract/intro/conclusion is exactly as strong as the evidence, with consistent quantifiers across sections | Overclaim, underclaim, or quantifier drift between sections |

## Severity levels for findings
- **CRITICAL**: invalidates a core claim or would cause rejection on its own
  (see da-protocol taxonomy). Must cite evidence (quote + location).
- **MAJOR**: requires substantive revision (new experiment, rewritten
  argument, restructured section).
- **MINOR**: local fix (sentence, caption, reference, formatting).

## Decision guidance (calibrated to the Stage-0 target venue; journal decisions below, conference analogue: Accept / Weak Accept / Borderline / Reject)
- **Accept (rare at first submission)**: no CRITICAL, no MAJOR, D-scores all >= 4.
- **Minor Revision**: no CRITICAL; MAJOR findings are all fixable without new
  experiments.
- **Major Revision**: any fixable CRITICAL, or MAJOR findings needing new
  experiments.
- **Reject**: an unfixable CRITICAL (broken core claim, unsalvageable
  novelty), or the DA's counter-narrative survives synthesis unrebutted.

## Rubric-level hard checks (any reviewer may file; R-METH owns)
1. Significance language outside the pre-declared primary metric: automatic
   finding, severity >= MAJOR (S-EXP-7).
2. Purity self-labels ("leakage-free" etc.): automatic MINOR finding with
   the D5 mechanism-statement fix suggested.
3. Abstract word count outside the target venue's gate (journal: 150-250
   from the house audit; conference: the profile's typical range is
   advisory, hard caps only where the venue states one): automatic MAJOR
   for a journal target (desk-level formatting risk).
4. Page count over the target venue's cap (mechanics tables in
   `core/literature/venue-style-profiles.md`): automatic CRITICAL until
   fixed; conference over-length is rejected without review.
5. Unverifiable references (from the citation report): MAJOR, listed
   entry by entry.
6. Quantifier drift between abstract/intro/conclusion and the tables:
   MAJOR (D7).

## Scoring integrity rules
- Write the score BEFORE writing the justification, per dimension, then
  justify; never reverse-engineer scores from a target decision.
- Evidence-first: every finding quotes the manuscript (or the audit output)
  and gives a location. A finding with no citable evidence is an opinion and
  goes to a separate "advisory" list, not the findings list.
- Surface-form parity: do not reward technical-sounding vagueness or
  penalize plain wording; run the opposite-style counterfactual before
  scoring D6.
