# 05 — Kubeadm bootstrap API (`api/bootstrap/kubeadm/`)

The **bootstrap provider** turns “I want this kubeadm/cloud-init shape” into **bootstrap data** the infrastructure layer feeds into a new Machine (usually via cloud-init or Ignition).

> **Hinglish:** *Bootstrap = VM pe pehli boot par “kya run ho” (cloud-init/Ignition + kubeadm join/init). Ye layer bina iske sirf “khali VM” hai, Node nahi.*

## `Format`: cloud-config vs Ignition

```30:40:api/bootstrap/kubeadm/v1beta2/kubeadmconfig_types.go
// Format specifies the output format of the bootstrap data
// +kubebuilder:validation:Enum=cloud-config;ignition
type Format string

const (
	// CloudConfig make the bootstrap data to be of cloud-config format.
	CloudConfig Format = "cloud-config"

	// Ignition make the bootstrap data to be of ignition format.
	Ignition Format = "ignition"
)
```

**Meaning:** Linux images expect different **first-boot** formats. CAPA might use cloud-config; some metal/flatcar flows use Ignition. The API forces a **small enum** so invalid strings are rejected at admission time.

## `KubeadmConfigSpec`: init vs join

```52:66:api/bootstrap/kubeadm/v1beta2/kubeadmconfig_types.go
// KubeadmConfigSpec defines the desired state of KubeadmConfig.
// Either ClusterConfiguration and InitConfiguration should be defined or the JoinConfiguration should be defined.
// +kubebuilder:validation:MinProperties=1
type KubeadmConfigSpec struct {
	// clusterConfiguration along with InitConfiguration are the configurations necessary for the init command
	// +optional
	ClusterConfiguration ClusterConfiguration `json:"clusterConfiguration,omitempty,omitzero"`

	// initConfiguration along with ClusterConfiguration are the configurations necessary for the init command
	// +optional
	InitConfiguration InitConfiguration `json:"initConfiguration,omitempty,omitzero"`

	// joinConfiguration is the kubeadm configuration for the join command
	// +optional
	JoinConfiguration JoinConfiguration `json:"joinConfiguration,omitempty,omitzero"`
```

**Reading the code:**

- **`MinProperties=1`**: You cannot create an empty KubeadmConfig—either **init** path or **join** path must be present. That matches kubeadm’s real CLI: `kubeadm init` vs `kubeadm join`.
- Nested types mirror **kubeadm’s own config** shapes so users can copy working kubeadm YAML into CRs.

Further down the same file (not fully quoted here) you will find **`Files`**, **`DiskSetup`**, **`Mounts`**, **`bootCommands`**, etc.—all the knobs you would normally embed in cloud-init user-data, now **versioned in Git**.

## Relationship to controllers

Types live under `api/bootstrap/kubeadm/`. The controller that **implements** reconciliation is under `bootstrap/kubeadm/internal/controllers/` (see [Bootstrap controllers](./10-bootstrap-controllers.md)).

**DevOps engineer:** You rarely SSH to wire up `kubeadm`; you tune `KubeadmConfigTemplate` objects and let Machines pick up the right bootstrap reference.

**Security:** Join tokens and certs must flow through **Kubernetes Secrets**; never paste long-lived tokens into `Machine` labels.

> **Hinglish:** *`MinProperties=1` ka matlab: khali KubeadmConfig allow nahi—ya to init story ya join story honi chahiye; warna kubeadm ko pata hi nahi chalega kya karna hai.*

**Next:** [Control plane kubeadm API](./06-api-controlplane-kubeadm.md).
