# `internal/controllers/` — reconciliation implementations

> **Hinglish:** *Asli “kaam” yahi hota hai—har resource ka `Reconcile`, finalizers, pause, status patch. Ye `internal` hai taaki public Go API chhota rahe.*

## Purpose

One package per domain: `cluster`, `machine`, `machinedeployment`, `machineset`, topology under `topology/`, `clusterresourceset`, etc. Each exposes a **`Reconciler`** with `SetupWithManager` and **`Reconcile(ctx, req)`**.

## Start reading here

- [`internal/controllers/cluster/cluster_controller.go`](../../internal/controllers/cluster/cluster_controller.go) — RBAC markers + `Reconcile`
- [`internal/controllers/machine/machine_controller.go`](../../internal/controllers/machine/machine_controller.go)

## Execution path (Cluster controller)

Fetch object → not found / error handling → **EnsureFinalizer** → **patch helper** → **pause** check → load **ClusterClass** if topology → defer **updateStatus**. Same structural pattern repeats across controllers.

## Official docs

- [Controllers overview](https://cluster-api.sigs.k8s.io/developer/core/controllers/overview.html)
- Per-controller book pages under [Controllers](https://cluster-api.sigs.k8s.io/developer/core/controllers/cluster.html)

## See also

- [04 — Public `controllers`](04-controllers-public.md)
