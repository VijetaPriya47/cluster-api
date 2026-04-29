# MachineHealthCheck (MHC) — Simple Hinglish

> **Note:** MHC ke exact fields + YAML ke liye English source check karein.

## Official source

- Repo: [`docs/book/src/developer/core/controllers/machine-health-check.md`](../../../../../../../docs/book/src/developer/core/controllers/machine-health-check.md)
- Web: [MachineHealthCheck](https://cluster-api.sigs.k8s.io/developer/core/controllers/machine-health-check.html)

## MachineHealthCheck ka main kaam

`MachineHealthCheck` ka goal hota hai:

- `Machine`/target machines ko monitor karna
- unhealthy conditions detect karna
- phir remediation ka flow start karna (jab allowed ho)

Iska output mostly conditions + remediation triggers ke through aata hai.

## SetupWithManager: controller kya watch karta hai?

- `For(&MachineHealthCheck{})` (MHC objects)
- `Machine` changes: `machineIsChangedPredicate()` se yeh decide hota hai ki only relevant changes par reconcile ho
- `Cluster` changes: `ClusterPausedTransitions` type logic
- `ClusterCache` raw source (remote cluster side health watching)
- Rate limit interval increase (controller stress ke time pe frequent reconciles ko throttle karne ke liye)

## Reconcile (waterfall) — simple flow

1. MHC fetch
2. Cluster fetch (`mhc.spec.clusterName`)
3. `patch.NewHelper(...)`
4. `paused.EnsurePausedCondition(...)`
5. Labels set (`ClusterNameLabel`)
6. `reconcile(...)` call

## `reconcile(...)` ke key steps (high level)

- MHC ke owner refs ensure karta hai (`Cluster` owner)
- Agar `ClusterControlPlaneInitializedCondition` true hai:
  - `ClusterCache.GetClient(...)` se remote client milta hai
  - workload cluster nodes ko watch karta hai (`watchClusterNodes`)
- healthy vs unhealthy targets compute + patch:
  - `patchHealthyTargets(...)`
  - `patchUnhealthyTargets(...)`
- remediation hooks/requests related checks:
  - `getExternalRemediationRequest(...)`
  - `externalRemediationRequestExists(...)`

## Major functions (code me)

- `reconcile(...)`
- `patchHealthyTargets(...)`
- `patchUnhealthyTargets(...)`
- `watchClusterNodes(...)`
- Target mapping/watch helpers:
  - `clusterToMachineHealthCheck`
  - `machineToMachineHealthCheck`
  - `nodeToMachineHealthCheck`

