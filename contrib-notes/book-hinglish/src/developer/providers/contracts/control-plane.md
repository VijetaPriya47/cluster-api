# Contract rules for ControlPlane — Simple Hinglish

> **Note:** Ye page “ControlPlane provider contract” ka simple mental model deta hai. Exact fields/rules ke liye English source follow karo.

## Official source

- Repo: [`docs/book/src/developer/providers/contracts/control-plane.md`](../../../../../../../docs/book/src/developer/providers/contracts/control-plane.md)
- Web: [Contract rules for ControlPlane](https://cluster-api.sigs.k8s.io/developer/providers/contracts/control-plane.html)

## ControlPlane provider ka role

ControlPlane provider ka kaam: workload cluster ke **control plane** ko lifecycle-manage karna.

Core side (CAPI) ko yeh chahiye hota hai ki ControlPlane provider:

- desired replicas/version ko implement kare
- API endpoint publish kare (taaki Cluster `spec.controlPlaneEndpoint` type info set/usable ho)
- apne Machines ko link kare (control-plane Machines list/ownership)
- conditions/status ko consistently update kare (Ready/available/failure signals)

## Contract rules ka “simple map” (v1beta2 mindset)

### 1) Common rules (all resources)

Har provider resource (ControlPlane/ControlPlaneTemplate) me:

- correct `TypeMeta`/`ObjectMeta`
- correct API group + version
- scope conventions follow (namespaced resources typically)

### 2) ControlPlane object: key integration points

Core controllers ko jo major things chahiye hoti hain:

- **endpoint**: control plane API server endpoint publish hona
- **replicas**: desired count & actual status aligned
- **version**: desired Kubernetes version reflect hona
- **machines**: control plane machines ka reference/list provide hona
- **rolloutAfter**: rollout orchestration ke liye time-based trigger (provider support)
- **initialization completed**: first-time init complete signal
- **in-place updates**: kuch updates “replace machine” ke bina possible (provider specific)
- **conditions**: Ready + other conditions consistently set
- **terminal failures**: non-retriable failure signal (so core keeps retrying forever na kare)

### 3) ControlPlaneTemplate

ClusterClass/topology workflows me ControlPlaneTemplate use hota hai:

- template = “blueprint” from which actual ControlPlane objects are created
- contract ensures template fields are consistent & patchable

### 4) Cluster kubeconfig & certificate management

Control plane endpoint ready hone ke baad:

- cluster kubeconfig generation/use-case possible hota hai
- certificates/rotation/management hooks provider contract ke scope me clarify hote hain

### 5) Placement + metadata propagation

Provider ko:

- control-plane Machines placement (node/zone/infra placement) support karna padta hai (as applicable)
- labels/annotations propagate karne ke rules follow karne hote hain

### 6) MinReadySeconds + UpToDate propagation

Rollout stability ke liye:

- “machine ready for N seconds” type stabilization
- “up-to-date” signals propagate/reflect hon

### 7) Multiple instances + clusterctl support

Contract yeh ensure karta hai ki:

- same cluster me multiple provider instances run kar sakein (namespaces/labels/identification)
- clusterctl repository expectations (components/templates) match karein

### 8) Pausing

Paused resources reconcile nahi hote. Contract me pause semantics clear hote hain so core & provider controllers consistent behavior dikhayen.

## Typical reconciliation workflow (high-level)

Ek normal flow generally:

1. Core `Cluster` controller sees `spec.controlPlaneRef`
2. ControlPlane provider creates/updates control-plane Machines
3. Provider publishes endpoint + updates conditions/status
4. Core uses those signals for kubeconfig, descendants, rollout, health checks, etc.

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
