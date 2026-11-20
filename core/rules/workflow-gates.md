<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Workflow, authorization, and concurrent edits

## W1. Honor the user's actual review scope

A request for a proposal/review before recording text creates a gate at the requested unit. A request to draft/apply/polish a named section authorizes that section. A whole-task authorization is not reduced to repeated paragraph approvals. Sentence plans and topic-first paragraphs control writing quality, not consent granularity.

If no presentation size is specified, deliver by subsection (whole section if unpartitioned), with a complete artifact at the end. Ask only when a material ambiguity cannot be resolved from existing context. Do not infer a mandatory outline gate or polishing gate from old versions of this suite.

## W2. Present concrete work at a real gate

Where approval is requested, provide the actual proposed text and the material meaning/metric/scope changes, not merely a plan. Use a sentence comparison table when useful or requested; do not force one for an untouched sentence. Wait for explicit approval of the pending unit. Once approved, apply the approved content and continue within the remaining authorization.

## W3. Stay within the writing assignment

Writing does not authorize new experiments, altered numerical results, submission, publication, messages to other people, or unapproved external disclosure. Reversible local reads, drafting, backups, and relevant verification within the authorized task do not need fresh permission merely because they are long or outside the manuscript directory. External collaboration follows [collaborative-review.md](collaborative-review.md).

## W4. One active manuscript and safe application

Read the active region immediately before changing it. Preserve technical meaning, comparison, metric, values, and claim scope unless the user has authorized a specific substantive change. Apply the smallest useful change; reread it in context.

If the file changed concurrently, compare the actual content and merge nonconflicting edits. Do not overwrite newer user text. When a conflict cannot be resolved safely, show the conflicting passages and ask a focused question; keep unaffected work moving. A stale-buffer overwrite is evidence of a conflict, not a reason to reapply blindly.

## W5. Review is read-only with respect to source artifacts

`ieee-review` and `ieee-style` produce reports, not source edits. They may write requested reports to the agreed output directory. Run builds in an isolated copy; never create a new `.aux`, `.log`, PDF, or baseline next to a reviewed original. Other workflows use the existing project build convention and preserve unrelated outputs.

## W6. Report real state

Distinguish proposed, approved, applied, verified, pending, and superseded. A skipped or unavailable check is not a pass. A partial draft with evidence gaps is a reviewable draft, not submission-ready. Preserve previous user decisions across turns.
