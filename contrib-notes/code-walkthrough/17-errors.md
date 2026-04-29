# `errors/` — CAPI error helpers

> **Hinglish:** *Typed errors / reasons jo conditions aur logs mein consistent dikhein.*

## Purpose

Shared **error types and constructors** for Cluster API controllers (e.g. terminal vs retryable semantics where applicable). Imported as `capierrors` or `sigs.k8s.io/cluster-api/errors`.

## Start reading here

- [`errors/doc.go`](../../errors/doc.go) — package overview
- [`errors/consts.go`](../../errors/consts.go), [`errors/machines.go`](../../errors/machines.go) — kind-specific helpers

## See also

- [03 — `internal/controllers`](03-internal-controllers.md) (usage sites)
