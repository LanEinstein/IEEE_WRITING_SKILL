---
name: ieee-write
description: Draft an IEEE journal manuscript or a requested section from research materials, with sentence-level blueprints, evidence-linked claims, and mechanism-focused analysis. Use for starting a paper, drafting sections, or restructuring an argument; adapt other venues to their actual requirements.
license: CC BY-NC 4.0, (c) 2026 Lan Zhang
---

# ieee-write: research materials to a reviewable manuscript

Resolve `<suite>` by following this entry directory's symlink to its real path; the suite root contains `core/` two levels above. Read [core/WORKFLOW.md](../../core/WORKFLOW.md) once, then only the resources needed below. Read the relevant section rule file in full before drafting/reviewing that section; do not replace its sentence tables with a remembered summary. Current session authorization and project agreements govern editing; presentation size never creates permission. Scientific accuracy and current official requirements constrain every house preference.

The shared rule set under `core/rules/` is binding for the requested unit: [paragraph-architecture.md](../../core/rules/paragraph-architecture.md), [sentence-craft.md](../../core/rules/sentence-craft.md), [lexicon.md](../../core/rules/lexicon.md), [translation-discipline.md](../../core/rules/translation-discipline.md), [voice-and-positioning.md](../../core/rules/voice-and-positioning.md), [terminology-and-notation.md](../../core/rules/terminology-and-notation.md), [figure-standards.md](../../core/rules/figure-standards.md) and, where the text is revised, [revising.md](../../core/rules/revising.md) and [review-loops.md](../../core/rules/review-loops.md). [QUICK_REFERENCE.md](../../QUICK_REFERENCE.md) is the one-page digest. Each section blueprint ends with a hardened checklist `S-*-H`. For English prose, run `scripts/prose_lint.py` (H must be zero) and then `scripts/pronoun_check.py`; both are diagnostics, not proof.

## 1. Start at the requested unit

Identify the active manuscript, available materials, and requested output from existing context. For a new full paper, read [evidence-and-claims.md](../../core/rules/evidence-and-claims.md), [storyline-and-contributions.md](../../core/rules/storyline-and-contributions.md), and [outline-template.md](../../core/templates/outline-template.md). Build a compact facts/story/paragraph plan, reusing project records. One [writing workspace](../../core/templates/writing-workspace.md) is enough; no mandatory suite of setup files.

If the user asked only for an abstract or a section, skip full-paper intake and outline creation. Deliver that unit from its actual sources. If only ideas exist, label proposed content, deliver a bounded outline and evidence gaps, and never invent completed results or design/run new experiments by default.

Read [workflow-gates.md](../../core/rules/workflow-gates.md). Respect a requested outline/proposal gate. Otherwise a request for a draft authorizes a reviewable draft; do not add paragraph-by-paragraph approval. State consequential assumptions once and make substantive progress in the first delivery.

## 2. Load the actual blueprint and write

Read [prose-rules.md](../../core/rules/prose-rules.md) and the file for the requested section:

| Unit | Required reference | Observable output |
| --- | --- | --- |
| Abstract/title | [section-abstract.md](../../core/rules/section-abstract.md) | A1–A9 actual content → one clean paragraph + measured words |
| Introduction | [section-introduction.md](../../core/rules/section-introduction.md) | P1–P8 sentence tasks → continuous motivation → matched contributions |
| Related Work | [section-related-work.md](../../core/rules/section-related-work.md) | Problem-oriented themes; each second paragraph 2–3 sentences, target 35–65 words, max 80 and no longer than first |
| Method | [section-methodology.md](../../core/rules/section-methodology.md) | Heading/figure mapping; inputs, symbols, equations, output consumers; training/inference distinction |
| Experiments | [section-experiments.md](../../core/rules/section-experiments.md) | Every paragraph topic-first; results E1–E6 with actual operational reasons and local boundaries |
| Conclusion | [section-conclusion.md](../../core/rules/section-conclusion.md) | C1–C6 supported thesis and scope, not an abstract replay |

The profile is `journal_method_structured_v2`, a house writing convention. Preserve function mapping if real method structure or an official constraint requires adjacent merges. Never fill missing slots with invented mechanisms, claims, citations, or experiments.

For figures load [figure-standards.md](../../core/rules/figure-standards.md); for new/changed external claims load [citations-policy.md](../../core/rules/citations-policy.md). Read the actual table/protocol/method definition before interpreting it. A current code tree is not automatically the source behind historical results. Do not copy private exemplars; [exemplar-patterns.md](../../core/templates/exemplar-patterns.md) explains functional borrowing.

## 3. Verify and deliver

Use [verification-protocol.md](../../core/rules/verification-protocol.md) for checks appropriate to the change, the real engine, and available tools. Unknown venue/tool gaps remain explicit; useful prose continues. Do not mark an unrun check as passed.

Deliver clean requested text, compact evidence/meaning notes, and only material unresolved items. For direct authorized edits, apply and reread the requested unit; for proposal-only work, leave the manuscript unchanged. Keep sentence plans in review notes unless requested in the response. Finish the full authorized scope, not just the first paragraph.
