<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Global Prose Rules (G1-G15)

These rules apply to EVERY sentence of EVERY section, in drafting, polishing, and
review. They were distilled from real revision rounds of an IEEE Transactions
manuscript with a senior author. Read this file in full before writing or editing
any paragraph. Enforcement tags: [SWEEP] = counted by `scripts/sweep_prose.sh`,
[MANUAL] = checked sentence by sentence by the writer/reviewer.

Zero-tolerance rules (a compliant manuscript contains ZERO violations, and zero
must be produced by a sweep count, never by impression): G1, G2, G9, G10, G11.

## G1. No vague or ambiguous pronouns [SWEEP + MANUAL]
Never use `this`, `these`, `it`, `its`, `they`, `their`, `them` in manuscript
prose, including the determiner forms `this X` / `these X`. Replace with the
explicit noun, a repeated math symbol, or an allowed substitute (`that`,
`the same`, `the two`, `each`, `both results`).
- Wrong: "Guided by this evidence, we design a compact head."
- Right: "Guided by the diagnostic, we design a compact head."
- Wrong: "...but they summarize only part of its geometry."
- Right: "...but each descriptor summarizes only part of the local field geometry."
- Wrong: "This gap motivates a compact recognizer."
- Right: "The dimensionality gap motivates a compact recognizer."
Repeating a math symbol is preferred over any pronoun: "The prior enters during
training only, and inference scores a clip by the plain logits z."
Exception: the conventional self-references "this paper" and "this work" are
allowed (contribution lists, roadmap sentences). The sweep still counts every
occurrence; a human confirms that each hit is the self-reference form.

## G2. Sentence-initial connectives take a comma [SWEEP + MANUAL]
Logical connectives go at the start of the sentence, followed by a comma:
`However,` `Therefore,` `Finally,` `In addition,` `Moreover,`. Do not bury the
connective mid-sentence.
- Wrong: "The model, however, remains compact."
- Right: "However, the model remains compact."

## G3. Positive phrasing [MANUAL]
State what holds, not what fails to fail.
- Wrong: "is never significantly worse than any baseline"
- Right: "is statistically tied with or better than every baseline"

## G4. Stitch parallel facts into one claim [MANUAL]
A paragraph of disconnected one-fact sentences is not acceptable. Connect facts
so that one becomes the cost, cause, or consequence of the other.
- Wrong: "The model reaches 0.61 UF1. The model has 0.2 M parameters."
- Right: "The model reaches 0.61 UF1 with at most 0.2 M trainable parameters,
  so the accuracy costs orders of magnitude fewer parameters than the largest
  baseline."

## G5. Keep causal chains causal [MANUAL]
When the mechanism is A leads to B, do not split A and B into coordinate
sentences. Restore the chain with `so`, `then`, or `which leaves`.
- Wrong: "The descriptors reach the head at full strength. The encoder learns
  the residual."
- Right: "The descriptors reach the head at full strength, which leaves the
  encoder free to learn only the nonlinear residual."

## G6. Prefer the plain physical explanation [MANUAL]
Replace sophisticated but hard-to-parse clauses with the direct physical reading
already used elsewhere in the paper.
- Wrong: "so the areal and rotational structure a scalar statistic omits reaches
  the network intact"
- Right: "so local expansion and rotation reach the network before any learning"

## G7. Single-value numbers must be true in every sentence [MANUAL]
When a quantity is a range, a bare single value is false for part of the range.
Use a bound that holds everywhere, and compute derived numbers with a tool,
never mentally.
- Wrong: "using 0.15% of the baseline's parameters" (when the true range is
  0.04%-0.15%)
- Right: "using at most 0.15% of the baseline's parameters"

## G8. Grammar self-check: modifiers and collocations [MANUAL]
Check every sentence for dangling modifiers (the modifier must attach to the
grammatical subject) and for standard collocations (`parity with`, never
`parity against`; `on par with`).
- Wrong: "At 0.04 to 0.15 percent of the parameters, parity holds against the
  baselines." (dangling; wrong collocation)
- Right: "The model reaches parity with the baselines at 0.04 to 0.15 percent
  of the parameters."

## G9. No repeated same-form clauses after one verb [SWEEP + MANUAL]
`shows how X and how Y` or `shows that A and that B` reads like a literal
translation and is banned. Split into an independent clause or a prepositional
phrase.
- Wrong: "Fig. 2 shows how the branches fuse and how the loss uses the prior."
- Right: "Fig. 2 shows how the branches fuse into one head, and only the
  training loss uses the prior."

## G10. No clause-joining semicolons [SWEEP + MANUAL]
Two closely related independent clauses are joined with `, and`, not with a
semicolon and not necessarily split into two sentences. List-type semicolons
also lean toward being split into sentences.
- Wrong: "The design is summarized in Fig. 1; the full architecture is given
  in Section III."
- Right: "The design is summarized in Fig. 1, and the full architecture is
  given in Section III."

## G11. No em-dashes [SWEEP]
Never use `---` (or the em-dash character) as a stylistic device in manuscript
prose. Restructure with commas, colons, parentheses, or separate sentences.

## G12. No mid-sentence interrupters [MANUAL]
Unless extremely easy to read, do not interrupt subject and verb with an
appositive or non-restrictive clause. Linearize, or front a participle phrase,
or move the addition to the end of the sentence.
- Wrong: "The pooling, a saliency-weighted pyramid over two grids, reduces the
  map to a fixed length."
- Right: "The pooling is a saliency-weighted pyramid over two grids, and the
  pyramid reduces the map to a fixed length."

## G13. No self-invented modifiers without a standard [MANUAL]
Every evaluative modifier must be verifiable. Replace invented superlatives
with checkable facts.
- Wrong: "the highest-powered benchmark", "a useful signal"
- Right: "the largest benchmark", "a signal that separates the two classes"

## G14. Dilute the density of "and" [SWEEP(count) + MANUAL]
When a paragraph chains several `and` conjunctions, restructure some into
subordinate clauses, participles, or separate sentences. The sweep reports the
per-paragraph count for a human judgment call.

## G15. Topic sentence first [MANUAL]
The first sentence of every paragraph states the conclusion or summary of the
whole paragraph, and the rest of the paragraph develops that sentence. Verify
by reading only the first sentences of a section: the chain must already tell
the story.

## Precedence
When a published exemplar (see `core/templates/exemplar-patterns.md`) conflicts
with a rule in this file, the rule in this file wins. The same holds for venue
profiles: `core/literature/venue-style-profiles.md` conditions section
structure, floats, and register by target venue, but no profile row relaxes
G1-G15. A venue habit that violates a G rule (for example em-dash-heavy
conference prose) is not adopted.
