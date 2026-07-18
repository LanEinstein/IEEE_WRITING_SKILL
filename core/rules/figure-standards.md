<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Figure Standards (FIG-1..FIG-8)

Binding standards for every figure produced during the writing workflow
(experiment plots, diagnostic panels, per-class bars, parameter sweeps).
Main-concept figures drawn by the user follow the same standards; the
outline's drawing suggestions must restate the relevant items.

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
