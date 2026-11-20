<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Prose rules: content before surface form

These rules govern journal-method drafting and scoped polishing. The explicit sentence blueprints are in the relevant section files. Their counts are house defaults, not IEEE requirements.

## G1. Explicit referents
Use concrete nouns when a pronoun could point to multiple mechanisms, quantities, or studies. Clear pronouns are allowed. An author's strict pronoun ban is an optional project preference; record its exact scope and exceptions rather than imposing it on every project.

## G2. Logical transitions
Use However for a contradicted expectation, Therefore/Accordingly for a supported consequence, Specifically for elaboration, and Finally for a genuine final operation. Place and punctuate connectives naturally. A connective cannot supply a missing logical relation.

## G3. Accurate assertions
Prefer direct factual wording; preserve negative results and limitations when scientifically material. Do not replace “no detected difference” with equivalence, or a tentative interpretation with a causal assertion merely to sound positive.

## G4–G6. Connected facts and operational explanations
A paragraph answers one question. Connect operation, functional consequence, evidence, and local implication. Separate what was measured from what follows from the method definition. Explain physical/algorithmic behavior plainly; avoid unmeasured “better semantics,” “stability,” or “overfitting prevention.”

## G7. Every numeric statement must remain true
Keep comparator, metric, range, scope, and aggregation intact. Use at most/at least/range only when appropriate. Compute derived values with a tool. Do not turn a best-case improvement into a universal gain.

## G8. Syntax and collocations
Keep modifiers attached to their grammatical subjects and the main subject/verb easy to identify. Use established collocations and consistent tense. Tense follows completed vs proposed work, not a template's wording.

## G9–G12. Readable sentence structure
Avoid repetitive parallel clauses, dense parenthetical interruptions, and overloaded sentences. Semicolons, em dashes, and clear pronouns are not universal IEEE violations. If the author explicitly bans a form, apply the recorded preference within its scope and preserve meaning. Repeated noun phrases are preferable to ambiguity, not obligatory everywhere.

## G13. Claim strength and terminology
Use a stable canonical name for each module, metric, and operation. Evaluative adjectives, “significant,” “robust,” “optimal,” “first,” and theoretical properties need the relevant evidence and conditions. Do not rename a technical object for lexical variety. Ordinary wording changes must not change scientific scope.

## G14. Information density
Reduce conjunction chains by splitting independent tasks or subordinating actual causes. Keep concrete operations and essential conditions when shortening. A shorter paragraph with “demonstrates effectiveness” substituted for an explanation is not an improvement.

## G15. Topic sentence first: required in the structured profile
Every natural paragraph begins with a sentence that governs its task; the remaining sentences develop it. All experimental paragraphs comply, including setup, chapter openers, comparisons, ablations, diagnostics, and failures. A result paragraph must also explain operational reasons/mechanisms with calibrated evidence. Read only the first sentences: they should already expose the section's argument.

For experiments, start with the factor or bounded finding, not “Table X,” “As shown in Fig. X,” a dangling question, or a repeat of broad motivation. The table locator belongs in the evidence sentence. See [section-experiments.md](section-experiments.md).

## Sweep interpretation
`scripts/sweep_prose.sh` detects candidate surface patterns and unresolved markers. It does not judge referent clarity, causal validity, or IEEE compliance. Classify hits using the active author preferences and context. A nonzero pronoun count is not a failure without an applicable ban; zero hits is not proof of scientific correctness.

## Where the detail lives

This file states the shared principles. The rules that make them operational are:

- [voice-and-positioning.md](voice-and-positioning.md): sell the work, positive framing, claim scope, sensitive applications.
- [paragraph-architecture.md](paragraph-architecture.md): one argument per paragraph, governing first sentence, analysis after observation, endings, transitions.
- [sentence-craft.md](sentence-craft.md): information order, true connectives, repetition control, referents, punctuation.
- [lexicon.md](lexicon.md): words and frames that weaken a manuscript, with replacements.
- [translation-discipline.md](translation-discipline.md): never render a plan or an instruction; the eight Chinese structures behind English faults.
- [revising.md](revising.md): polish scope, preservation list, check order, self-review.
- [review-loops.md](review-loops.md): simulated review, reader feedback, multi-pass read-through.
- [terminology-and-notation.md](terminology-and-notation.md): one name per object, definitions before use, minimal symbol set.
- [layout-and-build.md](layout-and-build.md): measure, do not estimate; density, orphans, TeX/PDF hygiene.
- [figure-standards.md](figure-standards.md): figures must carry new information; caption discipline.

Conflict resolution: an explicit instruction in the current session wins inside scientific accuracy; then the project's recorded preferences; then these house defaults. Record the exception with its scope instead of silently diverging.

## Defaults that projects commonly override

Pronoun use, semicolons, em dashes, "rather than", bold for defined terms, and caption length are author or venue preferences, not IEEE rules. The house default is strict for the English drafting path (see [sentence-craft.md](sentence-craft.md), [lexicon.md](lexicon.md)); a project may relax an item, and the relaxation is written down once with its scope.
