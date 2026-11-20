<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Proposal card

The unit of an approval round. One card, one change.

```text
ID:            <round>-<nn>
Location:      <section, subsection, paragraph, sentence>
Kind:          edit | decision | deletion | move
Original:      <exact text, copied from the manuscript>
Proposed:      <exact replacement text>
Reason:        <one sentence: which rule, which defect, what it gains>
Evidence:      <source for any number or claim the change touches>
Length:        <words/lines before -> after; what pays for a gain>
Neighbours:    <sentences whose referents or logic the change affects>
Not verified:  <e.g. rendered page not previewed>
```

For a decision card, replace Original/Proposed with:

```text
Question:      <the choice the author must make>
Options:       A) ... B) ...
Recommendation:A, because ...
```

Rules:

- Never bundle two unrelated changes in one card.
- A structural change is a plan plus its carrier sentences, not a card per sentence.
- A deletion names what replaces its function, or says that nothing does.
- `scripts/review_page.py` renders a list of these cards as an interactive page with approve/comment per card.
