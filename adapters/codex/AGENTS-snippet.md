<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# IEEE Paper Suite

The suite is installed at `{{IEEE_SKILL_ROOT}}`. Choose only the requested workflow:

- **ieee-write:** read `{{IEEE_SKILL_ROOT}}/skills/ieee-write/SKILL.md` for new manuscript/section drafting.
- **ieee-polish:** read `{{IEEE_SKILL_ROOT}}/skills/ieee-polish/SKILL.md` for scoped prose improvement.
- **ieee-review:** read `{{IEEE_SKILL_ROOT}}/skills/ieee-review/SKILL.md` for scientific review.
- **ieee-style:** read `{{IEEE_SKILL_ROOT}}/skills/ieee-style/SKILL.md` for structure/style/format audit.

The selected entry routes to `core/WORKFLOW.md` and the full relevant section blueprint. Follow the current user's review/apply scope; no mandatory per-paragraph go. Reuse the actual active manuscript and project records. Scientific accuracy and current official target requirements constrain house conventions. Unknown target rules remain pending. Review/style preserve manuscript sources and original build artifacts; requested reports are allowed in the agreed area. Independent models are used only when available and authorized.

This snippet makes the suite discoverable; it does not authorize source edits or external actions and does not replace project-specific instructions. Do not reactivate historical handoff or staging-file workflows.

Shared rules for this project (`{{IEEE_SKILL_ROOT}}/core/rules/`): paragraph-architecture, sentence-craft, lexicon, translation-discipline, voice-and-positioning, terminology-and-notation, revising, review-loops, layout-and-build, figure-standards. One-page digest: `{{IEEE_SKILL_ROOT}}/QUICK_REFERENCE.md`. Section blueprints end with a hardened checklist `S-*-H`. Before delivering English prose, run `python3 {{IEEE_SKILL_ROOT}}/scripts/prose_lint.py FILE.tex --quiet` (H = 0) and `python3 {{IEEE_SKILL_ROOT}}/scripts/pronoun_check.py FILE.tex`; report the counts and every S hit you kept, with the reason.
