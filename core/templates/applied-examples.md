<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Applied Examples: How the Rules Land in a Real Manuscript

Worked, END-TO-END examples showing several rules composing in one passage.
All examples are de-identified: method names, numbers, and domains are
fictitious placeholders (a compact recognizer "AcmeNet" against a heavyweight
baseline "GiantNet"). If a locally configured golden sample exists
(`golden_sample_path` in `local/config`), read that manuscript alongside this
file as the living exemplar; never quote an unpublished manuscript into any
shipped or generated artifact.

## Example 1: Abstract skeleton instance (S-ABS-1 + G1/G5/G7)

"Subtle events reveal safety-critical states, so subtle-event recognition
supports monitoring and screening. However, existing methods have two
limitations. First, high-capacity models read the raw frame, where nuisance
factors dominate the weak target signal, so the reported gains confound
signal, nuisance, and model capacity. Second, handcrafted descriptors
summarize the field before the classifier, so local structure is discarded
and only a linear readout remains. We therefore propose AcmeNet, a compact
recognizer that reads only the target signal. To resolve the first
limitation, the input is restricted to derivative maps with no nuisance
pathway. To address the second limitation, a zero-parameter stem exposes the
local structure before any learning, and a small encoder learns only the
nonlinear residual above a linear floor. Across three benchmarks, AcmeNet is
statistically tied with or better than all baselines, with at most 0.2% of
the largest baseline's trainable parameters."

Note the moves: consequences inside each limitation ("so ..."), causal chains
kept intact (G5), the bound "at most 0.2%" instead of a bare single value
over a range (G7), zero banned pronouns (G1), no self-labels (D5).

## Example 2: Protocol mechanism sentence instead of a purity label (D5)

- Wrong: "All results use a leakage-free protocol."
- Right: "Within each fold, the subjects are split three ways into disjoint
  fitting, validation, and test groups. Standardization statistics are
  estimated on the fitting group, while early stopping and every
  configuration choice read the validation group. Each test fold is scored
  once and never enters training, model selection, or standardization."

The right version states only verifiable mechanisms. A reader concludes the
protocol is clean; the text never begs for that conclusion.

## Example 3: Symbol continuity across equations (S-MET-2)

"Late fusion concatenates the three features, and one linear layer computes
the class logits,
  h = [phi_a; phi_b; phi_c],   z = W h + b,           (1)
where phi_a, phi_b, and phi_c are the branch features defined in Sections
III-B to III-D, and z holds the logits of the K classes. ... The classifier
is trained by cross-entropy on the prior-adjusted logits,
  L = -(1/B) sum_i log softmax(z_i + log pi)_{y_i},   (2)
where z_{i,k} is the logit of class k for sample i, computed by Eq. (1), and
pi is the class prior estimated on the training fold."

The phrase "computed by Eq. (1)" is the load-bearing move: the symbol in
Eq. (2) is explicitly wired to its defining equation, so no symbol appears
in isolation.

## Example 4: Headline + interpretation + tie resolution (S-EXP-1..4, D2)

"Across all six settings, AcmeNet is statistically tied with or better than
every baseline (Table III). The clearest separation appears on the largest
benchmark, where AcmeNet is the only method to significantly outperform all
baselines under the paired bootstrap defined in Section IV-A. AcmeNet ranks
second on the two remaining settings, reaching 0.71 versus GiantNet's 0.73,
and the paired difference includes zero in both, so the two methods are
statistically tied at orders of magnitude fewer parameters."

Moves: table lead-in before numbers, significance tied to the pre-declared
test only (S-EXP-7), the second-best cells resolved positively in one
sentence with a real interval statement (D2/D6), no losing-cell enumeration.

## Example 5: Per-paragraph polish proposal format (G16)

| # | Original | Proposed | Rule |
|---|---|---|---|
| 1 | "This shows the design is robust; it also runs fast." | "The ablation shows the design is stable, and the runtime stays below 2 ms." | G1 (this/it), G10 (semicolon), G13 (robust -> checkable fact) |
| 2 | "However the gain is large." | "However, the gain is large." | G2 |

Presentation rule: the proposal table is shown to the user and NOTHING is
edited until the user answers `go` (see `core/rules/workflow-gates.md`).
