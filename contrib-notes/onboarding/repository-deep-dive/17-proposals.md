# 17 — Design proposals (`docs/proposals/`)

Large behavioral and API changes in Cluster API go through **CAEPs** (Cluster API Enhancement Proposals)—Markdown design docs reviewed before implementation lands.

> **Hinglish:** *CAEP = “pehle design likho, phir code”—bada change bina RFC jaisa doc ke risky hota hai; yahan community trade-offs discuss karti hai.*

## What you will find

- Problem statements, goals, non-goals.
- API sketches and migration plans.
- Security and operational impact discussions.

## How to use this folder

**As a contributor:** Open a proposal **before** sweeping API changes; link the eventual PR to the CAEP.

**As a DevOps engineer:** Read CAEPs when a release note mentions behavior you don’t recognize—understanding **intent** beats guessing from YAML diffs alone.

**As a student:** Compare **proposal → code → tests** to see how design documents translate into production systems.

**Concrete workflow:** See [CONTRIBUTING.md — Proposal process (CAEP)](https://github.com/kubernetes-sigs/cluster-api/blob/main/CONTRIBUTING.md).

**Next:** [Developer book source](./18-dev-book.md).
