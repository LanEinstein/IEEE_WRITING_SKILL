<div align="center">

# IEEE Paper Suite

**Write, polish, review, and style-audit top-journal and top-conference manuscripts<br>with venue-targeted, hard-gated, single-source-of-truth workflows.**

<br>

[![English](https://img.shields.io/badge/English-README-2ea44f?style=for-the-badge)](README.md)
[![Chinese](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A3-1f6feb?style=for-the-badge)](README.zh-CN.md)

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-ready-d97757.svg)](#installation-and-usage)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-ready-412991.svg)](#installation-and-usage)
[![Model Agnostic](https://img.shields.io/badge/core-model--agnostic-8a2be2.svg)](adapters/generic/QUICKSTART.md)

</div>

---

## Background

Generic AI writing tools produce papers that read as machine-generated and
fall short of top-venue language standards. The gap is not the model; the
gap is the missing craft: the rules a senior author enforces during real
revision rounds. The suite freezes that craft, distilled from
paragraph-by-paragraph revision of an IEEE Transactions manuscript, from a
section-by-section analysis of ten published TPAMI/TIP papers, and from a
main-body read of ~60 best/outstanding papers at CVPR, ICCV, NeurIPS, ICML,
ICLR, and AAAI (2021-2026), into a single-source rule library and
hard-gated workflows that no step can skip. Every workflow is
venue-targeted: a journal target loads the TPAMI/TIP profile, a conference
target loads the matching conference profile, and structure, figures,
tables, and register follow the target rather than a fixed IEEE default.

## Features

| Workflow | What it does | Hard gate |
|:--|:--|:--|
| **`/ieee-write`** | Scans your codebase into a fact sheet, delivers an outline, then drafts paragraph by paragraph (Method, Experiments, Related Work, Introduction, Abstract, Conclusion) | Outline approval, then an explicit `go` per paragraph |
| **`/ieee-polish`** | Line-edits any `.tex` against the house rules, one paragraph at a time, as `original -> proposed` tables | Nothing is applied without your `go` |
| **`/ieee-review`** | Five-persona simulated peer review (editor/area chair, methodology, domain, writing, devil's advocate) plus an author-only compliance audit, with a decision estimate | Read-only by design |
| **`/ieee-style`** | Venue-targeted full-manuscript style-conformance review: structure, abstract mode, register, figures, tables, teaser, captions, page/template compliance, judged against the target venue's profile | Read-only by design |

What makes the suite different:

- **Venue-targeted, not venue-fixed.** Every workflow confirms the
  submission target in Stage 0 and loads the matching style profile
  (`core/literature/venue-style-profiles.md`): template and page caps,
  structure ratios, abstract mode, teaser and caption conventions, table
  color ceilings, claim register, and limitations handling all follow the
  target venue.
- **A single-source rule library.** Global prose rules, per-section rules
  (abstract through conclusion), disclosure policy, citation policy,
  figure standards, venue profiles, and a verification protocol live in
  `core/` as the only authority; workflows read the files whole, so rules
  cannot drift.
- **Everything measured, nothing invented.** Word counts, page limits,
  compile health, and zero-tolerance style sweeps come from scripts with
  verbatim counts. Citations are verified against live indexes (Crossref,
  OpenAlex) with a venue-tier gate and arXiv interception.
- **A review panel that pushes back.** Paper-blind pre-commitment,
  anti-sycophancy rules for the devil's advocate, severity-ranked findings
  with quoted evidence, and a calibrated decision estimate.
- **Model-agnostic core.** Plain markdown and scripts; adapters ship for
  Claude Code and Codex, and any agent that reads files and runs commands
  can drive the suite.

## Installation and Usage

```bash
git clone git@github.com:LanEinstein/IEEE_WRITING_SKILL.git ieee-paper-suite
cd ieee-paper-suite
./install.sh            # Claude Code (symlinks into ~/.claude/skills/)
./install.sh --codex    # Codex CLI (slash prompts + AGENTS.md snippet)
./install.sh --all      # both
```

Then invoke `/ieee-write`, `/ieee-polish`, `/ieee-review`, or `/ieee-style`
inside your paper project. Requirements: `pdflatex`, `bibtex`, `pdftotext`,
standard POSIX tools, and Python 3 with network access for citation
verification.

## Directory Structure

```
skills/     Entry points: ieee-write, ieee-polish, ieee-review, ieee-style
core/       Single-source authority: rules/, templates/, review/, literature/
            (incl. venue-style-profiles.md, the journal/conference profiles)
scripts/    verify_tex, sweep_prose, wordcount_abstract, check_figures_text,
            verify_citations, leak_scan
adapters/   codex/ (prompts + AGENTS snippet), generic/ (any-agent quickstart)
local/      Machine-local config (gitignored except the example)
```

## Acknowledgments

Sincere thanks to Prof. Xiankai Lu of Shandong University for his guidance
and support.

## License

<div align="center">

© Lan Zhang · [CC BY-NC 4.0](LICENSE) · non-commercial use only · attribution required

</div>
