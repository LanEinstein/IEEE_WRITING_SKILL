<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Section Rules: Conclusion (S-CON)

Apply on top of `prose-rules.md` and `disclosure-policy.md`. Drafted LAST
together with the abstract in the ieee-write order.

## S-CON-1. The four-step skeleton
1. **One-sentence summary**: "[MODEL] is a [category] that [core idea]." or
   "In this paper, we proposed [MODEL], ...".
2. **Component recap**: restate the architecture in one or two sentences,
   folding causality in with `so` rather than listing parts ("A fixed stem
   exposes the field as interpretable channels, so the anchor keeps a linear
   floor while a small encoder learns only the residual").
3. **Main findings and meaning**: the headline results and what they
   establish, stated directly. Do NOT tag findings with labels like "the
   main finding is"; assert the content.
4. **Future work close**: one or two sentences, concrete and modest
   ("Because the front end is task-agnostic, the same design may suit [an
   adjacent problem]. We leave that extension to future work, along with
   [one further direction].").

## S-CON-2. Compactness
A single tight paragraph is acceptable and often preferable. No new numbers
that did not appear in the experiments section, no new claims, no citations
unless indispensable.

## S-CON-3. Consistency duties
Result phrasing must match the experiments section exactly in strength:
if the experiments say "a significant win on [one benchmark]", the conclusion
may not generalize to "significant wins". Quantifier drift between sections
is a review-killing defect.

## S-CON-4. Disclosure rules apply
No weakness list, no hedging block. Scope statements, if any, are one plain
sentence of standard reproducibility or scope, per `disclosure-policy.md`.

## S-CON-5. Venue-conditional close [PROFILE]
- **Journal profile**: S-CON-1..4 as written.
- **Conference profile**: a merged "Conclusion and limitations" heading is
  acceptable; the limitation named is outside the main claim's evaluation
  envelope, framed as the flip-side of a strength, and paired with a
  forward path (gap positivization: "While there is still a gap with ...,
  we believe future work can bridge this using [OURS] as a backbone").
  House D1-D6 still bind: no protocol self-doubt, no weakness inventory,
  no hedging of the headline claim.
