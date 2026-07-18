<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Section Rules: Experiments (S-EXP)

Apply on top of `prose-rules.md` and `disclosure-policy.md`. Drafted right
after the method section in the ieee-write order. The experiments section is
about numbers, and the numbers must read as one connected argument, not as
isolated reports stapled together.

## S-EXP-1. Every number has a stated origin and relation
Each number quoted in prose must be traceable in the same sentence or the
previous one: which table, which column or cell, and what relation the number
has to the preceding sentence (continuation, contrast, or the other face of
the same quantity). No number appears from nowhere.

## S-EXP-2. Table lead-in sentences
Before citing numbers from a table for the first time, introduce the table in
natural language: "Table N reports the paired difference between ..." Both
exemplar families are acceptable: "Table N reports/shows/presents ..." and
"As shown in Table N, ...".

## S-EXP-3. Headline numbers only
Prose restates ONLY the headline cells: the strongest result, the tied cells,
and the resolution of any second-best cell. The full grid, and all confidence
intervals, speak through the table. Re-reciting every cell is a known defect
of weaker published papers, and the suite holds the higher bar.

## S-EXP-4. Number-then-interpretation pairing
Every quoted number or number group is followed by one sentence stating what
the number means ("The margin shows that ..."). Numbers never stand bare.
Use the claim-verb ladder deliberately: indicate < suggest < demonstrate <
confirm, matching verb strength to evidence strength.

## S-EXP-5. The respectively pattern
Multi-dataset numbers in one sentence use the parallel form: "reaches A, B,
and C on X, Y, and Z, respectively."

## S-EXP-6. Subsection transitions
Each subsection ends with one sentence that hands off to the next subsection
("With the protocol fixed, we first compare accuracy within each dataset.").
The purpose-clause opener is the standard connective between analyses: "To
further [verify/isolate/test] X, we [experiment Y]."

## S-EXP-7. Significance discipline (hard rule)
`significant` / `significantly` may ONLY be attached to the pre-declared
primary metric under the stated statistical test, exactly as defined once in
the protocol paragraph. Every other metric is described descriptively
("restores the minority-class recall from .48 to .71"), never with
significance language. Loose "significantly outperforms" without a test is a
defect of published exemplars: do not imitate. Before writing any
significance sentence, check the protocol paragraph wording and confirm the
claim's test actually exists.

## S-EXP-8. No puffery, no purity labels
- Banned evaluative phrases: "fully proves", "fully demonstrates",
  "excellent performance", "strong overall performance", and any equivalent
  self-praise. State the fact and let magnitudes speak.
- Never label the protocol with purity adjectives (see D5 in
  `disclosure-policy.md`): state the verifiable mechanism instead, once, in
  the protocol paragraph. Example mechanism sentence: "Each test fold is
  scored once and never enters training, model selection, or
  standardization."

## S-EXP-9. Ablation framing
Each ablation row answers three things in one or two sentences: what was
removed or replaced, how much the metric changed, and what the change shows
about the component. Frame deltas so that a positive value means the
component helps, and say so in the caption.

## S-EXP-10. Protocol is stated once
Datasets, folds, seeds, metrics, and the significance test are defined once
in the setup subsection. Later subsections never restate protocol details;
they reference the setup.

## S-EXP-11. Ties and second-best cells
Resolve ties positively and briefly: "statistically tied with [the strongest
baseline] at [parameter advantage]". Do not enumerate losing cells, do not
self-grade ("slightly worse"), and where an exception needs a mechanism
sentence, give exactly one hedged causal clause ("The gap on X may be
attributable to ...") and move on.

## S-EXP-12. Baseline reimplementation sentence
When baselines are re-run in-house, use the fixed formula, present tense,
once: "For a fair and controlled comparison, we reimplement all baseline
methods within a common codebase and evaluate them under the same training
and evaluation protocols as our method." State tuning fairness uniformly and
only once; repetitions get cut. (The "them" inside the fixed formula is a
sanctioned G1 exception, like "this paper": the sweep still counts the hit,
and a human confirms the hit is the formula.)

## S-EXP-13. Figures
Every experiments figure follows `figure-standards.md` (vector or >=300
dpi, no in-figure titles, scientific colorblind-safe palette, Times New
Roman, print-legible sizes, unoccluded standard legends, panel labels
centered below each subplot, real data only).

## S-EXP-14. Claim-verb ladder (both profiles)
Calibrate the verb to the evidence, ascending: observe/find (raw data) ->
indicate (several readings converge inside one exhibit) -> suggest (single
or cross-experiment extrapolation) -> hypothesize / "a possible explanation
is" (untested conjecture, labeled as such) -> confirm (ONLY a pre-stated
prediction or a post-control result) -> demonstrate/conclude (independent
lines converge). "supports" attaches to hypotheses, "confirms" to
predictions; "consistent with" is reserved for agreement with EXTERNAL
prior work. Strength adverbs (consistently, substantially, uniformly)
require full-table evidence; believe/expect appear only in forward-looking
sentences, never for measured results.

## S-EXP-15. Observation body for ablations and big tables
After a dense table, the sanctioned narration forms are:
- "From Table N, we observe: (i) ... (ii) ... (iii) ..." with each item a
  claim plus its cell numbers; or
- numbered bold observations: "Obs 1: <one-sentence claim>." followed by
  "Specifically, <numbers>" and one mechanism clause.
Both replace cell-by-cell recitation (S-EXP-3 still holds). A summary
device inside the table (a Wins/ties count row, or a Delta column vs the
strongest baseline, defined in the caption) turns "top-or-tied" claims into
checkable table content and is preferred over prose enumeration.

## S-EXP-16. Hypothesis-testing skeleton (analysis/diagnostic subsections)
When a subsection argues a mechanism rather than a ranking, use the
falsifiable-prediction loop: (1) state the prediction before the data,
should-form ("If X drives Y, removing X should ..."); (2) run the targeted
experiment with the control named in-sentence ("while keeping the outputs
fixed"); (3) close with the graded verb (S-EXP-14). Where feasible add one
reverse manipulation (induce or remove the cause on purpose) and one
named competing explanation actively excluded ("The gain is not explained
by ..., because ..."). A harmlessness check (the fix does not hurt the
primary metric) gets its own labeled unit when a fix is proposed.

## S-EXP-17. Error-bar and uncertainty declaration
Declare the uncertainty convention ONCE, centrally (protocol paragraph or
first caption): estimator, interval type, and run count ("shaded regions:
one std over 5 seeds"; "intervals: 95% percentile bootstrap"). Later
exhibits reference, never redefine. Where runs are deterministic, omit
error bars rather than fabricate them, without comment. Robustness-knob
statements ("varying k to 1/2 or 1/4 does not change the claims") back any
threshold the analysis depends on.

## S-EXP-18. Scope inside the claim
Qualifiers live inside the claim's noun phrase, not in a separate apology:
"current X", "on the largest benchmark", "for the three corpora we study".
A conservative-direction disclosure ("we did not tune the baseline's beta,
so these results may understate the baseline") is used only when the
conclusion still favors us under the disclosed conservatism (D1 discipline
otherwise applies).
