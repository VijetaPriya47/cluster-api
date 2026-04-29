# Book mirror — Hinglish / simple notes

This tree **mirrors** [`docs/book/src/`](../../docs/book/src/) **path-for-path**. Each `.md` here is a **companion** to the official English page: short **Hinglish / simple** explanation + link to the real source in the repo and the [published book](https://cluster-api.sigs.k8s.io).

- **Not official.** Not published to cluster-api.sigs.k8s.io.
- **How to use:** Open the same path under `contrib-notes/book-hinglish/src/` as in `docs/book/src/`, read the simple summary, then open the official file if you need full detail.

Navigation: [`src/SUMMARY.md`](src/SUMMARY.md) (same structure as the book’s `SUMMARY.md`, links point to these companion files).

To regenerate stubs after adding new book pages, run:

```bash
python3 contrib-notes/book-hinglish/generate_mirror.py
```
