# `bootstrap/kubeadm/` — CABPK

> **Hinglish:** *Kubeadm bootstrap provider—`KubeadmConfig` se cloud-init/Ignition + join/init data banata hai.*

## Purpose

Reference **bootstrap provider**: API types under [`api/bootstrap/kubeadm`](../../api/bootstrap/kubeadm); controllers under [`bootstrap/kubeadm/internal/controllers`](../../bootstrap/kubeadm/internal/controllers) (e.g. `KubeadmConfigReconciler`); own [`bootstrap/kubeadm/config/`](../../bootstrap/kubeadm/config/) for generated manifests.

## Start reading here

- [`bootstrap/kubeadm/internal/controllers/kubeadmconfig_controller.go`](../../bootstrap/kubeadm/internal/controllers/kubeadmconfig_controller.go) — `Reconcile`
- [`bootstrap/kubeadm/main.go`](../../bootstrap/kubeadm/main.go) — kubeadm bootstrap **controller-manager** entrypoint

## Execution path

Resolve owning **Machine** / pool → load **Cluster** → respect **pause** → generate **bootstrap data** / Secrets → set **conditions**.

## Official docs

- [Bootstrap provider contract](https://cluster-api.sigs.k8s.io/developer/providers/contracts/bootstrap-config.html)

## See also

- [02 — `api/`](02-api.md)
- [08 — `config/`](08-config.md)
