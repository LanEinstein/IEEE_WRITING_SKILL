<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Configuration: machine pointers and project intent are different

Copy only the machine-pointer block to suite `local/config.md` if needed. Existing local keys remain supported as agent-readable notes. Nothing here is automatically parsed by the shell/Python helpers; pass script bounds/options explicitly.

```yaml
# SUITE MACHINE POINTERS ONLY; optional and private
golden_sample_path: null       # local exemplar; never copy unpublished text/data
exemplar_pdf_dir: null         # read on demand, not a compulsory startup corpus
crossref_mailto: null          # only if the user supplies/authorizes that address
```

Current project/session facts belong in its existing configuration or a `WRITING_CONFIG.md` / workspace, not the suite's global local settings. Agent-fill from the task; fields are optional and a small task needs no new config file.

```yaml
# PROJECT NOTES, not an executable schema or a source of permission
target:
  venue: null
  article_type: null
  submission_stage_or_year: null
  official_source: null
  checked_on: null
manuscript:
  main_file: null              # resolve the actual active manuscript; do not create another
  evidence_record: null       # reuse existing facts/storyline/protocol
workflow:
  requested_scope: null
  proposal_only: null          # derive from the actual user instruction
  presentation_unit: subsection  # whole section if unpartitioned; not an approval gate
  authorization_source: null   # cite existing instruction; a field cannot grant permission
  new_experiments: false      # writing alone does not expand the research task
style:
  profile: journal_method_structured_v2
  author_preferences: {}      # explicit punctuation/pronoun/etc. preferences and exceptions
```

Default profile details live in the section rules, not duplicated numeric knobs here. Session intent overrides older project preferences within scientific accuracy and official constraints. Suite machine pointers cannot supply a new project's target, manuscript, or authorization.

Maintainers: `local/leak-patterns.txt` holds private patterns for `scripts/leak_scan.sh`. `local/scan-excludes.txt` can name non-shipped files. Missing patterns yield INCOMPLETE, never a clean release verdict. Multilingual runtime guidance is allowed; privacy is not determined by script language.

## Author preferences a project may record

Optional, agent-read. Every entry is a project decision with a scope; an entry here overrides the suite default for that project only.

```yaml
author_preferences:
  pronouns: allowed            # banned | allowed | allowed-with-check
  semicolons_in_prose: false
  em_dashes_in_prose: false
  colons_in_prose: false       # body prose; subsection-title colons may stay
  rather_than: false           # state results positively instead
  bold_for_defined_terms: true
  caption_max_lines: 5
  length_rule: "polish does not grow the text unless requested"
  banned_words: [only-repeat, markedly, recipe, registered, fits, package, deployed]
  banned_frames: ["lies in", "relies on", "X itself", "it alone"]
  exemplars: []                # papers in the target venue studied for this unit
  word_lists: null             # path to a file of "pattern => reason" for prose_lint --banned
paper_facts:
  page_limit: null             # + what counts toward it, from the official instructions
  split_documents: null        # main + supplement, own references, own builds
  required_statements: []      # e.g. an LLM-usage statement, with its exact required location
```
