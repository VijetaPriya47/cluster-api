# `api/` — CR types and contracts

> **Hinglish:** *Yahan “forms” define hote hain jo users apply karte hain—`Cluster`, `Machine`, IPAM, addons, runtime. Yehi se CRD YAML generate hota hai.*

## Purpose

Versioned **Go structs** for all core Cluster API kinds: `spec` / `status`, kubebuilder **validation markers**, condition helpers, and sometimes **defaulting** adjacent code. Companion generated files: `zz_generated.deepcopy.go`, conversions, OpenAPI pieces.

## Start reading here

- [`api/core/v1beta2/cluster_types.go`](../../api/core/v1beta2/cluster_types.go) — `Cluster`, finalizers, condition constants
- [`api/core/v1beta2/machine_types.go`](../../api/core/v1beta2/machine_types.go) — `Machine`
- [`api/bootstrap/kubeadm/v1beta2/`](../../api/bootstrap/kubeadm/v1beta2/) — bootstrap API
- [`api/controlplane/kubeadm/v1beta2/`](../../api/controlplane/kubeadm/v1beta2/) — KCP API

## How it connects

- **`controller-gen`** reads `+kubebuilder` markers here and emits [`config/crd/bases`](../../config/crd/bases).
- Controllers in [`internal/controllers`](03-internal-controllers.md) import these types as `clusterv1`, `bootstrapv1`, etc.

## Official docs

- [API design / versioning](https://github.com/kubernetes-sigs/cluster-api/blob/main/CONTRIBUTING.md#apis)
- [Concepts — Cluster / Machine](https://cluster-api.sigs.k8s.io/user/concepts.html)

## See also

- [08 — `config/`](08-config.md)
