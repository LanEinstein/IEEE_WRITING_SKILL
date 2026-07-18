<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Section Rules: Methodology (S-MET)

Apply on top of `prose-rules.md`. The method section is drafted FIRST in the
ieee-write order.

## S-MET-1. Method only, no experimental conclusions
The section presents the method. Effectiveness claims belong to the
experiments section: where a design choice is later validated, use a forward
reference ("Section IV reports the ablation of the pooling"), never a result
number or a superlative.

## S-MET-2. Symbol continuity (mandatory, checked per paragraph)
Modules, equations, and symbols must be woven together in prose. Nothing may
appear in isolation.
- **Every new symbol** is introduced with its origin (which module produces
  the symbol) and its destination (which equation or module consumes the
  symbol next).
- **Cross-equation substitution is stated in words.** When a later equation
  reuses a quantity from an earlier one, say so explicitly and add an
  `\eqref` back-reference. Example repair: "where z_{i,k} is the logit of
  class k for sample i, computed by Eq.~(FUSION)."
- **Subsection openers connect.** The first sentence of each module
  subsection picks up the output of the previous subsection: "The first
  branch supplies the head with a nonlinear readout. The second branch
  supplies the linear counterpart."

## S-MET-3. Symbol hygiene
Maintain a symbol table while drafting (symbol, meaning, defining equation,
consumers). Rules: no symbol defined twice with different meanings, no two
easily confused symbols for different quantities, bold for vectors/matrices
per IEEE convention, and every equation followed by a `where` clause defining
each symbol that first appears in that equation.

## S-MET-4. Section and subsection architecture
- **Section opener paragraph**: restate the physical difficulty of the task in
  one or two sentences, state the design philosophy, point to the overview
  figure, and (house option) list the subsection roadmap.
- **Overall-framework subsection**: walk the pipeline figure in order with
  First / Next / Then / Finally, naming each module and the tensor that flows
  between modules, so a reader can reconstruct the figure from the text.
- **One subsection per module**, in the order of the figure.

## S-MET-5. Module micro-template
Each module subsection follows: (1) motivation sentence ("To address X, we
introduce Y"), (2) design statement, (3) step-by-step derivation with
equations and `where` clauses, (4) closing sentence tying the design back to
the motivation or handing off to the next module.

## S-MET-6. Algorithm blocks
Where a training or inference procedure has nontrivial control flow, add an
`algorithm` float (IEEEtran-compatible packages) rather than a long prose
walkthrough. Keep notation identical to the equations.

## S-MET-7. Figure-caption duties
The overview-figure caption is self-contained: name every numbered block,
state which subsection details each block, and avoid derived numbers that the
figure does not display. Module names in the figure must equal the subsection
titles character for character.
