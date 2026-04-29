# `webhooks/` and `internal/webhooks/` — admission

> **Hinglish:** *API server object save karne se pehle validate/default—galat `Cluster` andar na jaaye, ya default fields bhar jayein.*

## Purpose

- **`webhooks/`** — exported admission handlers for some types (package doc: “external webhook implementations”).
- **`internal/webhooks/`** — additional internal admission logic; tests often under `internal/webhooks/test/`.

## Start reading here

- [`webhooks/doc.go`](../../webhooks/doc.go)
- Grep for `SetupWebhookWithManager` or `Defaulter` / `Validator` in [`webhooks/`](../../webhooks/) and [`internal/webhooks/`](../../internal/webhooks/)

## How it connects

- `controller-gen` + CRD patches under [`config/crd`](../../config/crd) point CRDs at the **webhook Service** the manager runs.
- [`main.go`](01-main-and-manager.md) registers webhooks on the same **Manager** as controllers.

## Official docs

- [Webhooks (provider getting started)](https://cluster-api.sigs.k8s.io/developer/providers/getting-started/webhooks.html)

## See also

- [08 — `config/`](08-config.md)
