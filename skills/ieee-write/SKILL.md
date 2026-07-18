---
name: ieee-write
description: Write a top-journal or top-conference paper from a codebase, outline-first with hard user gates and venue-targeted style (journal -> TPAMI/TIP profile; conference -> CVPR/ICCV/NeurIPS/ICML/ICLR/AAAI profile). Use when the user asks to write, start, or draft a paper from their project for a top venue, or invokes /ieee-write. Scans the project, produces an outline for approval, then drafts paragraph by paragraph (Method, Experiments, Related Work, Introduction, Abstract, Conclusion) with per-paragraph user approval.
license: CC BY-NC 4.0, (c) 2026 Lan Zhang
---

# ieee-write: Codebase to Top-Venue Manuscript

You are running the writing workflow of the IEEE Paper Suite. The suite is
venue-target driven: the target venue's profile decides structure, figures,
tables, and register. Follow the stages below IN ORDER. Every stage names the
core files to read: read each named file IN FULL before acting on that stage.
Never rely on a remembered summary of a rules file.

## Stage 0: Locate the suite, the project, and the target venue
1. Resolve the suite root: run `readlink -f` on this skill's directory; the
   suite root is two levels up from the resolved path (the directory
   containing `core/` and `scripts/`).
2. Confirm with the user: the paper project root (default: current
   directory), the output directory (default: `<project>/paper/`), and the
   **submission target**: journal or conference, plus the specific venue.
   If the user has not stated a target, ask once; if still undecided, use
   journal-TPAMI/TIP as the safe default and state the assumed profile in
   every deliverable.
3. Read `<suite>/core/literature/venue-style-profiles.md` IN FULL and load
   the profile matching the target (Profile J or Profile C plus the venue's
   mechanics row). The profile governs page caps, abstract mode, teaser and
   caption conventions, table color ceiling, claim register, limitations
   handling, and anonymization. House rules in `core/rules/` always win over
   profile rows.
4. If `<suite>/local/config.md` exists, read the config for a golden-sample
   path and other local pointers. Never copy content from an unpublished
   golden sample into any deliverable.
5. Read `<suite>/core/rules/workflow-gates.md` and
   `<suite>/core/templates/ieee-facts.md` now. The gates in the former bind
   the whole run; the latter holds the journal-side authoritative numbers.

## Stage 1: Scan the project into a fact sheet
Survey the project exhaustively: code, configs, results files, logs, data
manifests, README/plan documents. Produce `paper/FACT_SHEET.md` recording:
the method as implemented (modules, losses, inputs), every experimental
setting, and every result number WITH the file path each number came from.
Rules: numbers come only from real files or command output; anything not yet
measurable is written as `TBD`, never invented (V4 of
`core/rules/verification-protocol.md`).

## Stage 2: Outline (hard gate)
First, unless the user has already stated a preference, ask ONE setup
question: use an existing prepared .tex template (ask for the path), or
bootstrap the manuscript skeleton from scratch? Skip the question entirely
when the user has already made the choice explicit. When bootstrapping,
build the skeleton from the TARGET VENUE's template per the profile's
mechanics table (journal: IEEEtran per `core/templates/ieee-facts.md`;
conference: the venue's official kit, e.g. cvpr.sty / neurips_<year>.sty /
icml<year> / iclr<year> / aaai<yy>.sty, with the venue's anonymization
mode). Never hand-roll a lookalike preamble; if the kit is missing locally,
ask the user for the kit path or approval to fetch it.

Read `<suite>/core/templates/outline-template.md` and
`<suite>/core/templates/exemplar-patterns.md`. Produce `paper/OUTLINE.md`
per the template: title candidates, per-paragraph plan for every section,
floats plan, main-figure drawing suggestions (the USER draws all figures and
places the files at the agreed paths; you only specify content and
constraints), literature plan, open items.

**GATE:** present the outline and iterate on feedback. Only an explicit user
statement that the outline review has passed unlocks Stage 3. Record the
approval in `paper/OUTLINE.md`.

## Stage 3: Draft paragraph by paragraph (hard gate per paragraph)
Fixed drafting order: **Method, then Experiments, then Related Work, then
Introduction, then Abstract, then Conclusion.**

Before each section, read `<suite>/core/rules/prose-rules.md`,
`<suite>/core/rules/disclosure-policy.md`, the section's rules file
(`section-methodology.md`, `section-experiments.md`,
`section-related-work.md`, `section-introduction.md`,
`section-abstract.md`, `section-conclusion.md`), and consult
`<suite>/core/templates/exemplar-patterns.md` and
`<suite>/core/templates/applied-examples.md` for phrasing.

Grounding rules for the two evidence-bearing chapters:
- **Method chapter = the code base's truth.** Every mechanism described must
  match what the scanned code actually implements, as recorded in
  `paper/FACT_SHEET.md`. Never describe an idealized design the code does
  not contain; if design and code diverge, surface the divergence to the
  user instead of papering over the divergence.
- **Experiments chapter = real data only.** Every number comes from a fact
  sheet entry with file provenance; anything unmeasured stays `TBD` and the
  paragraph waits. When a paragraph needs a plot, generate the figure per
  `<suite>/core/rules/figure-standards.md` (300 dpi minimum, no in-figure
  titles, scientific palette, Times New Roman, print-legible sizes,
  unoccluded legends, (a)/(b) labels centered below each subplot) from real
  result files, and show the rendered figure to the user with the
  paragraph.

Per paragraph:
1. Draft the paragraph per the outline's plan for that paragraph.
2. Self-check sentence by sentence against the global rules and the section
   rules; state which checks were applied.
3. Present the paragraph to the user with a one-line note of any rule
   tensions.
4. **GATE:** wait for an explicit `go` before writing the paragraph into the
   .tex and before starting the next paragraph. One paragraph per cycle,
   no exceptions.

Citations: before citing, verify per `<suite>/core/rules/citations-policy.md`
(run `<suite>/scripts/verify_citations.py`; tiers in
`<suite>/core/literature/venue-tiers.md`). Unverified needs get the red
`[CITE: description]` placeholder, never an invented reference.

## Stage 4: Section verification
At each section boundary run `<suite>/scripts/verify_tex.sh` on the
manuscript and report pages/warnings/undefined/Overfull verbatim. For the
abstract, run `<suite>/scripts/wordcount_abstract.sh` on every version and
report the measured count.

## Stage 5: Handoff
When all sections are approved: run `<suite>/scripts/sweep_prose.sh`, report
counts, list open items ([CITE:] placeholders, TBD numbers, figures the user
still owes), and **proactively offer a full polishing pass** (the ieee-polish
workflow). Do not start polishing without the user's acceptance.
