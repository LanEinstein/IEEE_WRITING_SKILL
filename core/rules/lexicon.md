<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Lexicon: words that weaken a manuscript

A working list distilled from rejected drafts. Each entry is a default, not an IEEE rule: a project may override an item, but the override is recorded with its reason. `scripts/prose_lint.py` implements the hard entries.

## LX1. Verbs: replace the translation, keep the meaning

| Avoid | Why | Use instead |
| --- | --- | --- |
| use / utilize (to introduce a component) | low register, vague | introduce, apply, adopt, build, the method forms |
| get / obtain (for results) | low register | reach, achieve, yield, produce |
| lose / loses X points | wrong register for metrics | reduces X by, drops by, degrades X by |
| lower / raise (as the only verb, everywhere) | correct but monotonous | reduces/degrades/increases/improves/brings ... to |
| number (as a verb: "the folds number 68") | translation of 数量为 | contains, comprises, the 68 folds, in total |
| close (identities, sessions) | translation of 闭合 | separates identities, groups under one identity |
| fit / refit (as a noun) | engineering jargon | training, model, training run, configuration |
| deploy (without a deployment experiment) | implies production use | the trained model, inference, the method |
| use (as a noun for a design) | vague | the operation, the design, the choice |
| find (for an observation) | colloquial in some venues | observe, show, indicate, report |
| let X do Y | informal | allows X to do Y, enables |
| locate / location (for a finding) | odd transitive use | identify, reveal, place the interference in, the component that carries |

## LX2. Engineering and internal vocabulary

Banned in manuscript prose: recipe, registered / pre-registered, fits, twin arm, run plan, execution plan, training run (as a noun for a configuration), package (for a method), pipeline (only where it is the field's own term), stage code, screen, variant code, host family code, internal file names, "full model" when a canonical description exists.

Replaced by the scientific object: hyperparameters, configuration, fixed in advance, prescribed, retrained model, the method with P and E, architecture.

## LX3. Filler and decorative modifiers

Delete: neutral, by itself, per se, a first classifier layer, essentially, basically, obviously, clearly (as a claim), extremely, markedly, sharply, barely, largely (as a hedge), reliably (as a hedge), some, certain, various (when the set is known), "in order to" (use "to").

Adverb choice is checked against the target venue's corpus: substantially, slightly and greatly are common in vision papers; markedly, sharply and barely are rare and read as a stylistic risk.

## LX4. Absolutes and over-claims

| Avoid | Problem | Use instead |
| --- | --- | --- |
| must | asserts a requirement, closes the design space | is required to, the network needs, tends to, is expected to |
| any (network, method, setting) | universal quantifier without proof | the tested networks, a network, the four architectures |
| every / all | universal claim from sampled evidence | most, the tested, each of the four |
| only (15 uses in one paper) | emphasis inflation | restructure; keep at most one per section, only where it is a real restriction |
| always / never | universal | in the tested conditions |
| significant | implies a statistical test | substantial, large, clear (if no test), significant only with the test |
| clear progress, dramatic | overstates the field | notable progress, substantial progress |
| first to | unverifiable priority | to our knowledge, this work introduces |

## LX5. Frame phrases that mark machine text

Remove by rewriting, not by synonym: "lies in", "rests on", "relies on" (repeated), "plays a key role", "serves as", "is designed to" (repeated), "it is worth noting", "notably" (repeated), "X itself", "it alone", "the key insight is that", "in this regard", "as such", "thereby" (repeated).

One occurrence is fine. A frame appearing twice in a section, or once per paragraph, is a defect.

## LX6. Comparison language

| Avoid | Use instead |
| --- | --- |
| on par with, on bar with | comparable to, matches |
| better than all | outperforms the compared methods |
| much better, a lot | by a large margin, substantially |
| nearly equal, almost the same | differs by less than X, within the seed spread |
| unchanged | has little effect on (state the tolerance), barely changes |
| statistically tied (without a test) | the interval includes zero, the difference is not established |

## LX7. Terminology alignment with the field

Use the field's own word, checked against published papers: for merging datasets, "combine" and "composite" (not "pool", unless the field uses "pooled"); for evaluation units, "subject" (not "person" in one place and "subject" in another); for splits, the terms the protocol's origin paper uses.

Do not coin a term for a known object, and do not rename an established object for variety. When two names denote the same quantity, keep one and delete the other, including its definition.

## LX8. Tense

Present tense for what the paper establishes and what the method does. Past tense for what was done in the experiments when the subject is an action ("we trained", "the models were trained"). Do not mix within one sentence. Completed work is not described in the future tense.

## LX9. Maintenance

Add an entry only with a source: a rejected sentence or an author instruction. When an entry conflicts with a later instruction, the later one wins and the entry is updated rather than duplicated. `scripts/prose_lint.py` reads an optional project word list (`--banned FILE`, one entry per line, `pattern => reason`) so a project can extend this lexicon without editing the suite.
