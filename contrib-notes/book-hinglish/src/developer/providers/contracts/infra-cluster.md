# Contract rules for InfraCluster — Simple Hinglish

> **Note:** Ye page “Infrastructure Cluster provider contract” ka simple mental model deta hai. Exact fields/rules ke liye English source follow karo.

## Official source

- Repo: [`docs/book/src/developer/providers/contracts/infra-cluster.md`](../../../../../../../docs/book/src/developer/providers/contracts/infra-cluster.md)
- Web: [Contract rules for InfraCluster](https://cluster-api.sigs.k8s.io/developer/providers/contracts/infra-cluster.html)

## InfraCluster provider ka role

InfraCluster provider ka kaam: workload cluster ke “infrastructure-level” resources create/manage karna.

Examples (provider-specific):

- VPC/VNet, subnets, security groups
- load balancer / control plane endpoint plumbing
- failure domains info

Core side (CAPI `Cluster` controller) ko mostly yeh signals chahiye:

- infra ready hai ya nahi
- control plane endpoint publish hua ya nahi
- terminal failure vs retryable failure

## Contract rules ka simple map (v1beta2 mindset)

### 1) Common rules (all resources)

InfraCluster/InfraClusterTemplate me:

- correct `TypeMeta`/`ObjectMeta`
- correct API group + version
- predictable scope conventions follow

### 2) Control plane endpoint

InfraCluster provider ka important output:

- control plane endpoint (LB DNS/IP + port)

Core/controller plane provider is endpoint ko use karke `Cluster.spec.controlPlaneEndpoint` (or equivalent) populate/consume kar sakta hai.

### 3) Failure domains

Provider failure domains publish karta hai, taaki:

- machines placement/HA decisions better ho (zones/regions)

### 4) Initialization completed

Signal that:

- initial infra setup phase complete hai (provider-specific)

### 5) Conditions + terminal failures

Contract ensure karta hai:

- consistent conditions (Ready/error)
- terminal failures explicitly mark, taaki core infinite retries na kare

### 6) InfraClusterTemplate

ClusterClass/topology flows me templates use hote hain:

- template = blueprint for creating InfraCluster objects

### 7) Externally managed infrastructure

Kuch environments me infra already existing hota hai.

Contract clarify karta hai ki “externally managed” case me provider:

- create/delete behavior kaise handle karega
- status/conditions kaise report karega

### 8) Multi-tenancy + clusterctl support + pausing

- multi tenancy: isolation + identity conventions
- clusterctl support: provider repo components/templates expectations match
- pausing: paused objects reconcile nahi hote (consistent semantics)

## Typical InfraCluster reconciliation workflow (high-level)

### Normal

1. Core `Cluster` has `spec.infrastructureRef`
2. Infra provider creates/updates infra resources
3. Provider sets endpoint/failureDomains/conditions
4. Core continues with control plane + descendants

### Delete

1. Cluster deletion starts
2. Infra provider cleans up infra resources (unless externally managed)
3. Final conditions/status reflect completion

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
