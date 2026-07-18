<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->
<!-- Paste the block below into the AGENTS.md of a project (or the global
     ~/.codex/AGENTS.md) to make the IEEE Paper Suite available to Codex.
     Replace {{IEEE_SKILL_ROOT}} with the absolute path of the suite
     (install.sh --codex does the replacement automatically). -->

## IEEE Paper Suite

Three paper workflows are available from the IEEE Paper Suite installed at
`{{IEEE_SKILL_ROOT}}`:

- **ieee-write**: write an IEEE journal paper from the codebase. Entry:
  read `{{IEEE_SKILL_ROOT}}/skills/ieee-write/SKILL.md` in full and follow
  the stages exactly.
- **ieee-polish**: paragraph-by-paragraph line editing under the house
  rules. Entry: read `{{IEEE_SKILL_ROOT}}/skills/ieee-polish/SKILL.md` in
  full and follow the stages exactly.
- **ieee-review**: simulated five-persona peer review plus house audit.
  Entry: read `{{IEEE_SKILL_ROOT}}/skills/ieee-review/SKILL.md` in full and
  follow the stages exactly.

Rules for any of the three: the suite root referenced as `<suite>` inside
the SKILL files is `{{IEEE_SKILL_ROOT}}`. Read every core file the SKILL
names IN FULL before acting. Personas may be executed serially. All user
gates (outline approval, per-paragraph go) are mandatory: propose, wait for
explicit approval, then act.
