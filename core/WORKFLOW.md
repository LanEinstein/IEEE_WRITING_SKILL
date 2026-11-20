<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Start here: scope, routing, and a useful first delivery

This is the shared execution contract for the four entry points. Load this file once per task. Detailed section blueprints are loaded only for the section being written or checked. Manuscript prose defaults to concise academic English; explanations follow the user's language.

## 1. Resolve the task from existing context

Read the user request and current project instructions first. Identify the active manuscript, requested unit, available evidence, target venue (possibly unknown), and authorization already given. Reuse existing storyline, protocol, fact tables, and bibliography. Do not ask the author to re-enter known information or create duplicate records.

Use the following routing table. A local edit does not restart the full-paper workflow.

| Request | Read next | First useful delivery | Skip |
| --- | --- | --- | --- |
| An idea, no completed research | evidence-and-claims; storyline-and-contributions | Proposed question/thesis, available facts, missing evidence by claim, provisional outline | Completed-result abstract; automatic experiment design |
| Results/materials ready, blank manuscript | evidence-and-claims; storyline-and-contributions; outline-template | Compact facts/story/outline, then the authorized draft | Exhaustive repository scanning; approval already covered by the request |
| Draft or revise one section | prose-rules; that section's rule file; relevant source records | The actual section or requested proposal with unresolved items | Other section rules; full new workspace |
| Abstract only | prose-rules; section-abstract; evidence used by the abstract | A1–A9 mapping, clean abstract, measured count | Full outline, method ledger, whole-paper build |
| Method/overview figure | section-methodology; figure-standards; title-figure-symbol-map | Heading/figure/input-output mapping plus requested method text | New diagnostic experiments |
| Experimental analysis | section-experiments; relevant table/protocol/method definition | Topic-first E1–E6 paragraph with operational explanation | Invented causal tests; a recap of every cell |
| Peer review | review resources and sections in scope | Evidence-located scientific findings and bounded fixes | Manuscript edits; unsupported acceptance prediction |
| Style check | prose-rules; sections in scope; venue requirements if known | Scope-limited style report | Scientific-review panel; compulsory rewriting |

Paths in the table refer to `core/rules/` or `core/templates/`. All six section files are linked from the entry points and [sentence-plan.md](templates/sentence-plan.md).

## 2. Rules and project configuration

Scientific accuracy constrains every draft. Current official venue/article-type/stage requirements constrain submission format. Apply explicit session instructions and current project agreements within those constraints, then the selected house writing profile, then exemplar habits. Never treat a house convention as an IEEE rule. An instruction cannot turn an unsupported scientific statement into a fact; flag the conflict and offer accurate wording.

Configuration is read by the agent, not automatically parsed by the scripts:

1. Latest explicit session instructions and authorization.
2. Current project instructions, including explicitly superseding updates; do not reactivate replaced staging-file rules.
3. Project `WRITING_CONFIG.md` or an already-established equivalent.
4. Suite `local/config.md` for machine pointers only.
5. Defaults here and in [venue-style-profiles.md](literature/venue-style-profiles.md).

`local/config.example.md` is a sample, not a mandatory setup form. Do not copy the suite's local paths, article identity, or private exemplar content into a new project. If active manuscript or essential technical meaning is ambiguous, ask one focused question; continue independent work. An unknown venue stays `null`: use a provisional content structure and ask about the venue only when its answer affects the requested deliverable.

Default content profile: `journal_method_structured_v2` for journal method papers. Default presentation unit: **subsection**, or the section when it has no subsections. This is a delivery size, not an approval gate. The user's sentence-, paragraph-, section-, or whole-task authorization takes precedence.

## 3. Minimal records, immediate progress

For a small task, a short in-response work card is sufficient. For a new full paper, one `WRITING_WORKSPACE.md` can hold target/status, facts, storyline, outline, open issues, and handoff. Split into separate files only when useful. Existing `FACTS.md`, `PAPER_STORYLINE.md`, `WRITING_PROTOCOL.md`, or similar records remain in place.

Record only facts needed for the current claim, with source location and state. Read linked tables, method definitions, and run provenance as needed; discover code with the host's prescribed tools. A current implementation is not automatically the implementation behind historical results. No code is required for theoretical, measurement, or materials-only writing; report the evidence available.

First response after intake: state the scope and any consequential assumption in one or two sentences, then deliver substantive work. Never respond with only a long checklist of prerequisites. The [workspace template](templates/writing-workspace.md) offers optional fields; do not make the user fill them all.

## 4. Authorization and version safety

Follow [workflow-gates.md](rules/workflow-gates.md). If the user asks to see a proposal before edits, present the requested unit and wait. If the user authorizes direct drafting or applying a section, perform the work within that scope without per-paragraph permission. A new paper request authorizes creation of a reviewable draft; an explicitly requested outline-review gate remains binding. Silence is never approval of a pending gate.

Review/style workflows leave manuscript, bibliography, figures, and original build outputs unchanged. They may write the requested report in the agreed output area. Compile only in an isolated build copy for a read-only review. Do not submit, publish, push, or send private materials to another service without the authorization required for that action.

## 5. Missing tools or materials: localize the gap

| Missing item | Continue with | Mark accurately |
| --- | --- | --- |
| Venue unknown or official site unavailable | Content/logic and a provisional blueprint | Venue compliance pending; no assumed page cap or anonymity |
| No code/logs, but author-provided methods/tables | Source-linked draft and targeted questions | Author-confirmed vs run-traced separately |
| Missing result/contradictory sources | Independent paragraphs and narrower claims | `[EVIDENCE: precise item]` in draft only; affected claim pending |
| No TeX engine or missing template | Plain-text/Markdown prose and manuscript structure | Build/template check not run; never fabricate pages |
| PDF only | Visible-text and rendered-layout review | Source/build checks unavailable |
| No network/index failure | Existing verified sources and local full texts | Bibliographic metadata/content verification pending; not proof of nonexistence |
| No text layer in a figure | Source labels, visual inspection, or OCR when available | Extraction inconclusive; never call a rename safe from empty text |
| No independent/Claude runtime or quota | Own review, status of requested external review | Pending/unavailable; never simulate another model's agreement |

Working placeholders remain visibly distinct from final prose. Before declaring submission-ready, unresolved material evidence, citations, and venue requirements must be resolved or the dependent claim removed/limited with the author’s scope preserved. Do not block unrelated work or design/run new experiments merely to fill a writing slot.

## 6. Finish with a usable handoff

Deliver the actual text/report and a compact statement of: what changed, which evidence was checked, which checks ran, and only the unresolved items that affect use. Keep long sentence plans and audit tables in review notes rather than in manuscript prose. Offer optional next work once; do not turn it into a new gate or an assumed task.

For a paused/interrupted long task, record the active version, completed units, pending approvals, source conflicts, and next authorized step. Resume from that state without restarting intake.

## 7. Modes

Pick one mode from the request; do not blend them.

| Mode | Trigger | Deliverable | Never |
| --- | --- | --- | --- |
| Draft | "write / draft / restructure this unit" | the requested text, from sources | invent results; plan-only replies |
| Polish | "polish / revise / improve this text" | revised text (or proposals, if requested) with the material changes named | change the claim, the numbers, the comparator |
| Audit | "check / review style / find problems" | a scoped report with locations and fixes | edit the manuscript |
| Review | "review the science / mock review" | prioritized findings with evidence | new experiments; a simulated acceptance verdict |
| Campaign | a unit-by-unit series ("paragraph by paragraph") | one unit per turn: proposal, approval, apply, next | skip ahead; batch-apply unapproved units |

A campaign has a fixed loop: propose the unit (exact original, exact replacement, reason) → wait for the approval word → apply → re-read the applied text in context → next unit. One rejection switches the next proposal for that unit to the author's language as continuous prose for logic approval, then English again.

## 8. Before anything reaches the manuscript

Run these in order; report which ran.

1. Rules for the unit, read in full (the section blueprint plus the shared rules it names).
2. Self-review pass: as author, as first-time reader, as a hostile reviewer. Fix what it finds and say what it changed.
3. `scripts/prose_lint.py` when the unit is English prose: H must be zero; each S is fixed or justified.
4. `scripts/pronoun_check.py` after the other checks: no H; each S replaced or justified.
5. Numbers: every value traced, every difference computed by tool.
6. Terms and symbols: defined before use, one name per object, no symbol used once.
7. Layout, when the change can move text: measured after the text is final.

## 9. Rule index

| Concern | File |
| --- | --- |
| Selling the work, positive framing, claim scope | [voice-and-positioning.md](rules/voice-and-positioning.md) |
| Paragraph argument, topic sentences, transitions | [paragraph-architecture.md](rules/paragraph-architecture.md) |
| Sentence order, connectives, repetition, punctuation | [sentence-craft.md](rules/sentence-craft.md) |
| Word choice, register, banned forms | [lexicon.md](rules/lexicon.md) |
| Writing English without translating Chinese | [translation-discipline.md](rules/translation-discipline.md) |
| Revising: scope, preservation, check order, self-review | [revising.md](rules/revising.md) |
| Simulated review, reader feedback, read-through | [review-loops.md](rules/review-loops.md) |
| Terms, abbreviations, symbols, formulas | [terminology-and-notation.md](rules/terminology-and-notation.md) |
| Page budget, spacing, orphans, TeX and PDF hygiene | [layout-and-build.md](rules/layout-and-build.md) |
| Figures, visual results, captions | [figure-standards.md](rules/figure-standards.md) |
| Authorization, concurrent edits, real state | [workflow-gates.md](rules/workflow-gates.md) |
| Evidence traceability, claim boundaries | [evidence-and-claims.md](rules/evidence-and-claims.md) |

Section blueprints (`section-*.md`) end with a hardened checklist `S-*-H` distilled from rejected drafts; read it with the blueprint, not instead of it.
