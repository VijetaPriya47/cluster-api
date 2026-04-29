# 04 — Addons, IPAM, and Runtime API

Cluster API keeps **core** minimal and pushes optional features into **separate API groups**. Three important ones:

> **Hinglish:** *Core chhota rakha gaya hai taaki “zaroori cheez” stable rahe; add-ons/IPAM/runtime alag groups mein hain—matlab optional features core ko heavy nahi karte.*

## `api/addons/` — day-2 add-ons

**Problem:** After a cluster exists, you often need to apply CNI manifests, metrics scrapers, or internal tools—but you want that **declarative** and **repeatable**.

**Example type:** `ClusterResourceSet` selects clusters by **labels** and applies resources from Secrets/ConfigMaps.

```54:74:api/addons/v1beta2/clusterresourceset_types.go
// ClusterResourceSetSpec defines the desired state of ClusterResourceSet.
type ClusterResourceSetSpec struct {
	// clusterSelector is the label selector for Clusters. The Clusters that are
	// selected by this will be the ones affected by this ClusterResourceSet.
	// It must match the Cluster labels. This field is immutable.
	// Label selector cannot be empty.
	// +required
	ClusterSelector metav1.LabelSelector `json:"clusterSelector,omitempty,omitzero"`

	// resources is a list of Secrets/ConfigMaps where each contains 1 or more resources to be applied to remote clusters.
	// +required
	// +listType=atomic
	// +kubebuilder:validation:MinItems=1
	// +kubebuilder:validation:MaxItems=100
	Resources []ResourceRef `json:"resources,omitempty"`

	// strategy is the strategy to be used during applying resources. Defaults to ApplyOnce. This field is immutable.
	// +kubebuilder:validation:Enum=ApplyOnce;Reconcile
	// +optional
	Strategy string `json:"strategy,omitempty"`
}
```

**Reading the code:**

- **`ClusterSelector`**: Only clusters whose labels match get these manifests—think **GitOps for fleet segmentation** (“everything tagged `env=prod` gets policy bundle X”).
- **`Resources`**: Pointers to Secrets/ConfigMaps holding YAML blobs; caps (`MaxItems=100`) prevent accidental huge objects.
- **`Strategy`**: `ApplyOnce` vs `Reconcile` controls whether the controller **re-applies** when sources change.

**Security note:** A dedicated Secret **type** is enforced for CRS (`ClusterResourceSetSecretType`) so random Secret types are rejected—reduces foot-guns.

## `api/ipam/` — IP address management

**Problem:** Some infrastructures need per-machine IP allocation beyond a single static CIDR in `Cluster.spec.clusterNetwork`.

**What you get:** CRDs like `IPAddressClaim` / `IPAddress` (see `config/crd/kustomization.yaml` listing `ipam.cluster.x-k8s.io_*`). Providers or IPAM controllers allocate addresses and record them as objects—auditable and race-aware compared to ad hoc scripts.

## `api/runtime/` — ExtensionConfig and hooks

**Problem:** Large enterprises need **policy hooks** (approve mutations, lifecycle checks) without forking core CAPI.

**What you get:** Types such as `ExtensionConfig` (in CRD list: `runtime.cluster.x-k8s.io_extensionconfigs.yaml`) describe how to reach **HTTP extension** services. Feature-gated controllers (e.g. in `main.go` when `RuntimeSDK` is enabled) register and call those extensions.

**DevOps angle:** You can enforce naming standards, inject labels, or gate upgrades centrally—*provided* you operate the extension services securely (TLS, authn/z).

> **Hinglish:** *ClusterResourceSet = “jin clusters pe ye labels hain, unpe ye manifests laga do”; IPAM = IP allocate karne ka formal tareeka; Runtime SDK = bina core fork kiye policy/hooks lagana.*

**Next:** [Bootstrap kubeadm API](./05-api-bootstrap-kubeadm.md).
