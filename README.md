# IEEE Paper Suite

**English** | [简体中文](README.zh-CN.md)

Three independently invokable workflows that take a research codebase to an
IEEE top-journal manuscript in idiomatic academic English: **ieee-write**,
**ieee-polish**, and **ieee-review**.

## Background

Generic AI writing tools produce papers that read as machine-generated and
fall short of top-journal language standards. The gap is not the model; the
gap is the missing craft: the rules a senior author enforces during real
revision rounds. The suite freezes that craft, distilled from
paragraph-by-paragraph revision of an IEEE Transactions manuscript and from
a section-by-section analysis of five published IEEE TIP papers, into a
single-source rule library and hard-gated workflows that no step can skip.

## Features and What Makes the Suite Different

- **Three independent workflows.** Writing, polishing, and review are
  separate entry points, never one bundled pipeline.
- **A single-source rule library.** Global prose rules, per-section rules
  (abstract through conclusion), disclosure policy, citation policy, and a
  verification protocol live in `core/` as the only authority; workflows
  read the files whole, so rules cannot drift out of sync.
- **Hard user gates.** Outline approval before drafting, an explicit `go`
  per paragraph, propose-before-edit polishing. The model never edits a
  manuscript on its own judgment.
- **Everything measured, nothing invented.** Word counts, page limits,
  compile health, and zero-tolerance style sweeps come from scripts with
  verbatim counts. Citations are verified against live indexes (Crossref,
  OpenAlex) with a venue-tier gate and arXiv interception; a reference that
  cannot be verified cannot be cited.
- **A review panel that pushes back.** Five personas (editor, methodology,
  domain, writing, devil's advocate) with paper-blind pre-commitment,
  anti-sycophancy rules, a severity-ranked findings report, and a decision
  estimate, plus an author-only compliance audit layer.
- **Model-agnostic.** The core is plain markdown and scripts; adapters ship
  for Claude Code and Codex, and any agent that reads files and runs
  commands can drive the suite.

## Installation and Usage

```bash
git clone <repo-url> ieee-paper-suite
cd ieee-paper-suite
./install.sh            # Claude Code (symlinks into ~/.claude/skills/)
./install.sh --codex    # Codex CLI (slash prompts + AGENTS.md snippet)
./install.sh --all      # both
```

Then, in your paper project:

- `/ieee-write` starts from a codebase scan, delivers an outline for your
  approval, and drafts paragraph by paragraph (Method, Experiments, Related
  Work, Introduction, Abstract, Conclusion), waiting for your `go` at every
  paragraph.
- `/ieee-polish` line-edits any .tex (written by the suite or not),
  proposing original-to-new tables per paragraph and applying only what you
  approve.
- `/ieee-review` produces a two-layer report: a simulated five-persona peer
  review with a decision estimate, and an author-only compliance audit.

Requirements: `pdflatex`, `bibtex`, `pdftotext`, standard POSIX tools, and
Python 3 with network access for citation verification.

## Directory Structure

```
skills/     Entry points: ieee-write, ieee-polish, ieee-review (SKILL.md each)
core/       Single-source authority: rules/, templates/, review/, literature/
scripts/    verify_tex, sweep_prose, wordcount_abstract, check_figures_text,
            verify_citations, leak_scan
adapters/   codex/ (prompts + AGENTS snippet), generic/ (any-agent quickstart)
local/      Machine-local config (gitignored except the example)
```

## Acknowledgments

Sincere thanks to Prof. Xiankai Lu of Shandong University for his guidance
and support.

## License

© Lan Zhang. Licensed under [CC BY-NC 4.0](LICENSE): non-commercial use
only; redistribution and adaptation require attribution to the author
(Lan Zhang) and a statement of the source.
