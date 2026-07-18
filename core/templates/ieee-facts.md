<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# IEEE Facts Sheet (verified 2026-07-18)

Authoritative submission numbers used by the gates. Every fact carries its
source URL. If more than 12 months have passed since the verification date,
re-verify against the sources before relying on a number.

## IEEE Transactions on Image Processing (TIP)
Governed by the IEEE Signal Processing Society "Information for Authors":
https://signalprocessingsociety.org/publications-resources/information-authors
(also linked from the TIP page:
https://signalprocessingsociety.org/publications-resources/ieee-transactions-image-processing)

- Abstract: 150-250 words, self-contained, no abbreviations, footnotes,
  displayed equations, or references. (Practice note: published TIP papers
  freely use dataset/method acronyms, and `%` is a symbol, not an
  abbreviation. Enforce the word count strictly and the no-abbreviation
  clause loosely.)
- Initial submission, regular paper: at most 13 double-column pages,
  10-point font, including title, author info, abstract, text, all figures
  and tables, appendices, proofs, and references.
- Revised manuscript: at most 16 double-column pages.
- Overlength page charge: $220 per published page beyond the first 10.
- Supplementary material: uploaded at initial submission, at most 6
  double-column pages without EiC approval; supplementary material and
  graphical abstracts do not count toward the page limit.
- Graphical abstract: optional.
- Review model: single-anonymized (reviewers know the authors; authors do
  not know the reviewers). Do not spend effort anonymizing a TIP
  submission.
- Reproducibility: code/data release is encouraged.

## IEEE TPAMI
Source: https://www.computer.org/tpami-author-information
MOPC policy PDF: https://ieeecs-media.computer.org/assets/pdf/MOPC_policy.pdf

- Regular papers: 12 double-column pages standard; submissions may be up to
  18 pages subject to mandatory overlength page charges ($200 per page over
  12). Page limits include references and author biographies.
- Short papers: 8 double-column pages. Survey papers: 20.
- Supplementary files: no page limit.
- Abstract word limit: NOT stated on the official page (unverified; do not
  assert one).
- Review anonymity: not stated on the official TPAMI page; the IEEE-wide
  default is single-anonymous
  (https://journals.ieeeauthorcenter.ieee.org/submit-your-article-for-peer-review/about-the-peer-review-process/).
  Treat third-party claims of double-blind TPAMI review as unverified.

## LaTeX class
- IEEEtran v1.8b (2015-08-28), Michael Shell: https://ctan.org/pkg/ieeetran
- IEEE now directs authors to the IEEE Template Selector for current
  templates.

## Suite defaults derived from these facts
- Default target journal: TIP. Page gate: 13 (initial) / 16 (revision).
- Abstract gate: 150-250 words measured, target 230-250.
- No anonymization steps in any workflow unless the user overrides the
  target venue to a double-blind one.
