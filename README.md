# IEEE Paper Suite

Write, polish, and review an evidence-grounded manuscript for IEEE journals and for top conferences (CVPR/ICCV, NeurIPS, ICML, ICLR, AAAI). Start from a blank document or from the exact paragraph you need. The suite is model-agnostic Markdown: it states the rules, the file each rule lives in, and the checks that make them visible.

[中文说明](README.zh-CN.md) · [CC BY-NC 4.0](LICENSE)

## Choose the task

| Entry | Use it for | Editing behavior |
| --- | --- | --- |
| `ieee-write` | A new paper, a section draft, an argument reconstruction | Completes the requested draft; respects explicit proposal/outline gates |
| `ieee-polish` | Clearer academic English, stronger paragraphs, a revision round | Applies within the authorization given; proposal-only when asked |
| `ieee-review` | Scientific claims, method, protocol, evidence, positioning | Manuscript sources stay read-only; produces a scoped report |
| `ieee-style` | Structure, sentences, terminology, figures, target formatting | Manuscript sources stay read-only; produces a scoped report |

No compulsory paragraph-by-paragraph "go". Review granularity follows the user; paragraph architecture stays rigorous. A small task gets a short work card, not a new documentation package. Unknown venues, missing tools and local evidence gaps are reported explicitly while useful independent work continues.

## Use now

Point a file-capable agent at the matching `skills/ieee-*/SKILL.md`. Installed Codex skills answer to `$ieee-write`; Claude Code answers to `/ieee-write`. [Generic setup](adapters/generic/QUICKSTART.md).

```text
Use ieee-polish. Revise only Sec. 5.2. Keep the numbers and the comparison scope.
Show each paragraph as a proposal with its reason; apply after I approve.
```

```text
Use ieee-write. The method notes and the final results are in this project.
Draft the journal paper from the active main.tex and the existing storyline; no number changes.
```

```text
Use ieee-style. Audit Related Work: each subsection's second paragraph and the positioning logic. Propose, do not edit.
```

The agent loads [the shared workflow](core/WORKFLOW.md) and the **full rule set for the requested unit**, not everything for every request. [One-page checklist](QUICK_REFERENCE.md) · [sentence-plan index](core/templates/sentence-plan.md) · [workspace](core/templates/writing-workspace.md).

## What the rules cover

Nine shared rule files sit under `core/rules/`; each section blueprint ends with a hardened checklist distilled from rejected drafts.

| Concern | Rule file |
| --- | --- |
| Selling the work, positive framing, claim scope, sensitive applications | [voice-and-positioning.md](core/rules/voice-and-positioning.md) |
| One argument per paragraph, governing first sentence, analysis after each observation, endings | [paragraph-architecture.md](core/rules/paragraph-architecture.md) |
| Information order, true connectives, repetition control, referents, punctuation | [sentence-craft.md](core/rules/sentence-craft.md) |
| Word register, banned forms, replacements | [lexicon.md](core/rules/lexicon.md) |
| Writing English instead of translating Chinese; the eight structures behind bad English | [translation-discipline.md](core/rules/translation-discipline.md) |
| Revision scope, preservation list, check order, self-review | [revising.md](core/rules/revising.md) |
| Simulated review, real reader feedback, multi-pass read-through, review pages | [review-loops.md](core/rules/review-loops.md) |
| Terms, abbreviations, symbols, formulas | [terminology-and-notation.md](core/rules/terminology-and-notation.md) |
| Page budget, spacing, orphans, TeX and PDF hygiene | [layout-and-build.md](core/rules/layout-and-build.md) |

Section blueprints: [Abstract A1–A9](core/rules/section-abstract.md) · [Introduction P1–P8](core/rules/section-introduction.md) · [Related Work](core/rules/section-related-work.md) · [Method](core/rules/section-methodology.md) · [Experiments E1–E6](core/rules/section-experiments.md) · [Conclusion](core/rules/section-conclusion.md). Evidence and permission: [evidence-and-claims.md](core/rules/evidence-and-claims.md), [citations-policy.md](core/rules/citations-policy.md), [workflow-gates.md](core/rules/workflow-gates.md). Figures: [figure-standards.md](core/rules/figure-standards.md).

## Checks you can run

Dependency-free Python 3, no network:

```bash
python3 scripts/prose_lint.py main.tex --quiet        # H must be 0; then read the S list
python3 scripts/pronoun_check.py main.tex --quiet     # referents for this/these/it/its/...
python3 scripts/review_page.py round.json -o round.html   # approve/comment page, exports JSON
```

`prose_lint.py` reports Chinese-origin structures, paired cause-effect connectives, participial openers, banned vocabulary, colons in prose, a connective twice per paragraph, repeated phrases, long sentences and absolutes. It also prints the most repeated content words of each file. H = hard fault (rewrite), S = review, I = prompt for the manual reading tests. Captions are always scanned; `--include-floats` also scans float bodies; `--banned file` adds a project word list.

`review_page.py` turns a round of proposals into one offline HTML page: original, proposed (word-diffed), reason, approve control, comment box, optional variants, local persistence, JSON export. It implements the loop in [review-loops.md](core/rules/review-loops.md) §RL4.

Bash helpers stay available: `sweep_prose.sh`, `wordcount_abstract.sh`, `check_figures_text.sh`, `verify_tex.sh`, `leak_scan.sh`, `verify_citations.py`. They are diagnostics: a zero count is not proof of correctness, and a hit needs context. Scope and limits: [verification-protocol.md](core/rules/verification-protocol.md).

## Install

```bash
./install.sh            # Claude skill links
./install.sh --codex    # Codex skill links, legacy prompts, optional AGENTS snippet
./install.sh --all      # both
./install.sh --check    # self-test: links, scripts, rule-file references
```

Installation never edits project or global AGENTS files and preserves unrelated skill directories. Start a fresh host session if its skill list is cached. `local/config.md` holds private machine pointers only; the target, paths and authorization belong to the session or the project. A project may extend the lexicon with `--banned`.

Basic prose work needs file access, not a TeX toolchain. Optional verification uses Python 3, Bash/GNU tools, pdfLaTeX+BibTeX (only the build helper) and Poppler; citation lookup needs network. Follow the project's existing engine: missing tools give a useful draft with explicit pending checks.

## What the profile enforces

- Abstract A1–A9 and Introduction P1–P8 with sentence-level tasks and real motivation chains.
- Related Work: two paragraphs per theme; the positioning paragraph 2–3 sentences, 35–65 words, never longer than the first.
- Method: headings, figure nodes, symbols, axes, equations, inputs/outputs and training/inference state agree.
- Experiments: every paragraph topic-first, results explained operationally (E1–E6), counterevidence kept, inference bounded.
- Revision: the claim, the numbers and the comparator survive; length does not grow unless asked; every round closes with what was applied, rejected and left open.

These are house defaults for journal method papers. Actual research content and the current official venue, article-type and stage requirements constrain them. No invented results, citations, modules, statistical equivalence, experiments or false external review. Theory, application, system and conference tasks adapt their own evidence and format; no blanket page cap, tier-only citation gate or mandatory diagnostic figure.

## Acknowledgments and license

Sincere thanks to Prof. Xiankai Lu of Shandong University for his guidance and support.

© 2026 Lan Zhang · [CC BY-NC 4.0](LICENSE) · non-commercial use only; attribution required.
