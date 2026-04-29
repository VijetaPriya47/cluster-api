# `test/framework/` — shared e2e / integration helpers

> **Hinglish:** *Ginkgo tests ka “toolbox”—clusterctl config load, cluster proxy, bootstrap cluster—taaki `test/e2e` aur provider e2e duplicate kam likhein.*

## Purpose

Libraries used by [`test/e2e`](11-test-e2e.md) and downstream provider tests: **ClusterProxy**, **clusterctl** helpers, **E2EConfig** parsing, log streaming, etc.

## Start reading here

- [`test/framework/clusterctl/e2e_config.go`](../../test/framework/clusterctl/e2e_config.go) — `LoadE2EConfig`, `E2EConfig` struct
- [`test/framework/doc.go`](../../test/framework/doc.go) if present for package overview

## Execution path

Tests call `LoadE2EConfig` → YAML → `ResolveReleases` → `Validate` → use config to install providers and drive **clusterctl** flows.

## Official docs

- [Developing E2E](https://cluster-api.sigs.k8s.io/developer/core/e2e.html)
- [Testing](https://cluster-api.sigs.k8s.io/developer/core/testing.html)

## See also

- [11 — `test/e2e`](11-test-e2e.md)
