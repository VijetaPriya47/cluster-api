# 03 — Core API (`api/core/`)

The **core** API is the **portable contract** for Cluster API: objects every provider implements against, with cloud-specific details pushed into **referenced** CRs.

> **Hinglish:** *`api/core` woh “common language” hai jo har cloud follow karta hai—AWS/GCP ka detail `infrastructureRef` jaise alag CR mein chhupa rehta hai. Isse portability milti hai: same `Cluster`/`Machine` story, alag provider.*

## What lives here?

- Versioned packages, e.g. `api/core/v1beta2/`.
- Files like `cluster_types.go`, `machine_types.go`, `machinedeployment_types.go`, `clusterclass_types.go`, etc.
- Generated companions: `zz_generated.deepcopy.go`, conversion files, OpenAPI where applicable.

## `Cluster`: the workload cluster’s handle

The `Cluster` type embeds standard Kubernetes metadata and splits **desired** vs **observed** state (see [reading guide](./02-reading-go-code.md) for the struct).

**Real-world analogy:** `Cluster` is the **folder tab** in a filing cabinet labeled “Prod EU”—it points to **infrastructure** (lot) and **control plane** (frame) documents without caring if those are AWS or vSphere.

**DevOps angle:** In GitOps you commit `Cluster` YAML; controllers create/update/delete underlying provider CRs and Machines.

## `Machine`: one host, one Node goal

```805:818:api/core/v1beta2/machine_types.go
type Machine struct {
	metav1.TypeMeta `json:",inline"`
	// metadata is the standard object's metadata.
	// More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
	// +optional
	metav1.ObjectMeta `json:"metadata,omitempty"`

	// spec is the desired state of Machine.
	// +required
	Spec MachineSpec `json:"spec,omitempty,omitzero"`
	// status is the observed state of Machine.
	// +optional
	Status MachineStatus `json:"status,omitempty,omitzero"`
}
```

**Meaning:** A `Machine` ties together:

- **`infrastructureRef`**: “Create this VM/network attachment” (provider-specific).
- **`bootstrap` configRef**: “On first boot, run this kubeadm/cloud-init story.”

The **Machine controller** waits for infra + bootstrap data, coordinates creation order, and writes **conditions** and **`nodeRef`** when the Node registers.

**Immutability (conceptual):** Spec changes usually roll out by **replacing** Machines (new object), not patching in place—safer for etcd and kubelet state.

## Conditions

Types implement helpers like `GetConditions` / `SetConditions` so automation and `kubectl` can answer: *Is the cluster available? Is the control plane ready?*

Condition constants (e.g. `ClusterAvailableCondition`) document **which signals** roll up into user-visible health—read `cluster_types.go` near those constants for precise semantics.

## Why multiple API versions (`v1beta1`, `v1beta2`)?

Kubernetes APIs **evolve**. Older versions remain for compatibility while newer versions add fields or cleaner shapes. Conversion webhooks and Go conversion code migrate stored objects between versions.

**What to study in this folder:**

1. `ClusterSpec` / `ClusterStatus`—how topology and `ClusterClass` attach.
2. `MachineSpec`—how `clusterName`, `version`, and refs work.
3. `MachineDeployment`—rollout fields mirroring Deployments.

> **Hinglish:** *Machine usually immutable hoti hai—matlab spec badli toh aksar *naya* Machine banega, purana replace hoga; ye blast radius control karta hai, thoda pets-wala SSH culture kam.*

**Next:** [Addons, IPAM, Runtime](./04-api-addons-ipam-runtime.md).
