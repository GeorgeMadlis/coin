# Committed Bundles

This directory contains public bundle snapshots used as evidence for the inquiry-to-procedure
research trail. The bundle HTML files are derived inspection views; the authoritative source state
is the committed bundle source/provenance state recorded by each bundle's Markdown, `bundle.json`
where present, and published `manifest.json`.

## Downloading and exploring bundle metadata locally

A bundle can be downloaded or cloned to a local computer and opened directly in a browser. Start
with the bundle's `index.html` when a generated HTML entry point is present, or `index.md` when only
Markdown has been committed.

Generated HTML pages contain ordinary relative links to:

- the JSON metadata sidecar for that page under `metadata/`;
- the bundle-level published `manifest.json`;
- the COIN-local `metadata/local-metadata-manifest.json` that inventories page sidecars and
  checksums.

Because these links are relative and self-contained within the downloaded bundle, the page metadata,
bundle manifests, checksums, and copied provenance artifacts can be explored locally/offline after
download. External citations, remote datasets, source repositories, and live services referenced by
the metadata are provenance pointers; they are not necessarily bundled for offline access.
