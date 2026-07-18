<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->
<!-- Copy this file to local/config.md and fill in machine-specific values.
     Everything under local/ except this example is gitignored: private
     paths and unpublished-work pointers never enter the repository. -->

# Local Configuration (machine-specific, never shipped)

## golden_sample_path
Absolute path to a locally available manuscript that exemplifies the house
rules (may be unpublished; the suite reads the manuscript as a living
exemplar but never copies content from the manuscript into any shipped or
generated artifact).

golden_sample_path: /absolute/path/to/exemplar/main.tex

## exemplar_pdf_dir
Directory of published exemplar PDFs for on-demand quote mining with
pdftotext (see core/templates/exemplar-patterns.md).

exemplar_pdf_dir: /absolute/path/to/exemplar/pdfs

## crossref_mailto
Contact email appended to Crossref queries (polite-pool etiquette).

crossref_mailto: you@example.org

## leak_patterns
Maintainers: create local/leak-patterns.txt with one private pattern per
line (unpublished method names, machine paths, distinctive numbers) and run
scripts/leak_scan.sh before every release.
