# 06 — Kubeadm control plane API (`api/controlplane/kubeadm/`)

The **control plane provider** manages **how many control plane Machines** exist and how they roll forward on upgrades. The kubeadm implementation exposes **`KubeadmControlPlane`** (KCP).

> **Hinglish:** *Control plane = cluster ka “dimag” (API server, etcd, scheduler wagairah). KCP batata hai kitne control-plane nodes chahiye aur upgrade kaise rolling fashion mein ho—ye sensitive cheez hai, isliye strategy enum bhi tight hai.*

## Rollout strategy type

```28:36:api/controlplane/kubeadm/v1beta2/kubeadm_control_plane_types.go
// KubeadmControlPlaneRolloutStrategyType defines the rollout strategies for a KubeadmControlPlane.
// +kubebuilder:validation:Enum=RollingUpdate
type KubeadmControlPlaneRolloutStrategyType string

const (
	// RollingUpdateStrategyType replaces the old control planes by new one using rolling update
	// i.e. gradually scale up or down the old control planes and scale up or down the new one.
	RollingUpdateStrategyType KubeadmControlPlaneRolloutStrategyType = "RollingUpdate"
)
```

**Meaning:** Today the API **only** allows `RollingUpdate` as a strategy type—there is no “replace all at once” enum value. That reduces the chance of unsafe mass disruptions; the controller implements careful sequencing (etcd quorum, API availability).

## Finalizer and annotations (operations hints)

```38:66:api/controlplane/kubeadm/v1beta2/kubeadm_control_plane_types.go
const (
	// KubeadmControlPlaneFinalizer is the finalizer applied to KubeadmControlPlane resources
	// by its managing controller.
	KubeadmControlPlaneFinalizer = "kubeadm.controlplane.cluster.x-k8s.io"

	// SkipCoreDNSAnnotation annotation explicitly skips reconciling CoreDNS if set.
	SkipCoreDNSAnnotation = "controlplane.cluster.x-k8s.io/skip-coredns"

	// SkipKubeProxyAnnotation annotation explicitly skips reconciling kube-proxy if set.
	SkipKubeProxyAnnotation = "controlplane.cluster.x-k8s.io/skip-kube-proxy"

	// RemediationInProgressAnnotation is used to keep track that a KCP remediation is in progress, and more
	// specifically it tracks that the system is in between having deleted an unhealthy machine and recreating its replacement.
	// NOTE: if something external to CAPI removes this annotation the system cannot detect the above situation; this can lead to
	// failures in updating remediation retry or remediation count (both counters restart from zero).
	RemediationInProgressAnnotation = "controlplane.cluster.x-k8s.io/remediation-in-progress"
```

**Reading the code:**

- **`KubeadmControlPlaneFinalizer`**: Like `ClusterFinalizer`, ensures **ordered teardown** (etcd members leave safely, etc.).
- **Skip annotations:** Escape hatches for advanced operators who manage CoreDNS/kube-proxy out of band—**use rarely**; mis-use can desync cluster add-ons.
- **`RemediationInProgressAnnotation`:** Documents a **state machine** for unhealthy control plane nodes. External tampering with annotations is called out as dangerous—good example of how operators encode **assumptions** in metadata.

## Available condition documentation

The block defining `KubeadmControlPlaneAvailableCondition` (lines 73–88 in the same file) is unusually detailed: it explains how health is inferred from **static pods** and **etcd** when etcd is stacked. Read it when debugging “KCP says not Available but API works sometimes.”

**DevOps angle:** Bumping `spec.version` on KCP triggers a **rolling control plane upgrade**—still test in staging; etcd and API downtime windows are narrower than manual upgrades but not zero-risk.

> **Hinglish:** *Annotations jaise skip-coredns “escape hatch” hain—matlab advanced users ke liye; casually mat chhedna, warna cluster add-ons desync ho sakte hain.*

**Next:** [`config/` manifests](./07-config-manifests.md).
