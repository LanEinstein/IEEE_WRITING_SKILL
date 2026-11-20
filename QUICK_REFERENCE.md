<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# One page: the rules that decide most revisions

Keep this open while drafting. Each line points to the file that explains it.

## Before writing

1. Write the paragraph's claim in one sentence. If it is not a claim, the paragraph has no job. → [paragraph-architecture.md](core/rules/paragraph-architecture.md) PA1
2. Never translate a plan, an instruction or a Chinese draft. Write from the claim's function. → [translation-discipline.md](core/rules/translation-discipline.md) TD1
3. Write the claim, the evidence, the mechanism and the implication on a card first. → [paragraph-card.md](core/templates/paragraph-card.md)

## The paragraph

4. First sentence: a conclusion, covering every point the paragraph makes; the subject is the method, protocol or finding, not a table. → PA2
5. Every observation gets one analysis sentence, joined by the observation's subject. → PA3
6. End on the paragraph's own theme; a selling line about the field belongs in the Conclusion. → PA4
7. One fact, stated once. Later paragraphs recall it with a short noun phrase and a section pointer. → PA11
8. Nothing in a paragraph that does not serve its thread; no internal vocabulary, no development history. → PA12

## The sentence

9. Known information first, new information last; subject and verb close together. → [sentence-craft.md](core/rules/sentence-craft.md) SC1
10. A connective asserts a relation: write "premise ⇒ conclusion" before keeping therefore/thus/so. → SC2
11. One connective or limiter per paragraph; never two "only"/"also" in one sentence. → SC4
12. Repetition: limit frequency, never purge; never swap in a word that becomes the new dominant one. → SC5
13. A pronoun needs exactly one possible referent; bare "This shows" is out. → SC6
14. No colon or dash in body prose; no semicolon in a caption. → SC10
15. Absolutes (must, any, every, only) are replaced by the tested scope. → SC12

## The words

16. Introduce a component with introduce/apply/adopt; a metric falls by "reduces/degrades", never "loses". → [lexicon.md](core/rules/lexicon.md) LX1
17. No engineering vocabulary: recipe, registered, fits, run plan, package, deployed. → LX2
18. Delete filler: neutral, by itself, essentially, clearly, markedly. → LX3
19. No machine frames: lies in, relies on, it itself, plays a key role, serves as. → LX5
20. Use the field's own word: combine/composite for merged data, subject not person. → LX7

## The claim

21. Sell the work; do not pre-empt an objection nobody raised; never end on a competitor being best. → [voice-and-positioning.md](core/rules/voice-and-positioning.md) VP1–VP2
22. State a difference directly; the reviewer is not a detective. → VP3
23. Criticise procedures, not people; no named-method failure claims. → VP4
24. A contribution names an object, a change, a capability and its support. → VP7
25. No deployment, clinical or security claims without the corresponding evidence. → VP8–VP9

## Terms and symbols

26. One object, one name; no renaming for variety; define before use. → [terminology-and-notation.md](core/rules/terminology-and-notation.md) TN1–TN2
27. A symbol used once is not a symbol; one letter, one meaning; define every term in a display. → TN4–TN5
28. Figure labels, legends and text names agree exactly. → TN6

## The round

29. Proposal card: exact original, exact replacement, one sentence of reason. → [proposal-card.md](core/templates/proposal-card.md)
30. Apply only what was approved; re-read it in context; recheck the next paragraph's first sentence. → [revising.md](core/rules/revising.md) RV3, RV8
31. Length does not grow unless asked; when it does, say what pays for it. → RV5
32. Self-review before the author sees it; report what it changed. → RV9
33. Close the round: proposed, applied, rejected, open, version. → [review-loops.md](core/rules/review-loops.md) RL8

## Layout

34. Measure, do not estimate: build, read the line, change one item, rebuild. → [layout-and-build.md](core/rules/layout-and-build.md) LB2
35. No one- or two-word last lines; no heading alone at a page bottom; no sparse page. → LB4, LB9

## The last two commands

```bash
python3 scripts/prose_lint.py FILE.tex --quiet     # H = 0
python3 scripts/pronoun_check.py FILE.tex          # every referent unique
```
