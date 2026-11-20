<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Translation discipline: write English, not Chinese in English words

The most common defect in drafts written by non-native authors with an AI assistant is a sentence that is grammatical English but follows a Chinese argument order, a Chinese connective pair, or a Chinese topic frame. It is not fixed by swapping words; it is fixed before drafting.

## TD1. Never translate a plan, an instruction, or a Chinese draft

A Chinese plan defines what a paragraph must accomplish. A Chinese instruction defines what the author wants the sentence to mean. Neither is a sentence to render. Before writing any English sentence:

1. state its function (claim, design, evidence, mechanism, inference, concession, contrast, closure);
2. state the information it carries and which part the reader must already know;
3. choose an English frame for that function, from the section blueprint or from published papers in the target field;
4. write the English sentence from the frame, without looking at the Chinese.

If the author supplied a Chinese sentence, extract its claim first. Check the claim for factual errors and tell the author; then write the English independently. When the English deviates from the literal meaning (for example "is shown" instead of "is proven" because the evidence is empirical), say where and why.

## TD2. The eight Chinese structures behind English faults

| Class | Chinese source | English symptom | Fix |
| --- | --- | --- | --- |
| T1 modifier first | 因为…, 在…条件下, 与…相比, 没有…时, 基于… | one or two long adverbial clauses before the subject; participial opener plus comma | operation as subject: "Removing X barely changes Y, whereas removing Z lowers Y sharply" |
| T2 causal pair | 因为…所以; 由于…因此 | because/since and so/therefore in one sentence; although with but/yet | one connective per sentence, conclusion must follow from premise |
| T3 lexical calque | 确实, 之前的方法, 有利于, 来自原文, 闭合, 数量为 | emphatic "do", "earlier X", "in favour of", "from the original papers", "close over", "number" as verb | the field's word: prior work, supports, from the source records, separates, contains |
| T4 register | 使用, 损失, 配方, 登记, 拟合 | use, lose, recipe, registered, fit as noun | introduce/apply, reduce, configuration, fixed in advance, training |
| T5 island sentences | 意合: relations left implicit | each sentence states a fact, no visible link | link every sentence to the previous one by subject, relation clause or sentence-initial connective |
| T6 redundancy | repetition for emphasis; stacked qualifiers | same connective twice per paragraph, same phrase twice in a sentence, decorative adverbs | one statement per fact; delete the qualifier |
| T7 empty sentences | 总结式泛句 without information | "X depends on A, B and C"; "A cue seen only during training still benefits the network" | state the claim; give the evidence; delete if the fact is already known |
| T8 template monotony | one frame for every subsection | "To test whether ..." three times; "in X and in Y on Z" | vary the opener; merge prepositional phrases |

## TD3. The corpus is the arbiter, not intuition

Before using an unfamiliar structure, check that published papers in the target field use it. Sentence-initial "However" is common, sentence-initial "Because" is not. This is a frequency argument, not a grammatical one: a zero-hit phrase is a risk, not a proof of error, so the corpus is consulted for openers, adverb choice and frame phrases, never used to ban a technical term.

## TD4. Draft from an argument card

For each paragraph, note four items in English keywords: CLAIM, EVIDENCE (float or record), REASON/MECHANISM, IMPLICATION. Do not draft from a Chinese paragraph. Do not open the Chinese plan while writing the English sentence.

## TD5. Checks in order, before delivery

1. Structural lint: `scripts/prose_lint.py` reports H (hard) and S (soft) hits. H must be zero.
2. Calque review: for each sentence, check whether its structure maps one-to-one onto a Chinese frame in TD2.
3. Link test: every sentence after the first states its relation to the previous one with a visible marker.
4. Causal test: every therefore/thus/so/because asserts a relation that holds by itself.
5. Delete test: delete each sentence and ask whether the paragraph loses a fact, a rule or a mechanism.
6. First-reader test: for each term, abbreviation, symbol and number, ask whether the reader has met it before.
7. Referent test: `scripts/pronoun_check.py`, then repeat any noun whose referent is not unique.

## TD6. Keep the check script honest

The script detects structures, not meaning. It cannot judge whether a sentence has content, whether an inference is valid, or whether a paragraph is coherent. Zero hard hits means "no known Chinese structure", not "good English".

## TD7. When the author rewrites a sentence, adopt the meaning

A rewrite from the author, or a translated remark from a reviewer, is an instruction about meaning. Check it for factual accuracy first; if it contains an error, correct it in the author's language and get confirmation; then write the English from the corrected meaning. Never translate the author's wording word for word, and never silently change the claim.

## TD8. Report the discipline

In the delivery note, state which Chinese-origin structures were removed and what replaced them. This is the only visible evidence that the rule was applied rather than claimed.
