<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Layout, space, and build hygiene

Layout work starts only after the text is final, and it is measured, never estimated.

## LB1. Page budget before drafting

Establish the hard page limit, which parts count toward it (some venues exclude references, statements and appendices), and a budget per section. Write the budget down. Every later addition is paid for within its section before it is proposed.

Consult the current official instructions for the target; do not carry a page limit from another venue or from memory.

## LB2. Measure, do not estimate

Line counts do not add up: a page break absorbs or amplifies a change, a heading pushed to the next column costs two lines, and float placement moves text. For every layout-sensitive change:

1. build;
2. read the actual line number of the section heading or the last line of the target page;
3. change one item, rebuild, read again;
4. after combining the items, verify the target page once more.

Keep a record of the measured value per candidate. Report the measured page and line, not an estimate.

## LB3. Density

Top-venue papers are dense. Diagnose looseness by mechanism, not by eye:

- global float and text spacing parameters (float separation, text-float separation, gaps above/below displays);
- heading spacing and `\clubpenalty`/`\widowpenalty` interactions that push a heading to the next column;
- over-wide floats that leave a column short;
- display equations with generous local spacing;
- tables with excessive row stretch;
- forced breaks and `\newpage`/`\clearpage` that were right before the last edit.

Fix the parameter, then re-measure. Do not shrink fonts or margins the template fixes.

## LB4. Orphans and widows

- No one- or two-word last line in a paragraph. Three words is acceptable only if nothing shorter is available; verify by printing the last two lines, never by joining them.
- No heading alone at the bottom of a page.
- No figure or table separated from its first citation by more than a page.
- No single line of a paragraph at the top of a column.

## LB5. Floats

Place a float's source near the page where it is cited. Wide floats span both columns; a wide table in a two-column layout that cannot fit becomes a spanning table rather than a squeezed one. Check that numbering follows the citation order.

## LB6. Alignment and whitespace

- Column bottoms align where the venue's design expects it (a table that ends a column and a conclusion that ends the other should end together, within a fraction of a point).
- A figure's panels align on their outer edges; a statistics panel inside a figure aligns with the rounded panel above it.
- No large white bands inside a page, below a figure, or above a section heading.
- Captions are not sparse relative to the float they describe.

## LB7. TeX hygiene

- No comments that instruct, narrate the process, or reveal AI assistance. Keep only the template's official comments.
- No internal identifiers, dates of internal review rounds, file paths, hashes, task codes or draft markers in the source or the PDF.
- No metadata leaks: an inserted PDF carries its producer, author and path information into the output. Set the suppression mechanism for the engine in use and scrub figure metadata; check the shipped PDF's document information.
- One build engine, configured once; auxiliaries and intermediates go to a build directory, not next to the sources.
- Build the official sources with the official class and options; never modify margins, font sizes or column widths to make content fit.

## LB8. Warnings

Treat unresolved references, missing citations, overfull boxes above a small threshold and "rerun to get cross-references right" as defects. Build until the log is clean. If a warning is unavoidable, record why.

## LB9. Supplement layout

The supplement follows the venue's format. Balance columns; avoid a page holding only one float; re-place any forced column break after supplement text changes (a stale forced break is the most common cause of a sparse page). Every table in the supplement is cited from the main text or the supplement text.

## LB10. Visible-change discipline

A change that alters visible text needs the author's approval like any other text change. A change that only alters spacing, and provably leaves the text identical, does not; it is still measured and reported.

## LB11. Final inspection

After the last layout change, render every affected page and inspect it: reading order, float placement, caption legibility at final size, equation clipping, table whitespace, orphaned headings, column balance, and the last page's fill. A successful compile is not a layout check.

## LB12. Delivery artefacts

Ship only the designated PDFs, built from the official sources with the configured engine. Verify that the shipped PDF contains the latest approved text: read a sentence that changed in the last round, not only the file timestamp.
