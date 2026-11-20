<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Review loops: simulated review, expert feedback, read-through

This file covers the parts of the process that sit between drafting and submission: structured self-review, simulated peer review, handling a real reader's remarks, and the multi-round read-through. [../review/](../review/) holds the review lenses; this file holds the loop that uses them.

## RL1. Three review modes, never mixed up

| Mode | What it is | What it may claim |
| --- | --- | --- |
| Self-review | the same agent reads the manuscript against the rules | "checked against rules X, Y"; never "independent review" |
| Simulated review | review lenses applied by the same agent, or by another available and authorized model | "simulated review by N lenses"; never a prediction of the real decision |
| Real reader | a human expert's remarks | their opinion, quoted; adjudicated, not obeyed |

Never present a self-review as a second opinion, and never invent a reviewer's agreement.

## RL2. Simulated review: two readings, one synthesis

When the author wants a mock review, run two readings and present them separately:

1. **Criteria reading:** review against the target venue's own evaluation dimensions (problem significance, novelty with respect to the closest work, soundness of the method, sufficiency of the evidence, clarity, reproducibility). Base the criteria on the venue's published guidance and on papers of that venue, not on memory.
2. **Unaided reading:** review from evidence and logic alone, without the criteria list, so that a defect the criteria miss still surfaces.

Then adjudicate: for each remark, decide materially supported, stylistic, mistaken, or out of scope, and say why. The author sees the adjudicated list, with the raw remarks available. Do not flood the author with a hundred low-value items; rank by impact on acceptance.

A quality score, if the author asks for one, is a qualitative judgement for internal use. It is not a calibrated acceptance probability and is labelled as such.

## RL3. Handling a real reader's remarks

1. Read the whole remark set before acting; the overall comment often explains the individual ones.
2. Separate a structural remark ("this section reads like a lab notebook") from a local one ("this sentence is unclear"). A structural remark gets a plan, not a patch. See [../rules/revising.md](revising.md) RV1.
3. Apply the principle, not the instance: find every place in the manuscript with the same defect, list them, and fix them together. A remark answered in one paragraph while its twin survives elsewhere is not answered.
4. Check each remark against the manuscript and the evidence before adopting it. A reviewer can be wrong about what the text says; say so plainly, with the quotation.
5. Preserve the reviewer's wording in the record; keep interpretation separate.
6. Never put the review exchange in the manuscript.

## RL4. The proposal page

When a round has more than a handful of items, present them on one page rather than in the terminal. Requirements:

- one item per unit: location, exact original, exact proposed text, one sentence of reason;
- an approve control per item, whose meaning is stated ("ticked = apply exactly this text");
- a comment field per item, whose meaning is stated ("commented = do not apply; redraft from the comment");
- optional variants when two acceptable wordings exist;
- page state persisted so a reload does not lose work, and an export that returns the decisions as data;
- a summary of what was applied and what is still open at the end of the round.

`scripts/review_page.py` generates such a page from a small JSON file. State on the page what is not verified (for example, that a rendered page was not previewed).

## RL5. Multi-round read-through

A full read-through is done in passes, each with one focus, because a single pass cannot hold all the checks at once.

| Pass | Focus | Output |
| --- | --- | --- |
| 1 | Section-level argument: does each section deliver what it promises, in a sensible order, with no duplication? | section map with problems |
| 2 | Paragraph level: governing first sentence, analysis after each observation, endings, transitions between paragraphs | per-paragraph issues |
| 3 | Sentence level: connectives true, information order, length, insertions, repetition across the section | per-sentence issues |
| 4 | Word level and terminology: lexicon, register, one name per object, definitions before use | word list with replacements |
| 5 | Numbers and evidence: every value, comparison and rank traced; deltas computed | value table with sources |
| 6 | Layout and artefacts: measured pages, floats, warnings, shipped PDF | measured report |

Each pass produces its own item list. Do not merge passes; an issue found in pass 4 that was caused by pass 2 must be fixed at the level of its cause.

## RL6. Cross-agent review

When a second model or agent is available and the author authorizes it:

- freeze a version identifier before review and give that exact version;
- give the reviewer the task, the scope, the evidence boundaries and the rules, not the conclusion you hope for;
- ask for location, consequence, evidence, proposed fix, and the condition under which the item is resolved;
- adjudicate every finding; adopt, modify, or reject with evidence;
- a reviewer's editorial preference is not a defect; a reviewer's factual error is corrected, not debated;
- report which version was reviewed and by whom.

## RL7. What a review round must not do

- No new experiments, no re-run, no re-scored result, unless the author expands the task.
- No silent change of a number.
- No weakening of a claim to close a comment, when the claim is supported and the fix is wording.
- No item marked resolved that was not applied and verified.

## RL8. Closing a round

Close a round with: items proposed, items applied, items rejected with the reason, items still open, the version identifier after the round, and the checks run. This record is what makes the next round safe to start.
