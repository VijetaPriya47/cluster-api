# `feature/` — feature gates

> **Hinglish:** *Experimental cheezein flag se band/chalu—`main.go` mein `feature.Gates.Enabled(...)` dekhoge.*

## Purpose

Central **feature gate** registration for Cluster API: gates defined in [`feature/feature.go`](../../feature/feature.go) (or adjacent files), checked from controllers and webhooks before enabling new paths.

## Start reading here

- [`feature/`](../../feature/) — package docs and gate identifiers
- Grep: `feature.Gates.Enabled` across [`main.go`](../../main.go) and controllers

## Official docs

- [Experimental features](https://cluster-api.sigs.k8s.io/tasks/experimental-features/experimental-features.html)

## See also

- [16 — `exp/`](16-exp.md)
