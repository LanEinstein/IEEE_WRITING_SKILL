<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Verification: real outputs, relevant scope

## V1. Measure counts; select limits explicitly

`scripts/wordcount_abstract.sh <main.tex>` measures the source abstract and applies **no venue gate by default**. For a verified range use `--min 150 --max 250` (example only; not all IEEE journals). For a plain-text abstract use `--plain <abstract.txt>` before optional bounds. Exit 0 means count succeeded and any supplied bounds passed; 1 means no usable abstract or a supplied gate failed; 2 means bad arguments/dependency error. The source-stripping count is a working convention, not the submission portal's tokenizer; check the final rendered text near a hard limit.

Compute deltas/ratios/ranges with a tool, observe output, then write them. Source result values remain tied to their provenance; a writing assistant is not required to have run the historical experiment to quote an approved table accurately.

## V2. Verify meaning and linked objects

Check object, operation, metric, comparator, scale, quantifier, protocol, and evidence status before and after editing. An abstract-only change needs its sources, A1–A9 functions, word count, and local continuity; it does not force a full-paper build. A rename needs a relevant terminology sweep across accessible text/figure sources. `check_figures_text.sh` searches PDF text recursively; textless/failed/missing PDFs are inconclusive. No-hit extraction never proves every outlined/raster label is clear: inspect rendered/source labels as needed.

## V3. Use the real build; preserve reviewed sources

Follow the existing engine/build configuration. `verify_tex.sh <main.tex> [--set-baseline]` is a pdfLaTeX+BibTeX helper, not a universal engine. It writes beside the target: PDF, auxiliaries, and a per-manuscript `.<basename>.ieee_baseline.txt`. For read-only review, execute it only on an isolated project copy. Do not reset a baseline after edits merely to hide regressions.

For editing tasks, capture a pre-edit build baseline when layout is relevant and tools are available. If none exists, do not fabricate NEW/LEGACY attribution. The helper's line-based box signatures are preliminary; line shifts can change signatures, so verify a suspected new layout issue on the page. Failed compilation cannot establish pages or submission compliance. A successful build can still have unresolved citations/warnings.

A standalone abstract polish need not compile the full paper. Structural/equation/float edits need the relevant build and affected-page visual checks if available. Missing tools leave those checks pending, not the content work blocked. Never install a new toolchain or hand-roll an official-looking class just to make a checklist pass.

## V4. Report only observed results

Run, observe, then report; do not prefill expected counts or pages in the command-launch step. Save enough version/scope information to know which artifact the output describes. Mark each material check `PASS`, `ISSUE`, `NOT_RUN` with reason, or `NOT_APPLICABLE`. Do not describe an attempted Claude call as completed collaboration.

## V5. Sweeps are diagnostic

`sweep_prose.sh` reports raw candidates, including clear pronouns and punctuation that may be allowed. Evaluate each under the active preference and context. It does not parse all TeX macros or recursively expand included files; run on relevant chapter files when applicable. A zero count applies only to the scanned text/pattern. It proves neither scientific correctness nor full manuscript compliance.

`verify_citations.py` uses heuristic index metadata matches. `VERIFIED` does not mean the cited sentence is supported, the listed DOI has been validated, or all fields are correct. Read primary content. `NOT_FOUND` and lookup failures are pending verification, never proof of nonexistence; see [citations-policy.md](citations-policy.md).

## V6. Submission readiness uses the actual target

Use journal/venue, article type, submission stage/year, page accounting, anonymity, abstract limits, supplementary rules, and official source/date in the current project record. Unknown values stay pending. Check actual requirements before claiming submission readiness; do not default to TIP. Mechanical success alone cannot close evidence conflicts, missing citations, draft placeholders, or method/figure disagreements.

Final joint check: terminology/symbols; numbers/ranks; protocol/predictor; claims/evidence. The checks can live in one work record. Report concise outcomes, with detailed logs linked only where useful.

## V7. Prose lint and referent lint (dependency-free)

`scripts/prose_lint.py DRAFT.tex [--include-floats] [--quiet] [--json] [--banned FILE] [--max-words N]`

Reports structural candidates for [translation-discipline.md](translation-discipline.md), [sentence-craft.md](sentence-craft.md) and [lexicon.md](lexicon.md):

- H: known rejected structures (Chinese-origin openers, paired cause-effect connectives, participial openers before the subject, parallel conditional heads), house-banned vocabulary, colons in body prose, a connective or limiter twice in one paragraph, a phrase twice in one sentence.
- S: long sentences, preposition piles, comma chains, semicolons, absolutes and intensifiers, `every/all/any`, "significant" without a test, repeated openings.
- I: every causal connective with its two clauses (for the causal reading test), and sentences with no visible link to the previous one.

Captions are always scanned; set `--include-floats` to scan figure and table bodies. `--banned` adds a project lexicon, one `pattern => reason` per line, so a project's own bans live in the project.

`scripts/pronoun_check.py DRAFT.tex [--json] [--quiet]` lists every demonstrative and pronoun with the candidate antecedents from the same and previous sentence; H for a bare demonstrative, no candidate, or a paragraph-opening pronoun pointing backwards.

Both scripts detect structures, not meaning. Zero H means "no known defect pattern"; content, inference and coherence remain manual (the M-tests in the entry documents). Exit status: 0 clean, 1 H remains, 2 usage error.

## V8. Round-trip verification after applying text

After writing an approved change:

1. assert the old text occurred exactly once before writing, and the new text occurs exactly once after;
2. re-read the changed paragraph and the first sentence of the next paragraph (a changed last sentence can orphan a referent);
3. re-run the two prose scripts on the changed file;
4. re-measure layout if the length changed; a single word can move a line;
5. report the applied text, the location and the checks, not only "done".

## V9. Version identity

Before a review round, record the file version (commit hash or a copy in the preparation area) and give that version to any reviewer. After the round, record the new version. A report that does not name its version cannot be audited.
