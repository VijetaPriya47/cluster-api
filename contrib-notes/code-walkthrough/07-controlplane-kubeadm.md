# `controlplane/kubeadm/` — KubeadmControlPlane provider

> **Hinglish:** *HA control plane Machines + rollout—etcd aur static pods wali story yahi reconcile hoti hai.*

## Purpose

Reference **control plane provider**: types in [`api/controlplane/kubeadm`](../../api/controlplane/kubeadm); reconciler in [`controlplane/kubeadm/internal/controllers/controller.go`](../../controlplane/kubeadm/internal/controllers/controller.go); manifests under [`controlplane/kubeadm/config/`](../../controlplane/kubeadm/config/).

## Start reading here

- [`controlplane/kubeadm/main.go`](../../controlplane/kubeadm/main.go) — KCP manager binary
- [`controlplane/kubeadm/internal/controllers/controller.go`](../../controlplane/kubeadm/internal/controllers/controller.go) — `KubeadmControlPlaneReconciler.Reconcile`

## Execution path

Get **KCP** → **finalizer** → resolve **owner Cluster** → pause → reconcile **Machine** count, **version** rollouts, **etcd** membership / remediation (later in the same file and helpers).

## Official docs

- [Control plane contract](https://cluster-api.sigs.k8s.io/developer/providers/contracts/control-plane.html)
- [Kubeadm control plane (user)](https://cluster-api.sigs.k8s.io/tasks/control-plane/kubeadm-control-plane.html)

## See also

- [03 — `internal/controllers`](03-internal-controllers.md) (core vs KCP boundary)
