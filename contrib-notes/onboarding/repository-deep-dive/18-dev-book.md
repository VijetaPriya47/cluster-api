# 18 — Developer book source (`docs/book/src/`)

The documentation you are reading is built from **Markdown** in `docs/book/src/` using **mdBook** (see `make serve-book`).

> **Hinglish:** *Jo tum ab padh rahe ho woh bhi isi folder se banta hai—docs code ke saath review hote hain, alag wiki nahi.*

## Key files

- **`SUMMARY.md`**: Table of contents and nesting—this chapter appears because it is listed there.
- **`developer/repository-deep-dive/`**: The per-section pages you are reading now.

## Why this matters

- **Docs-as-code:** Doc fixes ride the same review process as code.
- **Linkability:** Official site [cluster-api.sigs.k8s.io](https://cluster-api.sigs.k8s.io) publishes these pages.

**Contributor tip:** After editing Markdown, run `make serve-book` locally to verify links and formatting.

**Next:** [Architecture guarantees](./19-architecture.md).
