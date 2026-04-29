#!/usr/bin/env python3
"""Generate Hinglish companion .md files mirroring docs/book/src (except SUMMARY)."""
from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BOOK_SRC = REPO / "docs" / "book" / "src"
OUT_ROOT = REPO / "contrib-notes" / "book-hinglish" / "src"


def title_from_relpath(rel: str) -> str:
    stem = Path(rel).stem.replace("-", " ").replace("_", " ")
    return stem.title() if stem else rel


def official_link(rel: str) -> str:
    depth = len(Path(rel).parts)
    up = "../" * (depth + 3)
    return f"{up}docs/book/src/{rel}"


def hinglish_blurb(rel: str) -> str:
    r = rel.lower()
    if r == "introduction.md":
        return (
            "Cluster API kya hai, kyun use karte hain—high-level intro. "
            "Official page pe poori English story hai; yahan sirf *feel* pakdo."
        )
    if r.startswith("user/"):
        return (
            "**User / operator zone** — cluster banane, chalane, samajhne wali baatein. "
            "Tum *consumer* ho CAPI ka: YAML, clusterctl, concepts."
        )
    if r.startswith("developer/"):
        return (
            "**Developer / contributor zone** — code, controllers, providers, tests. "
            "Tum *banane wale* ho ya codebase padhne wale."
        )
    if r.startswith("tasks/"):
        return (
            "**How-to tasks** — step-style guides (upgrade, certs, bootstrap, …). "
            "English page detailed steps; yahan *kis cheez ka task hai* clear karo."
        )
    if r.startswith("clusterctl/"):
        return (
            "**clusterctl CLI** — management cluster setup, templates, kubeconfig. "
            "Har sub-page ek command ya topic."
        )
    if r.startswith("reference/"):
        return (
            "**Reference** — API, glossary, versions, ports: *lookup* material. "
            "Padhna boring lag sakta hai par debug time pe gold."
        )
    if r.startswith("security/"):
        return "**Security** — PSS, guidelines; production mein zaroori."
    if r in ("contributing.md", "reviewing.md", "code-of-conduct.md"):
        return "**Community / legal** — contribute kaise karein, code of conduct."
    return (
        "Is path ka official English documentation niche link par hai. "
        "Neeche ek line mein *theme* samjho, phir original kholo."
    )


def page_body(rel: str) -> str:
    title = title_from_relpath(rel)
    ol = official_link(rel)
    blurb = hinglish_blurb(rel)
    return f"""# {title} — simple notes

> **Hinglish / short:** {blurb}

## Official English (source of truth)

- Repo file: [`docs/book/src/{rel}`]({ol})
- Published book (same content, rendered): open path under [cluster-api.sigs.k8s.io](https://cluster-api.sigs.k8s.io) (e.g. replace `.md` with `.html` in URL path).

## Folder / page ka matlab

Yeh file **book ke isi path** ka companion hai: `{rel}`  
Structure match isliye hai taaki tum `docs/book/src` jaisa hi tree `contrib-notes/book-hinglish/src` mein dhundh sako.

---

*Personal notes — `contrib-notes`. Official project docs upstream repo mein hain.*
"""


def main() -> None:
    if not BOOK_SRC.is_dir():
        raise SystemExit(f"Missing {BOOK_SRC}")

    for path in sorted(BOOK_SRC.rglob("*.md")):
        rel = path.relative_to(BOOK_SRC).as_posix()
        if rel == "SUMMARY.md":
            continue
        out = OUT_ROOT / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page_body(rel), encoding="utf-8")

    print(f"Wrote mirror under {OUT_ROOT}")


if __name__ == "__main__":
    main()
