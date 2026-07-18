<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Venue Tiers (initial scope: computer vision, machine learning, affective computing)

Governs the L2 citation gate. Default policy: **Tier 1 and Tier 2 pass; anything
else is denied by default and needs an explicit user approval with a one-line
justification.** The list is a living document: extend per project with user
consent, never silently.

## Tier 1 (always acceptable)
- Journals: IEEE TPAMI, IEEE TIP, IJCV, IEEE TAFFC, IEEE TMM, IEEE TNNLS,
  IEEE TCSVT, JMLR, Pattern Recognition.
- Conferences: CVPR, ICCV, ECCV, NeurIPS, ICML, ICLR, AAAI, IJCAI, ACM MM.

## Tier 2 (acceptable; prefer Tier 1 when equivalents exist)
- Journals: Neurocomputing, Pattern Recognition Letters, IEEE Access is NOT
  in this tier (see denied), Image and Vision Computing, Computer Vision and
  Image Understanding, IEEE Transactions on Biometrics, Behavior, and
  Identity Science.
- Conferences: BMVC, WACV, ACCV, ICASSP, ICIP, INTERSPEECH.
- Field-standard exceptions: IEEE FG (standard venue for face and gesture
  work despite mid-tier metrics).

## Denied by default (user approval required, case by case)
- arXiv-only entries (see L3 interception in `citations-policy.md`): only
  when no published version exists AND the artifact is necessary (dataset,
  tool, or the single defining reference of a method under comparison).
- IEEE Access, MDPI journals (Sensors, Applied Sciences, Electronics, ...),
  Hindawi journals, workshops without archival proceedings, national
  conferences, predatory or pay-to-publish venues.

## Application notes
1. The gate applies to NEW references being added. Pre-existing entries in a
   user's .bib are reported, not deleted; removal is the user's call.
2. Datasets and toolboxes are cited by their canonical paper wherever one
   exists (search the index first); cite a URL or arXiv only as a last
   resort with user approval.
3. Venue names in the .bib must match the tier list's canonical naming (one
   convention across the file; L4).
