# `hack/` and `scripts/` — tooling and CI glue

> **Hinglish:** *Makefile jo scripts bulata hai—verify, release notes, tools vendor—yahan zyada “robot work” hai.*

## Purpose

- **`hack/`** — development scripts, `tools` module pins, observability configs, version helpers (`hack/version.sh`), linters wrappers
- **`scripts/`** — CI entrypoints (`ci-e2e.sh`, etc.) invoked by Prow / local dev

## Start reading here

- Root [`Makefile`](../../Makefile) — see which `hack/` or `scripts/` targets are called
- [`scripts/ci-e2e.sh`](../../scripts/ci-e2e.sh) — repro CI e2e locally

## Official docs

- [Testing](https://cluster-api.sigs.k8s.io/developer/core/testing.html) (CI hints)

## See also

- [01 — `main.go`](01-main-and-manager.md) (build flags from `hack/version.sh`)
