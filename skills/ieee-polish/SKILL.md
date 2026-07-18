---
name: ieee-polish
description: Paragraph-by-paragraph polishing of an IEEE manuscript to idiomatic academic English under hard house rules, with per-paragraph user approval. Use when the user asks to polish, line-edit, or improve the English of a .tex manuscript (written by this suite or not), or invokes /ieee-polish. Proposes original-to-new edits per paragraph and applies nothing without an explicit go.
license: CC BY-NC 4.0, (c) 2026 Lan Zhang
---

# ieee-polish: Gated Line-Edit Pass

You are running the polishing workflow of the IEEE Paper Suite. The workflow
edits NOTHING without an explicit per-paragraph approval.

## Stage 0: Locate and set up
1. Resolve the suite root: run `readlink -f` on this skill's directory; the
   suite root is two levels up from the resolved path.
2. Identify the target .tex with the user, and the scope (whole manuscript
   or named sections).
3. Read IN FULL: `<suite>/core/rules/workflow-gates.md`,
   `<suite>/core/rules/prose-rules.md`,
   `<suite>/core/rules/disclosure-policy.md`, and
   `<suite>/core/rules/verification-protocol.md`.

## Stage 1: Baseline
1. Run `<suite>/scripts/verify_tex.sh <main.tex>` once to store the
   compilation baseline (pages, warnings, Overfull signatures). Later runs
   attribute every box to NEW or LEGACY; never report a legacy artifact as a
   new regression.
2. Read the whole manuscript once. Build a section map and a terminology
   list (established phrases, module names, metric names). During polishing,
   conform to established terms; grep the manuscript before proposing any
   rename, and check figures with
   `<suite>/scripts/check_figures_text.sh <figdir> <term>` before renaming a
   term that might appear inside a figure.

## Stage 2: Polish loop (one paragraph per cycle, hard gate)
Work top to bottom. For each paragraph:
1. Read the section rules file for the current section
   (`section-abstract.md` / `section-introduction.md` /
   `section-related-work.md` / `section-methodology.md` /
   `section-experiments.md` / `section-conclusion.md`) if not already read
   in this session.
2. Analyze sentence by sentence against the global rules (G1-G15), the
   section rules, and the disclosure policy. Consult
   `<suite>/core/templates/applied-examples.md` for the proposal format.
3. Present a proposal table: one row per changed sentence,
   `original -> proposed`, with the motivating rule ID per row. Propose
   only; do not edit.
4. **GATE:** wait for the user's explicit `go` (or amended instructions,
   then re-propose). Apply the approved edits exactly.
5. After applying, re-read the edited region and confirm the new text is in
   place (editor-buffer guard in `workflow-gates.md`). If old text
   reappears, stop and follow the guard procedure.
6. For the abstract, run `<suite>/scripts/wordcount_abstract.sh` after every
   applied change and report the measured count.

Compile checkpoints: at each section boundary (and after any structural
edit) run `<suite>/scripts/verify_tex.sh` and report
pages/warnings/undefined/Overfull with NEW/LEGACY attribution, verbatim.

## Stage 3: Final sweep
After the last approved paragraph:
1. Run `<suite>/scripts/sweep_prose.sh <main.tex>` and report every count
   with locations. Zero-tolerance rules must show zero; walk any residue
   back into the loop.
2. Run a final `<suite>/scripts/verify_tex.sh` and report the full
   compilation summary against the baseline.
3. Deliver a change log: paragraphs touched, rules most frequently applied,
   and any user-declined proposals (recorded, not re-argued).
