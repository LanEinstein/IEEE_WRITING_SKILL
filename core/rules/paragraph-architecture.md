<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Paragraph architecture: one argument, stated first

A paragraph is one argument with a claim, its evidence, and the reasoning that connects them. Everything else belongs elsewhere. These rules are house defaults for the structured profile; they are not IEEE requirements. For journal method papers they are not optional in experiments and analysis sections.

## PA1. One paragraph, one argument

Before drafting, write the paragraph's claim in one sentence. If the draft cannot be summarised by that sentence, the paragraph is doing two jobs or none.

Symptoms that a paragraph has no argument: a list of correct facts with no connective reasoning; a paragraph whose second half answers a different question; a paragraph the reader can summarise only as "some results".

## PA2. The first sentence governs the whole paragraph

The topic sentence is a conclusion-type sentence: concise, free of implementation detail, and covering every point the paragraph will make. If the paragraph makes two points, the first sentence names both. A topic sentence that covers one of two points is a defect even if it is true.

- Do not open with the table, figure or "As shown in Fig. X"; the subject is the method, protocol, benchmark or finding, and the float appears in the evidence sentence.
- Do not open with a concessive clause ("Although ...") when the paragraph's job is to state a finding.
- Do not open with a count ("Two checks ...", "First ... Second ...") or another report-style scaffold. State the claim and give the evidence.
- Do not open with a generic frame that any paper could use ("The class evidence depends on the input, the training and the architecture") when the subsection is about one of those.

## PA3. Every observation is followed by its analysis

After each result sentence, one sentence says what it shows: the mechanism, the operation that produced it, or the consequence. The analysis sentence takes as its subject the object of the observation ("This stability benefits from ..."), so the link is visible without an extra connective.

Results without analysis are rejected. Analysis without a result is speculation.

## PA4. The paragraph ends on its own theme

The last sentence carries the paragraph's strongest point and stays within its theme. In an analysis section it lands on the finding, not on a paper-level selling line. In a module section it ends on what the module achieves. Do not append a new fact after the logical endpoint has been reached; that breaks the closure the reader has just formed.

## PA5. Analysis over enumeration

Cover in more depth what the result reveals, and less the procedure that produced it. Numbers that a table already shows are not repeated in the prose. Necessary results are still stated; omission is not concision.

Give the reader the numbers that carry the claim (a gap, a rank, a range), and route the rest to the table or supplement.

## PA6. Depth follows importance

The strongest finding gets the most space and its full chain: phenomenon, mechanism, consequence. Secondary findings get one clear sentence each. A key insight must not be missing while a minor one is developed. Uneven depth is correct; missing insight is not.

## PA7. Describe what was achieved, not the order of your work

Do not write the laboratory chronology ("then", "after that", "we first ... and then ..."). Describe the design from a global viewpoint: what the component guarantees, why that guarantee is needed. Procedural detail that does not help a reader understand the method or the finding stays out.

## PA8. Each operation carries its motive in the same sentence

State the purpose and the operation together: "To isolate X, we replace Y with Z" or "Z removes Y, so the comparison measures X alone". A sentence that only reports an operation forces the reader to infer why it exists.

## PA9. Transitions between paragraphs

Every paragraph after the first in a subsection opens with a link to the previous one. Acceptable forms:

- a purpose clause ("To determine which component carries the evidence, ...");
- a concession or contrast that names the previous object ("Beyond the readout, ...");
- a sentence-initial adverb that states the real relation ("Moreover,", "In contrast,", "Similarly,");
- a subject that names the previous paragraph's object ("The discarded component ...").

Forced transitions are as bad as none. If two paragraphs are not related, the subsection structure is wrong, not the transition.

## PA10. No sentence may be its own paragraph

A one-sentence paragraph is merged into the paragraph whose point it supports, unless a section deliberately uses a short statement as a structural device.

## PA11. Do not repeat a fact already established

One fact is stated in full once. Later paragraphs recall it with a short noun phrase and a section pointer, only when the transition needs it. A sentence copied from the Abstract or Introduction into a body section is repetition, not consistency.

Before drafting, search the neighbouring paragraphs for the same fact.

## PA12. Nothing enters a paragraph that does not serve its thread

A fact that the paragraph neither uses nor explains is a detour, even when it is true and interesting. Internal project vocabulary (stage names, screen identifiers, file names, variant codes, development chronology) never appears.

## PA13. Reader position by position

The reader is not omniscient: they learn the paper in order. Do not use a symbol, abbreviation, term or result before the text defines it, and do not cite content from a later section that the reader cannot yet know. Forward references are allowed in a navigation paragraph, in the Introduction, and when pointing to the supplement; they are not allowed as a substitute for local explanation.

## PA14. Topic sentences read as a summary

Read only the first sentence of every paragraph in a section. They should give the section's complete argument in order. If they do not, the section's logic lives only in the author's head.

## PA15. Subsection titles

Titles are noun phrases naming the object under test, and they show progression across the section. Banned: slogan titles, "From X to Y" titles, "Ablation Study I / More Experiments", and titles that promise a result the subsection does not establish. A subsection with a single paragraph needs no run-in heading.
