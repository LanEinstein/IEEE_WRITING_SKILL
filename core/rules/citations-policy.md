<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Citations: existence, metadata, and content (L1–L5)

## L1. Verify the actual support

Use primary publisher/proceedings/dataset/software/standard sources where possible. Locate author, title, venue/version, year, and DOI or another valid identifier, then read the relevant content to check the sentence's actual claim. Keep metadata verification separate from content support. No DOI or absent index hit does not establish nonexistence.

`scripts/verify_citations.py <references.bib> [--limit N] [--mailto address]` is an optional Crossref/OpenAlex metadata helper requiring Python and network access. Its fuzzy title/year/venue statuses require human interpretation. It does not read papers, enforce venue tiers, prove a DOI match, or establish scientific support. `NOT_FOUND`, `LOOKUP_ERROR`, `PARTIAL`, and mismatches remain pending until checked against appropriate sources.

## L2. Select by relevance and accurate credit

Find the closest methods by task, difficulty, assumption, and operation; follow references/citing work as needed. Record the mechanism, scope, relation to the current work, supporting passage, and status. Prefer originals for datasets, algorithms, protocols, and tools. An explicit author preference can guide selection but cannot justify inaccurate attribution; [venue-tiers.md](../literature/venue-tiers.md) explains the former tier list's status.

## L3. Handle versions explicitly

Check for a suitable published version of a preprint, and verify that it supports the same claim. Preprints, technical reports, workshops, standards, datasets, and software are not universally forbidden IEEE sources. Apply the target's current rules and actual source reliability/necessity. Do not invent a publication upgrade or require new permission for every legitimate source by default.

## L4. Bibliographic hygiene

Use stable keys, protect proper-name capitalization, unify venue naming, and check duplicate/missing/unresolved entries. Required fields depend on entry type and publication state: an early-access article may not yet have final pages. Do not fabricate volume/pages/DOI to satisfy a field checklist. Use the target template and [IEEE Reference Guide](https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/sites/7/IEEE_Reference_Guide.pdf) when relevant.

## L5. Unverified claims stay visible in drafts

Use `[CITE: precise support needed]` in a draft/review note. In TeX, avoid introducing an undefined coloring macro merely for a placeholder; plain bracketed text or an existing project macro is sufficient. Never guess citation keys or metadata. Resolve the support or accurately remove/narrow the dependent claim before submission; deleting only the marker is not resolution. Offline work continues on independently supported content with pending status stated honestly.
