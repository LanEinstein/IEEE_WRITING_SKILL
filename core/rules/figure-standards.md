<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Figure and Table-Presentation Standards (FIG-1..FIG-13)

Binding standards for every figure produced during the writing workflow
(experiment plots, diagnostic panels, per-class bars, parameter sweeps).
Main-concept figures drawn by the user follow the same standards; the
outline's drawing suggestions must restate the relevant items.
FIG-9..FIG-13 are venue-conditional: apply them per the loaded profile in
`core/literature/venue-style-profiles.md` (journal vs conference).

## FIG-1. Resolution
Vector output (PDF) is the default. Any raster export is at least 300 dpi
AT THE FINAL PRINT SIZE. Never upscale a low-resolution render.

## FIG-2. No in-figure titles
Figures carry no title text inside the image (no suptitle, no per-axes
title). The LaTeX caption carries all description. Axis LABELS (quantity and
unit) are required and are not titles.

## FIG-3. Scientific color scheme
Use a colorblind-safe, muted scientific palette, consistent across ALL
figures of the manuscript (one palette per paper). No default rainbow or
saturated primary palettes. Series that must be distinguished in grayscale
print get distinct markers or hatching in addition to color.

## FIG-4. Typeface
All figure text, including tick labels, axis labels, legends, and panel
labels, uses Times New Roman (or the exact serif family of the manuscript
body, e.g., Nimbus Roman / STIX as the system provides). One typeface per
paper, no mixing.

## FIG-5. Font size at print scale
Text must be clearly legible at the final double-column size. Compute
source sizes, never guess: source_pt = target_print_pt x (canvas_width /
print_width). At print scale, every text element is at least 7 pt, with 8-9
pt (caption size) as the target for labels and legends. Verify by rendering
the figure at print width and reading the text.

## FIG-6. Legend
Standard placement, complete (every plotted series named), and NEVER
occluding data marks, bars, or curves. Move the legend outside the axes or
into empty data regions; consistency of legend style across figures.

## FIG-7. Multi-panel labels
Subfigure labels (a), (b), (c) are placed centered DIRECTLY BELOW the
corresponding subplot, never in a corner, never above, never to the side.
Label size follows FIG-5.

## FIG-8. Real data only
Every plotted value comes from a real result file recorded in the fact
sheet, with provenance (V4 of `verification-protocol.md`). Concept figures
contain no fabricated numeric data. Plot scripts are saved beside the paper
(e.g., `paper/figures/scripts/`) so every figure is regenerable, and each
script saves both the vector PDF and a >=300 dpi raster preview.

## FIG-9. Page-1 figure (teaser) [VENUE-CONDITIONAL]
- **Journal profile**: page 1 is usually text-only; Fig. 1 is a page-2
  pipeline or motivation figure. A single-column motivation figure on page 1
  is acceptable, not the norm.
- **Conference profile**: a page-1 teaser is near-mandatory (CVF/AAAI
  corpus: 10/10 award papers carry one). Choose ONE mode and design for it:
  1. *Capability input-to-output*: inputs left, outputs right, one arrow
     chain; caption may carry a speed/scale number.
  2. *Qualitative wall*: a grid of non-cherry-picked results; state the
     selection policy in the caption ("random samples, no re-ranking").
  3. *Failure-mechanism / paradigm contrast*: dissect the incumbent's
     defect, or ladder (a)(b)(c) paradigms ending in ours.
  4. *Performance scatter*: the trade-off plot itself as the teaser
     (accuracy vs cost, ours as a distinct marker).
  Placement: full width above the abstract, or right column beside it.
  The teaser caption states the claim (see FIG-12 conference row).

## FIG-10. Diagnostic (evidence) figure
One data figure that justifies a design choice, placed IN THE METHOD
section next to the choice (corpus pattern: a measured spectrum/histogram
motivating a hyperparameter; a training-curve strip naming a phenomenon).
The figure answers "why this design", not "how much better". Every
diagnostic figure carries real measured data (FIG-8) and its caption states
the design conclusion drawn from the data. Journal profile: also standard,
often as a motivation figure in the introduction or an analysis subsection.

## FIG-11. Trade-off scatter
For efficiency claims, an accuracy-vs-cost scatter: cost axis log-scaled
when spanning decades, our method a distinct marker (star), competitor
points labeled, optional corner cues ("best" arrows). Efficiency deltas in
the caption use multiples ("9x faster"), accuracy deltas absolute numbers.
Journal profile treats the scatter as optional (tables carry efficiency);
conference profile treats it as a strong default for any compact/efficient
method paper.

## FIG-12. Caption register [VENUE-CONDITIONAL]
- **Journal profile**: captions short (1-2 sentences): noun-phrase locator,
  then the reading key. Heavy semantics (color codes, box meanings) live in
  body prose. Conclusions belong to the running text.
- **Conference profile**: captions are self-contained mini-abstracts: bold
  lead (often the method name), reading instructions ((a)/(b) or
  Left/Right walk), and a CONCLUSION sentence; numbers allowed.
- Both profiles: the caption declares every convention the float uses
  (arrows, daggers, shading, error bars with their interval type), and any
  uncertainty band names its estimator and run count, declared at least at
  first use ("shaded: +-1 std over 5 seeds").

## FIG-13. Table background color (P1-P4) and LaTeX mechanics
Color paradigms observed in the corpus, ranked for the suite:
- **P1 own-row pale tint (PREFERRED)**: a light background on the
  proposed-method row/column only. Color answers exactly one question,
  "which row is ours"; best/second/significance stay with
  bold/underline/dagger, so decoloring loses zero information.
  Grayscale- and colorblind-safe by construction.
- **P2 best/second colored cell fills (BANNED, journal profile)**: red/blue
  fills for top entries are grayscale-unsafe and fight the bold/underline
  channel. Conference profile tolerates full rank heatmaps; they do not
  transfer to a journal (re)submission.
- **P3 semantic zone tints**: pale bands separating table regions by
  meaning (taxonomy groups, summary bands). Acceptable in both profiles
  when declared in the caption.
- **P4 group row-bands**: alternating pale bands purely for readability of
  very wide tables. Acceptable; never encodes ranking.
Verified LaTeX mechanics (from a real IEEEtran manuscript):
- `\usepackage[table]{xcolor}` loaded AFTER `array`, BEFORE `hyperref`
  (option clash otherwise); brings colortbl.
- Define named colors once, e.g. pale violet `#ECEBF6` for the own row,
  pale green `#EAF3EA` for a single highlighted winning cell, neutral
  `#F7F7FA` for summary bands; reuse the same three names across all tables.
- Precedence `\cellcolor` > `\rowcolor` > `\columncolor`; `\rowcolor` must
  open the row; column tint via `>{\columncolor{...}}c` (needs `array`);
  `\multirow` cells do not inherit row tints (tint the column instead, or
  `\cellcolor` every spanned row).
- Every colored table's caption carries one neutral sentence declaring the
  color semantics ("the proposed method's row is shaded"), and the table
  must survive grayscale printing with no meaning lost (decolor test).
