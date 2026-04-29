# `config/` — generated install manifests (core)

> **Hinglish:** *CRD, RBAC, Deployment, webhook Service—`make generate-manifests` se aate hain; prod mein kustomize/overlay se install.*

## Purpose

Kustomize **bases** for the **core** Cluster API provider:

- [`config/crd/bases/`](../../config/crd/bases/) — per-kind CRD YAML
- [`config/rbac/`](../../config/rbac/) — from `+kubebuilder:rbac` markers
- [`config/manager/`](../../config/manager/) — Deployment for core manager
- [`config/webhook/`](../../config/webhook/) — webhook Service + certs hooks

Provider copies live under `bootstrap/kubeadm/config/`, `controlplane/kubeadm/config/`, CAPD, etc.

## Start reading here

- [`config/crd/kustomization.yaml`](../../config/crd/kustomization.yaml) — lists all shipped core CRDs + webhook patches
- Root [`config/kustomization.yaml`](../../config/kustomization.yaml) if present for full install

## Official docs

- [Repository layout — config](https://cluster-api.sigs.k8s.io/developer/core/repository-layout.html#manifest-generation)

## See also

- [02 — `api/`](02-api.md)
