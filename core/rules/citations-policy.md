<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Citations Policy (L1-L5)

Literature handling for drafting, polishing, and review. Backed by
`scripts/verify_citations.py` and `core/literature/venue-tiers.md`.

## L1. Every citation is verified against a live index
Before a reference enters the .bib file, verify the tuple
(title, venue, year, DOI) against Crossref or OpenAlex (primary backends;
Semantic Scholar and DBLP as fallbacks). Run
`scripts/verify_citations.py` on the .bib and keep the verification report
with the manuscript. A citation that cannot be located in any index does not
exist for the purposes of the manuscript.

## L2. Venue quality gate
Only top venues by default: the tier list in
`core/literature/venue-tiers.md` governs. A reference outside the tiers is
denied by default; an exception requires an explicit user approval with a
one-line justification (for example a niche venue that is standard in a
subfield). Record approved exceptions in the verification report.

## L3. arXiv interception
For every entry whose venue is arXiv:
1. Search Crossref/OpenAlex/DBLP for a peer-reviewed published version.
2. If found, upgrade the entry to the published venue.
3. If not found, place the entry on an "arXiv-only" list and ask the user to
   rule case by case. The default is exclusion: arXiv is cited only when
   necessary (for example a dataset or tool that exists nowhere else).

## L4. Bib hygiene
- Brace-protect proper nouns in titles (`{ImageNet}`, `{Bayesian}`).
- One consistent venue naming convention across the file (either full names
  or one abbreviation standard, never mixed).
- Required fields present per entry type (journal: author, title, journal,
  volume, pages, year, DOI; conference: author, title, booktitle, pages,
  year).
- After compilation: scan the .blg for warnings and the PDF for `?` marks
  (unresolved citations), and report counts.

## L5. Never invent a citation
While drafting, if a claim needs a source that is not yet verified, write the
placeholder `\textcolor{red}{[CITE: one-line description]}` instead of a
guessed reference. The final sweep counts these placeholders, and the count
must reach zero before submission by real verification, never by deletion of
the claim marker without resolution.
