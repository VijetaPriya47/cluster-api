# `internal/` — non-controller support packages

> **Hinglish:** *Controllers ke alawa bhi `internal` mein topology helpers, runtime registry, contract, setup—yeh sab “engine room” hai.*

## Purpose

Packages **not** under `internal/controllers/` but still **not public API**:

- **`internal/topology/`** — ClusterClass / rollout upgrade logic shared with tests
- **`internal/runtime/`** — runtime extension registry, clients
- **`internal/contract/`** — provider contract helpers
- **`internal/setup/`** — manager setup pieces
- **`internal/webhooks/`** — see [05 — Webhooks](05-webhooks.md)

## Start reading here

- Grep imports from `main.go`: `internal/setup`, `internal/runtime`, `internal/contract`
- [`internal/topology/`](../../internal/topology/) when debugging ClusterClass upgrades

## See also

- [03 — `internal/controllers`](03-internal-controllers.md)
