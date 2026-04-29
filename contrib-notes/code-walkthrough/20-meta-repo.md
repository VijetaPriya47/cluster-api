# Meta: `.github/`, `docs/proposals/`, `docs/book/`

> **Hinglish:** *Code nahi, par project ka “law & constitution”—CI, CAEP, published book.*

## `.github/`

Workflows, issue/PR templates, **Prow** interacts via `kubernetes/test-infra` too—local copy shows lint/test jobs hints.

## `docs/proposals/`

**CAEPs** — design before large API/behavior changes. Read when a release surprises you.

## `docs/book/src/`

Official **mdBook** source published at [cluster-api.sigs.k8s.io](https://cluster-api.sigs.k8s.io). Your **`contrib-notes/`** deliberately stays **outside** this tree.

## Official docs

- [CONTRIBUTING.md — CAEP](https://github.com/kubernetes-sigs/cluster-api/blob/main/CONTRIBUTING.md#proposal-process-caep)

## See also

- [contrib-notes README](../README.md)
