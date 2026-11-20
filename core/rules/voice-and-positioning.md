<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Voice: sell the work, state it positively

These rules govern how a sentence positions the paper. They do not license unsupported claims; [evidence-and-claims.md](evidence-and-claims.md) still decides what is true.

## VP1. The paper promotes its own work

Say what this work achieves that earlier work did not. Do not hedge a supported claim, pre-empt an objection nobody raised, or shrink the claim below the evidence. Reviewers read a defensive draft as weak and as machine-written.

The failure modes to remove:

- a paragraph that opens by denying a doubt the previous text never created ("The main result cannot be explained by dataset shortcuts" with no preceding suspicion);
- a sentence that lists limitations the reader could not have suspected;
- a qualifying clause attached to every claim;
- an ending that lands on a competing method being best.

## VP2. Unfavourable results get an honest, favourable reading

State the result, give the interpretation the evidence supports, and end on what the work establishes. Never end a paragraph whose subject is this work on a competitor's advantage.

- Write "this model ranks in the top two of both tasks, which no other method achieves", not "it ranks second".
- When a criterion is not met, report the positive outcome the evidence does support and put the formal criterion where the review trail expects it (typically the supplement). Do not volunteer shortfalls in the main text.
- Keep the numbers exact. An honest favourable reading changes emphasis, not values.

## VP3. State the difference directly

Do not expect the reader to infer a contrast. "Who can see from this that the problem setting differs?" is a rejection reason. Name the difference in the same sentence:

- weak: two related protocols are listed side by side and left for the reader to compare;
- strong: state what the other setting does, then what this work does differently, then why the difference matters.

Related work that is not a competitor must not be written as one. If two works address different tasks, say so in the sentence that mentions both.

## VP4. Criticise procedures, not people

Protocol-level analysis is allowed and encouraged. Named-method failure accusations, per-paper reproduction-gap tables, "selection artifact" phrasing, and attributions of motive are not. Show protocol sensitivity through this work's own re-implementations, and cite published evaluation studies for the general claim.

Raised-tone criticism triggers rejection; a calm statement of what a protocol leaves unconstrained does not.

## VP5. One subject per sentence

Do not coordinate two different objects under one predicate. "The evidence depends on the training input, and the gain of a module depends on the architecture" reads as one sentence making one claim and is false as written. Split it, or make the shared subject real.

Never let a clause comment on a referent the reader must reconstruct. The reader should not spend effort deciding what a clause is about.

## VP6. No self-undermining wording

Words that make the work sound derivative or optional are banned in the Abstract, Introduction and Conclusion: "re-examine designs" (implies the designs are someone else's), "we merely", "a simple attempt", "preliminary". The Contribution list states what was built.

## VP7. Contribution framing

Each contribution is a complete sentence: object, substantive change, capability, support. Module names alone are not contributions. Do not split one idea to manufacture a third item; do not present a rank or a largest ablation drop as novelty.

The lead-in is stated plainly ("The main contributions are summarized as follows:" or "Overall, the contributions can be summarized as follows:"). Do not promise a "future" framing in the Introduction, and delete "We hope ...".

## VP8. Sensitive application framing

Choose application framings that a broad reviewer pool receives neutrally. Avoid national-security, surveillance, policing, medical-diagnosis and clinical claims unless the paper actually validates them, and never state a clinical capability the experiments do not test. Prefer what the task measures and the scientific use of that measurement.

## VP9. Do not invent a deployment story

"Deployed", "in production", "real-time system" require evidence of that deployment. A method tested offline is described as tested offline.

## VP10. Weight follows importance

A key result gets a concrete number (through a macro generated from the admitted table), a clause saying why it is strong, and an analysis sentence. A key result squeezed into a trailing "also ... since ..." clause reads as unimportant and will be treated as such.

Detail may be uneven: the strongest finding gets the most space, secondary findings get one clear sentence each, but no central finding may be left without its insight.

## VP11. Self-check before delivery

Read the requested unit as a reviewer looking for a reason to reject. Ask of every paragraph: does it leave the reader thinking better of this work than before, or worse? If worse, either the evidence does not support the paragraph's role or the wording is defensive. Fix the wording first; if the paragraph has no positive role, cut it.
