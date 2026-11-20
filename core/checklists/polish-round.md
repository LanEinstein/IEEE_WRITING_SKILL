<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Polish round checklist

A polish round is one unit of revision with the author in the loop.

## Before proposing

- [ ] The unit and its neighbours are read; the paragraph's claim is written in one sentence.
- [ ] The evidence behind every claim in the unit is checked, not assumed.
- [ ] The section's role is checked: an analysis section does not design modules, a method section does not report ranks.
- [ ] The rules for the unit are read in full, including the section's hardened checklist.
- [ ] Each item has: exact original, exact replacement, one sentence of reason.
- [ ] Items that would grow the text name what pays for the extra words.
- [ ] Decisions the author must make are listed as decision items, not silently chosen.

## Presenting

- [ ] Few items: terminal, with the full proposed paragraph.
- [ ] Many items: one review page (`scripts/review_page.py`), one item per change.
- [ ] The page states what approval and comment mean, and what was not verified.
- [ ] No item bundles two unrelated changes.

## Applying

- [ ] Only approved items are applied, exactly as approved.
- [ ] Each applied item is re-read in context; the neighbour sentence is checked for a stale referent.
- [ ] Applied items are recorded: id, text, location, round.
- [ ] Rejected items and their reasons remain in the record.
- [ ] Layout is re-measured if text length changed.
- [ ] A round close-out states: proposed, applied, rejected, open, and the version after the round.

## After a rejection

- [ ] The reason behind the comment is identified, not only the wording.
- [ ] If the complaint is structural, a plan replaces a patch.
- [ ] The next proposal for that unit is written as continuous prose in the author's language for logic approval, then in English.

## When the author supplies wording

- [ ] Factual accuracy checked first; errors corrected in the author's language and confirmed.
- [ ] The English is written from the corrected meaning, not translated.
- [ ] Deviations from the literal wording are stated with the reason.
