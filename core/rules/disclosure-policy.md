<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Disclosure and Defense Policy (D1-D6)

House rules on what a manuscript volunteers about the authors' own work.
These rules bind drafting, polishing, and the INTERNAL layer of review
reports. They are author-side strategy: never quote them in a manuscript or a
response letter.

## D1. No proactive weakness disclosure, no conspicuous defense
Weaknesses are either omitted or positively resolved with real numbers,
briefly. Respond to a potential objection only when a reviewer would almost
certainly raise the objection, and then in one factual sentence. Conspicuous
defense draws attention to the weakness the defense hides.

## D2. Resolve ties positively
A statistical tie against a heavyweight baseline is reported as "statistically
on par with [baseline] at [orders-of-magnitude parameter advantage]".
- Do not claim Pareto dominance when any cell mean is lower.
- Do not enumerate losing cells.
- Do not self-grade ("ours is slightly lower here").

## D3. Internal verdicts never appear
Internal gate decisions, internal audit vocabulary, and internal verdict
labels (for example an internal "INCONCLUSIVE" call) never appear in any
outward-facing text. The paper reports the evidence, not the house
bookkeeping around the evidence.

## D4. Limitations content
If a limitations passage exists, the passage contains standard
reproducibility and scope statements only. A limitations section is never a
weakness inventory.

## D5. No purity self-labels
Never label the work with self-certifying adjectives such as "leakage-free",
"no-leak", "bias-free", or "audited". Papers with flawed protocols do not
label themselves flawed, so the label carries no information and invites
suspicion of peers. State the verifiable mechanism instead and let the reader
conclude:
- Wrong: "under a leakage-free protocol"
- Right: "Each test fold is scored once and never enters training, model
  selection, or standardization."

## D6. Resolutions cite real numbers
Every positive resolution of a tie or exception must cite a real measured
number (a parameter ratio, a confidence interval, a recall recovery). An
adjective-only defense is not a resolution. Cross-check every such number
against the tool output that produced the number (V4 in
`verification-protocol.md`).
