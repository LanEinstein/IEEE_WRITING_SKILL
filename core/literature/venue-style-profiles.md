<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Venue Style Profiles (VP): journal vs conference, target-driven

The suite is venue-target driven: every workflow (ieee-write, ieee-polish,
ieee-review, ieee-style) confirms the submission target in Stage 0, loads the
matching profile from THIS file, and applies the profile's conventions on top
of the house rules. There is no single "IEEE default" style; the target decides.

Selection protocol (identical for all four skills):
1. Ask the user: journal or conference, and which venue (free text; map to the
   nearest profile below).
2. If the user does not specify, ASK ONCE. If still undecided, use
   **journal-TPAMI/TIP** as the safe default and STATE the assumed profile in
   every deliverable produced under the assumption.
3. Precedence: `core/rules/` house rules > profile conventions > exemplar
   habits. Where a profile row conflicts with a zero-tolerance house rule
   (G1-G15, D1-D6, S-EXP-7/8), the house rule wins and the profile row is
   applied in its house-compatible form (noted per row below).

Evidence base: 10 TPAMI/TIP full papers + ~60 award papers (CVPR/ICCV/NeurIPS/
ICML/ICLR/AAAI 2021-2026) re-read 2026-07-18; distilled notes in
`local/corpus_notes_20260718.md` (machine-local). Mechanics verified against
official author pages on 2026-07-18; re-verify after 12 months.

---

## 1. Template mechanics (operational; check at Stage 0 and at every compile gate)

### Profile J — top journal (TPAMI, TIP, IJCV-class)
| Item | Value |
|---|---|
| LaTeX class | IEEEtran (v1.8b+); journal option |
| Columns | 2 (double column, 10 pt) |
| Page cap | TIP: 13 dc pages initial / 16 revision (all-inclusive). TPAMI: 12 standard, up to 18 with overlength charges (incl. references and bios). See `core/templates/ieee-facts.md` for sources |
| Abstract | TIP: 150-250 words measured (`wordcount_abstract.sh`); self-contained |
| References | count toward the page cap |
| Anonymization | single-anonymized: do NOT anonymize |
| Extras | optional graphical abstract (TIP); supplementary ≤6 dc pages (TIP) |

### Profile C — top conference (per-venue mechanics)
| Venue | Style file / kit | Submission cap (main) | Columns | Not counted | Extras |
|---|---|---|---|---|---|
| CVPR / ICCV | CVF author kit, `cvpr.sty` (`\usepackage[review]{cvpr}` adds line numbers + anonymity) | 8 pages incl. floats; over → rejected without review | 2 | cited references only | supplementary PDF |
| NeurIPS | `neurips_<year>.sty` | 9 content pages | 1 | references, checklist, technical appendices | mandatory paper checklist |
| ICML | `icml<year>` style (LaTeX only) | 8 pages (9 at camera-ready); over → auto-reject | 2 | references, impact statement, appendices | impact statement |
| ICLR | `iclr<year>` style (OpenReview) | 9 pages main text (10 at rebuttal/camera-ready) | 1 | references, appendix (reviewers need not read) | reproducibility statement customary |
| AAAI | `aaai<yy>.sty` author kit | 7 pages technical content | 2 | references + reproducibility checklist | reproducibility checklist |
- All Profile-C venues are double-blind at submission: anonymize authors,
  acknowledgments, self-citations ("the authors of [n]" form), and code links
  (anonymous repo). This REVERSES the journal no-anonymization default.
- ieee-write Stage 2 bootstraps the skeleton from the venue's official kit; do
  not hand-roll a lookalike preamble. If the kit is not installed locally, ask
  the user for the kit path or approval to download it.

---

## 2. Structure and length allocation

| Axis | Profile J | Profile C |
|---|---|---|
| Skeleton | I Intro → II Related Work (2-3 thematic subsections, critique+pivot each) → III Method → IV Experiments (35-48% of body) → V Conclusion | Free: related work may sit early, after method, late, or be replaced by a positioning/capability table; Limitations subsection normal; Applications may be a chapter |
| Roadmap paragraphs | Mandatory: intro end + method head + experiments head preview their subsection order | Usually absent; bold run-in headers navigate instead |
| Intro | 5-10 paragraphs, funnel, paragraph-final "However," gap sentences; contributions 3-4 items; \IEEEPARstart | ~1-1.5 pages; gap → proposal → contribution bullets (2-4, may embed key delta numbers); a precisely-scoped first-ness claim is acceptable ("the first to X", X narrow and checkable) |
| Method opening | 2-4 sentence pure roadmap (no motivation restatement) | Same, or background section pre-loading notation so method reads as substitutions |
| Cost/efficiency | Mandatory, LAST experiments unit: hardware named, absolute per-item time, deployment close | Efficiency column/multiples embedded in the main table ("9× faster"); dedicated cost table optional |
| Extension disclosure | A journal paper extending a conference version discloses the version and enumerates the deltas ("A preliminary version appears in [n]. The extensions are as follows. First, ...") | n/a |
| Conclusion | Single tight paragraph (S-CON) | May merge with limitations ("Conclusion and limitations") |

## 3. Abstract mode

| Axis | Profile J | Profile C |
|---|---|---|
| Length | 150-250 words measured (target 230-250) | 130-215 words typical; obey venue form |
| Skeleton | S-ABS-1 limitation-then-solution skeleton, mandatory | Context → gap → propose/NAME → mechanism one-liner → evidence close; discovery variant adds a strength-adverb central-finding sentence ("Crucially, we find ...") |
| Numbers | Optional and claim-tied: most published TIP/TPAMI method abstracts carry zero numbers; a numeric close appears when the claim IS a number (efficiency/improvement papers). One clean headline number max; never per-dataset enumeration | Compressed forms only: ranges ("25-75%"), multiples ("32× fewer"), averages with declared aggregation ("averages of 18.5%"); or zero numbers deferring to tables |
| Links | No code links in the abstract (footnote/end) | Code/project link in abstract or page 1 is customary |

## 4. Figures

| Axis | Profile J | Profile C |
|---|---|---|
| Page-1 figure | TPAMI: page 1 usually text-only; motivation/phenomenon figures land on pages 2-3 BEFORE any method figure. TIP: an early conceptual figure (page 1-2) is standard and its mode is free (failure-mechanism, performance scatter with labeled coordinates, paradigm ladder ending in ours) | Teaser near-mandatory (CVF/AAAI). Four modes: capability input→output; qualitative wall; failure-mechanism/paradigm contrast; performance scatter. Full-width above abstract, or right column beside it |
| Overview figure | Double-column, page-top, 30-45% page height; caption: noun-phrase locator → First/Then/Finally walk → optional takeaway | Same, but caption additionally carries the conclusion (see captions row) |
| Captions | Short (1-2 sentences); heavy semantics (color codes, box meanings) live in body prose | Self-contained mini-abstract: bold lead (often method name), reading instructions, CONCLUSION sentence, numbers allowed |
| Evidence figures | Diagnostic panels, confusion matrices (per-class instrument), parameter sweeps | Diagnostic figure in the METHOD section justifying a design choice (power-spectrum → K=16 pattern); trade-off scatter with log axis, own-method distinct marker, corner cues ("best"/"fastest"); limitation/failure-example figures acceptable |
| Error bars | Declare the interval type in caption; house FIG rules apply | Declare once, centrally, then never repeat ("Error bars ... twice the standard deviation over 5 test sets"); omit rather than fake when runs are deterministic |
| Both profiles | FIG-1..FIG-8 house standards (vector/300dpi, no in-figure titles, colorblind-safe palette, serif typeface, print-legible sizes, unoccluded legends, (a)/(b) below subplot, real data only) | same |

## 5. Tables

| Axis | Profile J | Profile C |
|---|---|---|
| Semantics | bold = best, underline = second best, †/‡ protocol footnotes, ↑/↓ metric direction in headers; every convention declared in the caption | Same base; plus tolerated extras: gray main-metric column, colored best/second text, capability ✓/✗ matrix, per-cell relative gains, full rank heatmap |
| Background color | Grayscale-safe ceiling: P1 own-row pale tint (color = "which row is ours" ONLY; best/second/significant stay with bold/underline/dagger; zero information lost on decolor). P2 red/blue best-cell fills are BANNED (grayscale-unsafe, fights bold/underline) | Shading tolerated up to full heatmaps; still prefer P1 + declared semantics; heatmaps do not transfer to a journal resubmission |
| Summary devices | Wins/ties Count row; Δ or Gain column vs best baseline (define in caption) | Same, widely used (Informer Count row; Δ% columns) |
| Group structure | datasets as top-level column groups with metric sub-columns; own rows below a rule; anchor rows (random/human/oracle) where they add a scale | Same + family/backbone group-header rows; ‡ concurrent-work markers; ghost lower-bound rows |
| Failure cells | "-"/"N/A - no results reported." footnote; distinguish causes honestly (OOM vs unacceptable) | same |
| Ablation form | per-component rows; delta framed so positive = component helps (S-EXP-9) | config-ladder ("+component" cumulative rows, Δ column) equally standard |
| Text color | Secondary semantics only, re-declared per caption (red = gains rows, gray = reproduced/degraded, blue = significant p-values); the same color may carry different meanings in different tables ONLY because each caption re-declares | same, plus colored best/second text tolerated |
| Stats-forward device | p-value bottom row: paired-test p between the top-2 (bold and underlined) methods per column, significant values highlighted and declared | rare; CIs/error bars live in figures |
| Method-row tags | competitor rows carry venue+year tags ("PROSER (CVPR'21)") or a Pub. column | same |

## 6. Claim register, statistics, and disclosure

| Axis | Profile J | Profile C |
|---|---|---|
| Statistics | mean±σ / CI culture; significance ONLY on the pre-declared primary metric under the stated test (S-EXP-7); paired-difference CIs for tie claims | CVF: typically no CI/tests, relative-percent chains; NeurIPS/ICML discovery: declared-once error bars + robustness-knob statements; RL/eval subculture follows Statistical-Precipice prescriptions (stratified bootstrap CI, IQM, CI-of-difference). Whatever the paper adopts must be internally consistent; S-EXP-7 still governs the word "significant" |
| Claim verbs | observe/find → indicate → suggest → hypothesize; confirm only for pre-stated predictions; strength adverbs (consistently/substantially) only with full-table evidence | same ladder, plus: "supports" for hypotheses vs "confirms" for predictions; "consistent with" reserved for external prior work; believe/expect only in forward-looking sentences |
| Questions | Avoid; statements only. At most 1 quoted+numbered intro research question when the whole paper answers that question | Live device: self-answered intro pivot, question section headings, Q&A analysis paragraph heads. Budget stays small; every question must be explicitly answered |
| Limitations | House D1-D6 unchanged: no weakness inventory; scope one-liner max; ties resolved positively with real numbers | An explicit Limitations subsection is the venue norm (checklist culture). House-compatible form: limitations listed are OUTSIDE the main claim's evaluation envelope (adjacent regimes, cost, scope), each paired with a mechanism or forward path; never protocol self-doubt, never hedging the headline claim. Gap positivization: "While there is still a large gap ..., we believe future work can bridge this using X as a backbone" |
| First-ness | Avoid "for the first time"; carry priority structurally | Acceptable when narrowly scoped and checkable; prefer structural priority |
| Emphasis budget | Tiny: bold = acronym first-mention/dataset names/run-in labels/key numbers; italic = term first-use; ≤2 free emphases per page | Bold verdict-style paragraph headers and italic full-clause claims are routine; run-in bold headers are the primary navigation |

## 7. Cross-venue universals (enforce everywhere; already house rules where cited)
1. Caption declares every convention used (bold/underline/arrows/daggers/shading).
2. Every prose number carries its comparator and condition; efficiency as
   multiples, accuracy as absolute deltas; honest modifiers (at most, up to,
   approximately) keep single values true (G7).
3. Losses/ties: state flat, one hedged causal clause, convert to a boundary
   condition or scoped strength; never defensive (D1/D2, S-EXP-11).
4. Phenomenon naming: name once, early, typographically marked, operationalize
   within a paragraph (measurable handle), then use as a plain term.
5. Mirrored enumeration: numbered limitations ↔ numbered design answers ↔
   per-component ablation units; no orphan lists.
6. Fairness sentences written into the caption or protocol paragraph ("under
   identical hyperparameters", "while keeping X fixed", parameter budgets).
7. Verify-then-write: all counts and page numbers from the scripts (V1-V6).

## 8. Profile hooks for the review/style workflows
- ieee-review personas calibrate to the target: R-EIC reads as "senior
  associate editor of the target journal" (Profile J) or "senior area chair of
  the target conference" (Profile C); rubric hard-check #3 (abstract word
  count) and #4 (page cap) take their numbers from THIS file's mechanics
  tables for the chosen venue.
- ieee-style audits each dimension against the chosen profile's rows and cites
  the row violated (e.g., "VP §4 teaser: journal profile accepts no-teaser;
  for CVPR add a page-1 teaser").
