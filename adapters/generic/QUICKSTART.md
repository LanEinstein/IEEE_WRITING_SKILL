<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Any-agent quick start

Give a file-capable agent the suite location and requested task:

> The IEEE Paper Suite is at `<absolute suite root>`. Read `skills/ieee-write/SKILL.md` there to draft, `ieee-polish` to revise prose, `ieee-review` to review science, or `ieee-style` to audit structure/style. Use my existing scope, active manuscript, and authorization. Load the shared workflow and the full section blueprint only for the requested unit.

The core is model-agnostic Markdown. Basic prose work needs no codebase, network, or compiler. Optional helpers have dependencies listed in [verification-protocol.md](../../core/rules/verification-protocol.md); use the actual project build engine. Missing tools yield useful content plus explicit pending checks, not a fabricated pass.

Do not force a new full-paper outline for an abstract edit or a go for each paragraph of an authorized section. Respect explicit proposal-only requests. Unknown venue stays provisional. Preserve truth, actual values, source/version boundaries, canonical terms, and important counterevidence. The selected journal-method profile retains concrete A/P/R/M/E/F/C functions; adapting scope does not remove those writing requirements.

Review sources remain unchanged; reports go to the agreed area and necessary builds run in an isolated copy. Review perspectives may run serially. A serial lens is not an independent agent or a Claude review; actual cross-model use must be available and authorized.

## If the task is revision rather than drafting

Read `core/rules/revising.md` and `core/checklists/polish-round.md`. One round = one unit with the author in the loop: exact original, exact replacement, one sentence of reason; apply only what was approved; re-read in context; close the round with what was applied, rejected and left open. For more than a handful of items, generate one page with `python3 scripts/review_page.py round.json -o round.html`, which gives an approve control and a comment box per item and exports the decisions as JSON.

## If the task is an audit

Read `core/checklists/pre-delivery.md` and the section's `S-*-H` checklist. Report locations, the rule each finding violates, and a concrete fix; do not call a house preference a venue requirement. `python3 scripts/prose_lint.py` and `python3 scripts/pronoun_check.py` give the mechanical part; read their H hits as faults and their S hits as candidates.

## If the manuscript is approaching submission

Read `core/checklists/submission.md` and `core/rules/layout-and-build.md`. Verify the current official requirements at source for this year and track, measure layout rather than estimating it, and confirm the shipped PDF contains the last approved sentence.
