<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Section Rules: Related Work (S-RW)

Apply on top of `prose-rules.md`. Drafted after the experiments section in the
ieee-write order.

## S-RW-1. Principles only, never results
Related work discusses differences at the level of principle and method ONLY.
- A subsection must NEVER end with a performance comparison ("yet still
  matches or exceeds the baselines..."). Results belong to the experiments
  section exclusively.
- Do not re-explain any mechanism that the method section already derives
  with equations. One sentence of positioning is enough; a full re-derivation
  is cross-section duplication and gets cut.

## S-RW-2. Structure: 2-3 thematic subsections
Organize by theme: typically (A) the task family, (B) the closest technical
sub-family, (C) the borrowed technique or design philosophy. An optional
one-sentence preamble may state the scope of the review and which subsection
is most relevant.

## S-RW-3. Every subsection ends with critique plus pivot
The strongest structural invariant of the published corpus (5/5 papers):
each subsection closes by naming the shared limitation of the reviewed line
and pivoting to the present work at the principle level.
- Pattern: "However, these methods [shared limitation]. [MODEL] instead
  [principle-level difference]."
- Allowed connectives: "However, ...", "Although ..., they can hardly ...",
  "Despite progress, these methods [limitation]."

## S-RW-4. The named-critique micro-pattern
Within a subsection, review concrete works with:
- "A et al.~\cite{n} proposed B, which [one-line mechanism]."
- Famous methods may be the subject directly: "ACRONYM~\cite{n} introduces
  [mechanism] to [goal]."
Use chronology markers to give the line a direction: "Early methods ...",
"With the advent of deep learning, ...", "Recently, ...".

## S-RW-5. Terminology consistency
Reuse the manuscript's established terms; never introduce a synonym for an
existing concept ("path" vs "route" vs "approach" drift is a known real
failure). Before renaming anything, grep the whole manuscript for the
established phrasing and conform to that phrasing.

## S-RW-6. Pronoun repairs specific to reviews
When listing several works, `they` is banned like every pronoun (G1): repair
with `each` plus singular agreement ("each method summarizes ..."), or repeat
the family name ("these descriptor methods" is banned too because of
`these`; write "the descriptor methods").
