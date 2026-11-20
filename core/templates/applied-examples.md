<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Worked examples: mechanics, not research facts

All examples here are synthetic teaching examples. They do not describe a real experiment, provide a citation, or authorize a claim in a manuscript. Fill real plans with the current paper's verified evidence. The [section files](sentence-plan.md) contain the full abstract/introduction/RW/module/experiment blueprints.

## E1–E6 as a complete analytical paragraph

Synthetic source card: variants share encoder/input/adapters/splits/optimization; A updates teacher+student, B freezes teacher parameters and normalization state; the supplied toy table reports the metric higher for B; no forgetting or target-drift measurement was supplied.

> The teacher-update comparison examines whether a fixed reference is useful in the evaluated transfer setting. Both variants retain the encoder, inputs, adapters, and optimization protocol, while only the teacher update policy changes. The frozen-reference variant has the higher reported score in the supplied comparison. Joint training changes both the student representation and the mapping that produces its alignment targets. Freezing preserves the pretrained mapping while allowing the student and adapters to fit the target task. The comparison therefore supports a fixed reference within the evaluated pipeline, without identifying an unmeasured optimization mechanism.

Six sentences: total statement → verified control → evidence → operation A → operation B and relevance → bounded inference. Replace the evidence sentence with source-located actual values when available; never invent a delta. “Prevents catastrophic forgetting” would exceed this source card. Do not delete sentences four/five and substitute “demonstrating effectiveness.”

## Method symbol continuity

> The fusion layer concatenates the branch vectors into h and computes class logits z = Wh + b. The cross-entropy objective uses z from the fusion equation, with the sample and class axes defined before the loss.

The later loss names the symbol's origin. A real method must also define shapes, index ranges, and parameter states. A B×B attention matrix is not a spatial attention map merely because the input originated from an image.

## Scientific meaning during polish

| Source statement | Unsafe edit | Meaning-preserving direction |
| --- | --- | --- |
| Projected means and standard deviations are compared | Full distributions become identical | Name the actual compared moments and scope |
| Each ensemble member uses only the student | One model is evaluated | State the retained member architecture and actual ensemble separately |
| Difference interval includes zero | Methods are statistically equivalent | State the actual result and test/interval conditions; no automatic equivalence |
| One setting has a lower mean | Wins in every setting | Keep the exception and narrow the quantifier |

## Concrete proposal without invented evidence

Original: “This shows the method is robust; it also runs fast.”
Proposal with no measurements available: “The comparison supports the method under the evaluated conditions.”
Reason: the original supplied no robustness scope or runtime measurement. Ask for the relevant source only if the author needs those claims; do not create a 2 ms figure as a language repair. Apply or propose according to existing authorization, not a new mandatory paragraph gate.
