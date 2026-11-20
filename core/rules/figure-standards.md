<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Figures, tables, captions, and visual results

## FIG1. Start from a question and real sources

For each float record the reader's question, necessary content, source/version, comparison, statistical meaning, and text location. Concepts depict actual method relationships; evidence figures use existing data with provenance. No writing rule requires a new diagnostic run, cost experiment, or scatterplot. Do not fabricate data or infer a method from an outdated figure.

## FIG2. Method semantics and names

Check inputs/outputs, branch roles, frozen/trainable parameters and normalization state, gradient paths, adapters, stage numbering, axes, loss edges, and inference. Every meaningful heading maps to a canonical node or declared panel/acronym via [title-figure-symbol-map.md](../templates/title-figure-symbol-map.md). Composite headings map to their actual components. Small operators need no separate subsection. Do not confuse callout leaders with computation arrows or repeated blocks with shared weights.

If the final figure does not exist, deliver a planned mapping/specification and mark final verification pending. When it arrives, inspect actual labels/relations. Planned and checked are different states.

## FIG3. Data and table semantics

Axes/headers declare quantities, units, metric direction, and aggregation. Captions/notes explain bold, underline, shading, daggers, missing-result reasons, selection rules, and uncertainty estimator/count. Keep cross-figure colors/names consistent and distinguish key objects in grayscale. Do not imply significance from best-value formatting. Rank counts, statistical outcomes, and missing results are separate.

If a compact table shows selected baselines, declare the selection criterion and full-table location; preserve exceptions that alter claims. State quoted/reproduced/adapted baseline provenance honestly. Do not claim identical conditions unless verified.

Print leading zeros (0.73, not .73); make highlight colours dark enough to read in greyscale; move unit or marker symbols from the header into the caption; do not keep empty cells — every cell is either a result or an explained absence.

## FIG4. Resolution and fonts: check actual official scope

Prefer vector plots/diagrams with editable source. The [IEEE resolution page](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/resolution-and-size/) checked 2026-10-18 specifies >300 dpi for non-vector color/grayscale and >600 dpi for black/white line art. Upsampling cannot restore detail. Follow publication-specific requirements and final physical size.

The [file-formatting guidance](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/file-formatting/) checked the same day recommends several fonts and appropriate embedding/outlines. Times New Roman is a valid project choice, not the only IEEE font. Check legibility at final column width, including subscripts, formulas, and legend text.

## FIG5. A results figure must carry new information

A figure that redraws table content, illustrates an operation the reader already understands, or shows a deterministic transformation whose outcome is implied by its definition adds nothing. The test: what does the reader know after this figure that the text and tables cannot give? If the answer is "nothing", delete the figure or give the space to another float.

- New evidence may be what a trained model responds to, per-class spatial structure, or an intervention on real inputs.
- Visualise what is visual: a real image or real flow field with real annotations beats a schematic; a heatmap no one can check against data is decoration.
- Panels must not contradict each other; check the numbers across panels.
- One figure, one message. Drop panels that do not serve it, even if they took work.
- Text must not overlap graphics; labels must be readable at final size; the palette is chosen from published figures, not from defaults; a light panel on a light background has no contrast.
- Legends are boxed and aligned with the content above them; no decorative marks without function.

## FIG6. Captions

The caption helps a reader interpret the float where it sits. It is not a place for analysis, motivation, or extra results.

- Length: as short as the float allows. A single-panel float may need only a title phrase. A five-line caption is already long in a two-column layout.
- First sentence: a noun-phrase title of what the figure shows, readable on its own and following the exemplar habit of the target venue.
- Then only what is needed to read the figure and is not in the text: what each panel compares, what colour or shading means, what the error bars are, what a symbol is if the text defines it later.
- Do not describe what the reader can see. Do not restate a table. Do not repeat the analysis. Do not introduce a comparison the figure does not support.
- Multi-panel floats still need one short sentence per panel.
- Every sentence is a complete sentence; no semicolons; no chains of "namely ... with ... and ...".
- Terms, metric names, abbreviations and symbols match the text; a term coined in the text appears in the caption only with one clarifying phrase.

## FIG7. Joint page inspection

After structural/float edits, inspect affected rendered pages for citation distance, reading order, orphaned headings, equation/label clipping, table whitespace, and readable final scale. Preserve official template dimensions and font sizes rather than shrinking everything to force a cap. Use the real build; mark page QA unavailable if not run. A successful compile alone does not establish layout quality.

## FIG8. Provenance and metadata

A figure produced by a plotting script is regenerated from the script, not edited in the PDF. Keep the script, the data snapshot and the settings with the source, and note which version the manuscript uses. Figure PDFs carry metadata (producer, author, path) into the paper's PDF: suppress it at build time and scrub the figure files. Never ship a figure whose labels contain internal names, dates or draft markers.

## FIG9. Prompts for external drawing tools

When a figure is produced by an external design tool, the prompt states: the message of the figure, the panels and each panel's message, the data each panel shows, the palette and typography, the alignment requirements, the final physical size, and the output format (editable). Review the returned figure against FIG5–FIG6 before it enters the manuscript, and record what was checked.
