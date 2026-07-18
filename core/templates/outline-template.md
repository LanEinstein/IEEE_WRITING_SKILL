<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Outline Deliverable Template (ieee-write, stage W2)

The outline is the contract between the author and the suite: drafting starts
only after the user explicitly passes the outline review. Produce the outline
as `paper/OUTLINE.md` in the user's project with the following structure.
Every number cited in the outline must come from the fact sheet
(`paper/FACT_SHEET.md`), which records only tool-produced values.

```markdown
# Paper Outline: <working title>

## -1. Target venue and profile
- Target: journal/conference + specific venue; profile loaded from
  core/literature/venue-style-profiles.md (state which, and whether the
  default was assumed). Template, page cap, anonymization mode.

## 0. Title and thesis
- Title candidates (2-3), each <= 15 words, problem + approach keyword.
- One-sentence thesis: the single claim the whole paper defends.
- Contribution list draft (3-4 items, mapped to evidence in the fact sheet).

## A. Story in one paragraph
Hook -> gap -> proposal -> headline results, as one connected paragraph.
(The paragraph later seeds the abstract, but the abstract is written last.)

## B. Section-by-section plan
For EACH section (I Introduction / II Related Work / III Method /
IV Experiments / V Conclusion), list every planned paragraph as:
- (p<N>) CLAIM: what the paragraph asserts.
  DATA: which table/figure/fact-sheet entry supports the claim.
  NOTES: rule reminders specific to the paragraph (e.g., S-RW-1 for a
  related-work paragraph).
Method subsections mirror the module structure; experiments subsections
follow the canonical order (setup -> main comparison -> analyses ->
ablation -> further evaluations).

## C. Floats plan
| Float | Content | Claim it carries | Section | Source of numbers |
One row per table and figure. Every float carries exactly one claim.

## D. Main-figure drawing suggestions (user draws the figures)
For each figure the user will draw: purpose, essential visual elements,
what must NOT be in the figure (no fabricated data), block names that must
match subsection titles character for character (S-MET-7), and the agreed
file path where the user will place the finished figure. Every figure spec
(user-drawn or generated) restates the applicable items of
`core/rules/figure-standards.md`.

## E. Literature plan
Candidate references per section with verification status
(verified/pending), venue tier, and any arXiv-only flags awaiting the
user's ruling (L2/L3).

## F. Open items
TBD numbers awaiting runs, missing artifacts, decisions the user still owes.
```

Gate reminder: iterate on user feedback for as many rounds as needed. Only an
explicit statement that the outline review has passed unlocks stage W3
(drafting). Record the approval verbatim in `paper/OUTLINE.md` under a
"Approved on" line.
