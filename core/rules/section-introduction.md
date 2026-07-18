<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Section Rules: Introduction (S-INT)

Apply on top of `prose-rules.md`. The introduction is drafted AFTER the
method, experiments, and related-work sections in the ieee-write order.

## S-INT-1. Opener
Open with `\IEEEPARstart` and a definition sentence of the task, plus
citations. Follow with importance and application scenarios, then the gap or
demand statement. Use the restrained register: do NOT open with sensational
statistics or emotional hooks, even though some published papers do.
- Pattern: "X are [definition]~\cite{...}. X recognition supports [fields],
  yet the task remains difficult because [physical reason]."

## S-INT-2. Weave the prior art into the narrative
Cite and characterize prior work inside the introduction paragraphs, each
citation followed by a pointed limitation, using the named-critique pattern:
- "A et al.~\cite{n} proposed B. However, B overlooks C."
Paragraph-final `However,` gap sentences structure the whole introduction:
every prior-art paragraph ends by opening the gap the paper will fill.

## S-INT-3. The pivot
Transition to the proposal with the fixed move: "To address these issues, we
propose ..." (or an equivalent), then 1-2 sentences on how the internal
modules answer the limitations just raised. Point to the motivation figure
here if one exists.

## S-INT-4. Contribution list
- Introduce with the formula: "The main contributions are as follows." or
  "The contribution of this paper is threefold:".
- 3-4 items, each one self-contained sentence starting with a strong verb or
  noun phrase. Vary the openers: do not start every item with "We" (use
  "This paper ...", "[MODEL] ...", "On [benchmark] ..." for variety).
- The last item is often the experimental validation claim.
- Claims in the list must match the experiments word for word in strength:
  qualify superlatives exactly as the tables support them (for example
  "the largest and strongest baseline", not just "the largest", when the
  experiments section says both).

## S-INT-5. Roadmap paragraph
"The rest of this paper is organized as follows. Section II reviews ...
Section III presents ... Section IV reports ... Section V concludes the
paper." The roadmap is the house default. (Recent published papers sometimes
omit the roadmap: treat omission as an option only if the user asks.)

## S-INT-6. Consistency duties
- Any number quoted in the introduction must exist in the experiments section
  and match exactly.
- Terminology introduced here (module names, metric names) must match the
  method and experiments sections. Grep the manuscript before coining a name.
