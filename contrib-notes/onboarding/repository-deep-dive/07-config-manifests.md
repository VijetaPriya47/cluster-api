# 07 — Core manifests (`config/`)

The `config/` directory is how the **core Cluster API provider** is **packaged** for installation: CRDs, RBAC, manager Deployment, webhooks—all **kustomize** bases, mostly **generated** from Go markers.

> **Hinglish:** *`config/` basically “install pack” hai—CRD se API server ko naye kinds milte hain, RBAC batata hai controller ko kaunsi permission, webhook validation/defaulting handle karta hai. Haath se YAML kam, zyada generate hota hai.*

## CRD kustomization: what gets installed

`config/crd/kustomization.yaml` lists every **core** CRD base file that ships together:

```1:18:config/crd/kustomization.yaml
# This kustomization.yaml is not intended to be run by itself,
# since it depends on service name and namespace that are out of this kustomize package.
# It should be run by config/
resources:
- bases/cluster.x-k8s.io_clusterclasses.yaml
- bases/cluster.x-k8s.io_clusters.yaml
- bases/cluster.x-k8s.io_machines.yaml
- bases/cluster.x-k8s.io_machinesets.yaml
- bases/cluster.x-k8s.io_machinedeployments.yaml
- bases/cluster.x-k8s.io_machinedrainrules.yaml
- bases/cluster.x-k8s.io_machinepools.yaml
- bases/addons.cluster.x-k8s.io_clusterresourcesets.yaml
- bases/addons.cluster.x-k8s.io_clusterresourcesetbindings.yaml
- bases/cluster.x-k8s.io_machinehealthchecks.yaml
- bases/runtime.cluster.x-k8s.io_extensionconfigs.yaml
- bases/ipam.cluster.x-k8s.io_ipaddresses.yaml
- bases/ipam.cluster.x-k8s.io_ipaddressclaims.yaml
# +kubebuilder:scaffold:crdkustomizeresource
```

**Reading this file:**

- Each line under `resources:` is a **generated** OpenAPI schema for one Kind.
- Groups (`cluster.x-k8s.io`, `addons.cluster.x-k8s.io`, …) match the **api** packages in Go.
- The comment **`+kubebuilder:scaffold:crdkustomizeresource`** is a hook for kubebuilder tooling when you add new types—teaches you that CRD lists are **maintained mechanically**, not by hand.

## Webhook patches

The same file continues with `patches:` entries such as `webhook_in_clusters.yaml`. Those patches **teach each CRD** where to send **conversion** or **defaulting/validation** webhook traffic—wired to the Service created under `config/webhook/`.

## Other `config/` subtrees (mental model)

- **`config/manager/`**: Deployment for `cluster-api-controller-manager` (image, args, service account).
- **`config/rbac/`**: `ClusterRole` + bindings produced from `+kubebuilder:rbac` markers.
- **`config/certmanager/`**: Optional issuer/cert resources when you use cert-manager for webhook certs.

**DevOps engineer:** You rarely edit `bases/*.yaml` by hand—change Go types or markers, run `make generate-manifests`, then use your GitOps overlay for namespaces, resource limits, and image digests.

> **Hinglish:** *Scaffold comment dekhoge to samajh aayega: naya CRD jodo to tooling isi list mein entry bhi suggest karti hai—manual typo kam.*

**Next:** [`internal/controllers`](./08-internal-controllers.md).
