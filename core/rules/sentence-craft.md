<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Sentence craft: order, connectives, repetition, punctuation

These rules govern single sentences and their neighbours. They assume [paragraph-architecture.md](paragraph-architecture.md) has already fixed the argument.

## SC1. Information order

Put known information at the start of the sentence and new information at the end. Keep the subject and its verb close (normally within the first eight words). This is the topic/stress principle of scientific prose: the beginning connects the sentence backwards, the end carries the point.

A sentence whose first clause is a long condition, cause, reference or comparison places its subject late and reads as translated Chinese. Take the operation as subject instead:

- weak: "Without the projection, M3 UF1 stays nearly unchanged, whereas without the onset–apex flow, UF1 drops sharply in both tasks."
- strong: "Removing the projection barely changes M3 UF1, whereas removing the onset–apex flow lowers UF1 sharply in both tasks."

## SC2. Connectives must state a true relation

Before keeping a connective, write "premise ⇒ conclusion" and check that the conclusion follows from the premise alone.

| Connective | Correct use | Frequent misuse |
| --- | --- | --- |
| However / Yet / But | the expectation just set up is contradicted | two facts placed in sequence |
| Therefore / Thus / Hence | the clause is derivable from the previous statement | an experiment attached as a consequence |
| So | a direct, conversational consequence | a late-clause conclusion, two "so" in one paragraph |
| Specifically | a generalisation is being made concrete | a new topic introduced |
| Similarly / Likewise | a genuine structural analogy | a different result about a different object |
| Moreover / In addition | a second, independent point in the same direction | repeating the previous point |
| Meanwhile | two things happening under the same frame | a different finding |
| Finally | the last item of a stated series | any closing sentence |

If the relation is real but the connective is an over-used one, restructure the sentence so the relation is carried by its subject and verb.

## SC3. Balance, not flooding

A paragraph with no connectives is a set of islands; a paragraph with a connective in every clause is equally bad. Aim for one visible link per sentence: a sentence-initial connective, a relation clause, or a subject that names the previous object.

## SC4. One connective per paragraph

The same connective, or the same limiter ("only", "alone", "whereas", "although", "so"), does not appear twice in one paragraph. Two uses of "only" in adjacent sentences, or "because ... so" in one sentence, are hard faults. With a tense paragraph, vary the sentence structure rather than swapping in a synonym of the same frequency.

## SC5. Repetition control: limit frequency and density, never purge

Word repetition is a signal of machine text. Control it by frequency and density, not by eliminating the word.

- Count occurrences of content words, connectives and limiters across the requested unit. Any word appearing more than about once per two paragraphs, or twice in one paragraph, is a candidate.
- Vary the surrounding structure, the verb, or the subject before replacing a word.
- Never replace a term with a synonym that is itself frequent, and never replace a word so that a new word becomes the new dominant one. Recount every introduced word.
- Fixed terminology is exempt: a canonical technical name is not varied for style.

A machine-written pattern is a repeated frame, not a repeated word: "lies in", "relies on", "X itself", "it alone", "plays a key role". These are removed by rewriting the sentence.

## SC6. No pronoun without a unique referent

Use "this X", "it", "its", "they", "them", "these", "such" only when exactly one noun of the previous sentence can be the referent. Test against every candidate noun; if two fit, repeat the noun.

Bare demonstratives ("This shows ...", "This is because ...") and paragraph-initial pronouns pointing to the previous paragraph are hard faults. A demonstrative whose referent lives across a subsection break is a hard fault even with a plausible antecedent: name the object.

When a polish changes a paragraph's last sentence, recheck the first sentence of the next paragraph.

## SC7. One described object per sentence

Do not coordinate clauses about different objects under one predicate; the reader has to reconstruct who is being commented on. Split the sentence or make the shared subject real.

## SC8. Sentence length and insertion

- One point per sentence. Split sentences over roughly 35 words, and any sentence the author needs two passes to parse.
- Do not stack parenthetical insertions, appositions, or a chain of relative clauses. Two commas inside a clause is a warning; five commas in a sentence is a rewrite.
- Do not place a definitional comma-clause ("whose subjects take no part in training") between a verb and its object.
- Do not use a relative clause inserted before the subject ("Together with X, which ..., the model ...").

## SC9. Active and passive

Academic English uses both. A long run of active sentences reads like a report; a long run of passive sentences hides the actor. Mix them, and keep the passive where the object carries the information ("Networks are trained on four frames" when the training setup is the topic).

## SC10. Punctuation

- No colons or dashes in body prose. Structural colons in a subsection title are allowed. Rewrite the sentence instead: use a full stop, a causal connective, or a reordered subject.
- No semicolons in captions and no semicolon chains in prose paragraphs; split into sentences. A semicolon between two closely related clauses is acceptable only when the target venue's corpus uses it and the author has not banned it.
- Parentheses carry units, abbreviations at first mention, and short clarifiers; they do not carry the main argument.
- Enumerations introduced by a count use a plain sentence ("... are threefold.") rather than a colon.

## SC11. Numbers and words

Write out numbers below ten in prose except when reporting a measurement; keep leading zeros (0.73, not .73). Values of very different magnitude do not share one "respectively" sentence. A count of results ("three of four comparisons") is a numeric result and is governed by the same rules as a metric.

## SC12. Absolutes

"Must", "any", "every", "always", "never", "all" and "only" assert universality that the evidence rarely supports. Replace with what was tested ("tends to", "in the tested networks", "most", "the tested architectures") unless the sentence states a definition or a proof.

"Significant" is reserved for a stated statistical test; a development-screen difference is not significant. "Clear progress" overstates the field; "notable progress" does not.

## SC13. Collocations and register

Use the collocations of published papers in the target field, not the first translation that comes to mind. When unsure whether a word or short phrase is used in the field, search a corpus of the target venue's papers before using it. A phrase with zero corpus hits is not automatically wrong, but it is a risk in a top-venue submission; a rare adverb chosen to save a line is a defect.

## SC14. No showing off

Prefer the plain statement a reader absorbs in one pass over a clever construction. A sentence that impresses on a second reading loses a reviewer on the first.

## SC15. Sentence frames to avoid

- "Relative to X, ..." (translated comparison frame)
- sentence-initial "Because ...", "Since ...", "Like X, ...", "Compared with ...", "Due to ...", "In terms of ...", "As for ...", "Regarding ...", "With the help of ..."
- participial openers ("Scored on ..., the model ...", "Acting on ..., the projection ...")
- "X itself", "it alone", "Y per se" as emphasis
- "rather than" / "instead of" as the main contrast device in a paper that states results positively
- "we use" for introducing a component ("we introduce", "we apply", "the method adopts")
- "To test whether ..." as the opener of several consecutive subsections

## SC16. Two neighbouring sentences must not share their frame

Two consecutive sentences with the same syntactic shape read as generated text. Vary the subject position, the verb type, or the clause order.
