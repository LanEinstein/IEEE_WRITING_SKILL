<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Section Rules: Abstract (S-ABS)

Apply on top of the global rules in `prose-rules.md`. The abstract is drafted
LAST (after the conclusion) in the ieee-write order.

## S-ABS-1. The limitation-then-solution skeleton (mandatory)
Write the abstract sentence-by-sentence on the following skeleton, in order:

1. **One value sentence.** Why the task matters. Background stops here.
   - "X reveals Y, so X recognition supports Z and W."
2. **The turn.** "However, existing methods have two limitations."
3. **Limitation one, limitation two.** `First, ... Second, ...` and each
   limitation MUST state a consequence. A fact without a consequence is not a
   limitation. Fold "why the task is hard" into limitation one as the cause,
   so cause and consequence form one chain without spending extra sentences.
4. **(Optional) diagnostic step.** If a diagnostic or analysis motivates the
   design, place one sentence for the diagnostic between the limitations and
   the proposal, phrased as the answer to limitation one, and keep only the
   single strongest number. A diagnostic must never occupy half the abstract.
5. **The proposal.** "We therefore propose X (ACRONYM), a ..." or
   "In this paper, we propose ...".
6. **Design mapping.** "To resolve the first limitation, ..." and
   "To address the second limitation, ..." with exactly one design element per
   limitation. If a solution is a component of the model, make the ownership
   explicit so the sentence does not read as an external, standalone method.
7. **Experiments close.** "Experiments on [benchmarks] show that ..." with the
   headline results. Numbers in the abstract are optional in the exemplar
   corpus, but a named-benchmark list is near universal.

## S-ABS-2. Length: 150-250 words, measured [SCRIPT]
The IEEE SPS rule is 150-250 words (`core/templates/ieee-facts.md`). Target
230-250. Measure EVERY version with `scripts/wordcount_abstract.sh` and report
only the measured count. Never estimate: repeated real-world drafts each
"felt" under 250 and measured 260-400. Published exemplars measure 204-260
words.

## S-ABS-3. Self-contained
No citations, no displayed equations, no footnotes. The no-abbreviation rule
is applied loosely in practice: dataset and method acronyms are acceptable
(published exemplars use them), and `%` is a symbol, not an abbreviation
(write `91\%`, not `91 percent`).

## S-ABS-4. Global limits awareness
At initial submission the whole manuscript must fit the page cap of the target
journal (13 double-column pages for the reference journal; see
`core/templates/ieee-facts.md`). Check pages with `scripts/verify_tex.sh`
whenever abstract edits are compiled.

## S-ABS-5. Every global rule applies with full force
The abstract is the most-read paragraph: banned pronouns, positive phrasing,
causal chains, single-value truth, and the em-dash ban (G1-G15) are checked
sentence by sentence, and the disclosure rules (`disclosure-policy.md`) apply
unchanged (no self-labels, no proactive weakness).
