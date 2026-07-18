<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Exemplar Patterns from Published IEEE TIP Papers

Distilled from a section-by-section analysis of five published IEEE
Transactions on Image Processing papers (two micro-expression recognition
papers, one open-set recognition paper, one 3D semantic scene completion
paper, one driver-attention estimation paper; 2021-2026). Short quotes are
reproduced for scholarly analysis with attribution:

- [P1] Li et al., "Joint Local and Global Information Learning With Single
  Apex Frame Detection for Micro-Expression Recognition," TIP 2021.
- [P2] Zhang et al., "Micro-Expression Analysis Based on Self-Adaptive
  Pseudo-Labeling and Residual Connected Channel Attention Mechanisms," TIP 2026.
- [P3] "Embracing the Power of Known Class Bias in Open Set Recognition From
  a Reconstruction Perspective," TIP 2026.
- [P4] "Enhanced Geometry and Semantics for Camera-Based 3D Semantic Scene
  Completion," TIP 2026.
- [P5] "LNet: Lightweight Network for Driver Attention Estimation via Scene
  and Gaze Consistency," TIP 2026.

PDFs are NOT shipped with the suite. To mine further quotes locally, set
`exemplar_pdf_dir` in `local/config` and extract with `pdftotext`.

**Precedence: the house rules in `core/rules/` always win over exemplar
habits.** See "Exemplar defects to avoid" at the end of this file.

---

## 1. Cross-paper invariants (found in 3+ of 5 papers; treat as canonical)

1. Abstract = value sentence -> "However" limitations (ideally exactly two,
   each with a consequence) -> propose ACRONYM -> one design sentence per
   limitation -> experiments claim. Measured lengths: 204-260 words.
2. Introduction opens with a task-definition sentence plus citations, with a
   drop-cap first word (`\IEEEPARstart`).
3. Paragraph-final "However, ..." gap sentences structure the introduction.
4. Contribution list: "The (main) contributions of this paper are (summarized)
   as follows:", 3-4 verb-initial bullets, last bullet often the experimental
   validation.
5. Roadmap paragraph is optional (older style keeps one; 2026 papers omit).
6. Related work: 2-3 thematic subsections, each closing with critique plus
   pivot to the present work.
7. Method section opens with "In this section, we ..." plus a figure pointer;
   the overall-architecture subsection walks the pipeline figure in
   First/Next/Then/Finally order.
8. Module subsections: motivation sentence -> derivation with equations ->
   `where` clause after every equation -> closing sentence tying back to the
   motivation.
9. Experiments order: datasets -> metrics (often with defining equations) ->
   implementation details (hardware named) -> main comparison -> further
   benchmarks -> ablations -> sensitivity/analysis -> computational cost.
   Failure-case or discussion subsections are a rising norm in 2026 papers.
10. Table lead-ins: "Table N reports/shows/presents ..." or
    "As shown in Table N, ...".
11. Number citation formula: "outperforms [baseline] by [d1], [d2], and [d3]
    in terms of [metric] on [D1], [D2], and [D3], respectively."
12. Every cited number is followed by an interpretation sentence ("The
    results demonstrate/indicate that ...").
13. Every losing or exceptional cell gets one hedged causal clause ("This may
    be attributable to ...", "mainly because ...", "likely due to ...").
14. Experiment transitions: "To further [verify/validate/investigate] X, we
    [conduct/compare/evaluate] Y, with results shown in Table N."
15. Connective palette: Specifically / Moreover / Additionally / Furthermore /
    However / Notably / It is worth noting that.
16. Conclusion: proposal recap -> module recap -> findings -> optional future
    work.

---

## 2. Sentence banks by section (short attributed quotes)

### Abstract moves
- Limitation pair with consequences [P2]: "However, existing
  pseudo-labeling-based methods for micro-expression analysis have two major
  limitations. First, ... which leads to inaccurate labeling. Second, they
  predominantly focus on overall features, thereby neglecting subtle
  features."
- Design mapping [P2]: "To address the first limitation, we propose a
  Self-Adaptive Pseudo-labeling Method (SAPM) that ... thereby improving
  labeling accuracy."
- Experiments close with numbers [P2]: "Experimental results show that our
  proposed method significantly outperforms existing methods, achieving an
  overall performance of 58.24%, a 19.62% improvement ..." (note: the house
  significance rule S-EXP-7 requires a test behind such wording).
- Experiments close without numbers [P4]: "By doing so, our method achieves
  performance improvements over state-of-the-art methods on the ...
  benchmarks."

### Introduction moves
- Definition opener [P1]: "MICRO-EXPRESSIONS (MEs) are involuntary facial
  movements reacting to emotional stimulus [1]."
- Applications sentence [P3]: "widely used in practical applications such as
  autonomous driving [4], medical diagnosis [5], and security monitoring [6]".
- Gap sentence [P5]: "However, these approaches typically focus on the
  unidirectional guidance of information extraction and fail to fully explore
  the bidirectional relationship between gaze and scene."
- Pivot [P2]: "To address these issues, we propose the Spot-Then-Recognize
  Method (STRM) ..."
- Contribution intro [P1]: "The contribution of this paper is threefold: (1)
  A new method, termed ..., is proposed to ..."
- Roadmap [P1]: "The remaining parts of this paper are organized as follows:
  Section II presents the related work, while Section III details ..."

### Related-work moves
- Named critique [P2]: "Liong et al. [8] proposed a sliding window-based
  pseudo-labeling technique, which can lead to large discrepancies between
  pseudo-labels and actual conditions ..."
- Acronym-subject review [P3]: "ARPL [8] introduces an adversarial margin
  constraint to minimize the overlap between ..."
- Subsection-closing pivot [P3]: "Although the core motivation of methods
  discussed above is to ..., they can hardly eliminate the known class bias
  completely due to the absence of unknown classes in training. Therefore,
  this paper ... utilizes ..."
- Chronology markers: "In earlier studies ...", "With the advent of deep
  learning ...", "Recently, ...", "More recently, ..." [P1-P4].

### Method moves
- Section opener [P3]: "In this section, we demonstrate the details of the
  proposed ... framework (as shown in Fig. 3) which ..."
- Pipeline walkthrough [P4]: "First, the images are processed using ...
  Next, ... this paper directly performs ... Then, considering ..., we design
  two subnetworks ... Finally, we introduce the loss function used for
  training."
- Module motivation opener [P4]: "To fully leverage the advantages of ...
  while addressing ..., we introduce an ..."
- Where-clause [P5]: "where F is the input feature, and F_int denotes the
  extracted feature."
- Motivation tie-back [P3]: "... which is consistent with our motivation."

### Experiments moves
- Table lead-ins: "Table IV reports the comparison results in terms of
  accuracy and F1-score." [P1]; "As shown in Tab. II, we report the
  quantitative results of our method compared to the latest ... methods on
  the ... validation set." [P4]
- Delta formula [P1]: "the proposed ... consistently outperforms LBP [40] by
  0.2439, 0.0566, and 0.3011 in terms of NMAE on CASME, CASME II and SAMM,
  respectively."
- From-to formula [P5]: "TC is reduced from 10.36 to 2.15 ... NFPE-KL and
  NFPE-MSE decrease by 66.6% and 49.8%, respectively."
- Efficiency trade-off [P5]: "the model parameters are reduced by 96.84%,
  while accuracy shows only a 1.99% and 7.03% trade-off, respectively."
- Comparable-performance phrasing [P1]: "achieves comparable performance,
  i.e., 0.60 vs. 0.57 on CASME, 0.64 vs. 0.62 on CASME II ..."
- Interpretation pairing [P2]: "These results confirm that SAPM's adaptive
  threshold consistently outperforms any single fixed threshold within the
  tested range."
- Exception explanation [P3]: "It is worth noting that our method is slightly
  inferior to SOTA methods in closed-set accuracy, mainly because ... In
  other words, ... at the cost of closed-set accuracy." (house note: D1/D2
  cap such passages at one hedged clause; do not expand a weakness.)
- Ablation opener [P5]: "To evaluate the contribution of each proposed
  component, we conduct an ablation study, with results shown in Table VII."
- Qualitative walkthrough with numbered advantages [P4]: "We observe that our
  method has the following advantages over other methods: 1) ... 2) ... These
  results further validate the effectiveness of our approach."
- Honest-latency note [P5]: "theoretical reductions in computational
  complexity do not necessarily yield proportional wall-clock acceleration or
  FPS gains."

### Conclusion moves
- Opener [P5]: "In this paper, we propose a lightweight framework (LNet)
  designed to ..."
- Module recap with ordinals [P2]: "first, an adaptive pseudo-labeling
  approach is introduced to ... Second, we design the ... based on ..."
- Future-work closers [P2]: "future work could establish finer-grained and
  unified standards to boost analysis performance. Moreover, ... integrating
  auxiliary cues such as gestures, voice, and ECG therefore represents a
  promising avenue ..."

---

## 3. Options, not rules (varies across the corpus)
- Roadmap paragraph: present in older-style papers, omitted in 2026 papers.
  House default keeps a roadmap; omission is a user choice.
- Numbers in the abstract: one of five papers gives concrete numbers; a
  named-benchmark list is near universal.
- Future-work paragraph: three of five close with future work; two end on the
  findings recap (acceptable when a discussion section already covers open
  problems).
- Teaser figure or positioning table inside the introduction: used in
  dense-benchmark fields [P4]; optional.
- Journal-extension declaration ("A preliminary version of this work was
  presented in [n]. The work in this paper is substantially extended in four
  aspects: ...") [P1]: mandatory content when the paper extends a conference
  paper, otherwise absent.

---

## 4. Exemplar defects to avoid (the suite holds a higher bar)
1. **Loose "significantly"**: several exemplars write "significantly
   outperforms" with no statistical test. House rule S-EXP-7 restricts
   significance language to the pre-declared primary metric under a stated
   test.
2. **Puffery**: "fully proves", "fully demonstrates", "excellent
   performance", "strong overall performance" appear in exemplars and are
   banned by S-EXP-8.
3. **Full-grid recitation**: exemplars often re-recite entire tables in
   prose. House rule S-EXP-3 restates headlines only.
4. **Protocol repetition**: exemplars restate protocol details inside later
   subsections. House rule S-EXP-10 states the protocol once.
