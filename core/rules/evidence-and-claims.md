<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Evidence, protocol, and claims

## EVID1. Trace the claim to the relevant version

Record content, source location (table/label/log/run/primary document), associated method/configuration/version, statistical unit, status, and scope. Use these states: `verified`, `author-confirmed/run-untraced`, `pending`, `conflict`, `superseded`. A clarified reporting convention is not a reproduced historical run.

Locked manuscript tables are the numeric reference during writing. If a linked result record disagrees, preserve the current values, list the discrepancy and affected claims, and seek a focused resolution. Do not choose a favorable number, silently change results, or treat the latest code as historical truth. Source priority comes from the current project's explicit provenance agreement and relevance to the actual result, not file modification time alone.

## EVID2. Reconstruct the full evaluation object

Check dataset/version/sample scope, label mapping/exclusions, split unit, pretraining overlap, fitted preprocessing statistics, inner model/epoch/config selection, untouched outer evaluation, and final predictor. Distinguish pooling predictions from averaging fold metrics; probability averaging from logit averaging or voting; seed repetitions from subject uncertainty.

A student-only member can still be part of a multi-model ensemble. A batch-by-batch operator can make predictions depend on other batch members. Report actual inference, member count, test-time processing, and relevant batch conditions. Do not infer them from the phrase “student-only.”

## EVID3. Separate three kinds of statements

- **Evidence:** measured comparison or documented fact, with its actual controls and scope.
- **Operational interpretation:** what the verified operation mathematically or physically changes, connected to the observation without claiming an unmeasured mediator.
- **Limitation:** what the evidence does not establish, including counterexamples that alter the claim.

For example, freezing keeps the teacher parameter mapping fixed if normalization state also stays fixed. A performance gain alone does not measure catastrophic forgetting or optimization stability. Distribution-moment agreement does not establish high-order or class-conditional equality. Heatmaps alone do not establish causation or anatomical action-unit ground truth.

## EVID4. Numeric and statistical scope

Attach metric, scale, comparator, protocol, aggregation, uncertainty estimator, and direction wherever needed to make a number true. Calculate derived values with a tool, observe the output, then write. Absolute differences on a 0–1 score, percentage-point changes, and relative percentages are distinct.

Mean±SD requires the repetition unit, run count, aggregation order, and sample/population estimator. Do not invent a confidence interval, statistical test, or missing per-run values. Non-significance and an interval including zero do not establish equivalence or a statistical tie. Descriptive rank counts and significance counts are different. An average advantage across a family does not imply every member wins.

## EVID5. Keep counterevidence visible

Update abstract/introduction/conclusion quantifiers if one protocol loses or an added baseline changes rank. Do not hide a harmful stage placement, crossed ranking, material cost, or protocol difference behind “overall effectiveness.” Give the boundary once at the appropriate location without repetitive defense. Do not extrapolate to untested datasets, modalities, applications, or universal optimality.

## EVID6. Missing evidence narrows delivery, not truth

Mark the dependent draft sentence `[EVIDENCE: precise missing item]` or use accurately scoped wording. Continue independent content. An idea can support a proposed question and outline, not a completed-result abstract. Writing-only tasks identify missing evidence; concrete research design and new runs require an expanded assignment. Never fabricate facts to complete a blueprint.
