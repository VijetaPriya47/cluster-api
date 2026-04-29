# `test/e2e/` — Ginkgo end-to-end suite

> **Hinglish:** *Poora flow test—kind + providers + clusterctl; `-tags=e2e` se alag build.*

## Purpose

Production-like **journey tests**: suite setup in [`test/e2e/e2e_suite_test.go`](../../test/e2e/e2e_suite_test.go) (`//go:build e2e`), specs in sibling `*_test.go` files, driven by **config YAML** (default often `test/e2e/config/docker.yaml`).

## Start reading here

- [`test/e2e/e2e_suite_test.go`](../../test/e2e/e2e_suite_test.go) — flags, global `e2eConfig`, bootstrap cluster
- Individual specs e.g. quick start / upgrade tests (browse directory)

## Execution path

`init` registers flags → `SynchronizedBeforeSuite` builds management cluster + providers → Ginkgo **specs** run → cleanup.

## Running

`make test-e2e` from repo root (see Makefile for `GINKGO_*` variables).

## Official docs

- [Developing E2E tests](https://cluster-api.sigs.k8s.io/developer/core/e2e.html)

## See also

- [10 — `test/framework`](10-test-framework.md)
- [13 — envtest](13-envtest.md) (lighter tests)
