# Cluster Controller — Simple Hinglish

> **Note:** Commands/YAML aur exact errors ke liye official English page check karein.

## Official source

- Repo: [`docs/book/src/developer/core/controllers/cluster.md`](../../../../../../../docs/book/src/developer/core/controllers/cluster.md)
- Web: [Cluster Controller](https://cluster-api.sigs.k8s.io/developer/core/controllers/cluster.html)

## Is controller ka kaam kya hai?

`Cluster` controller “main orchestrator” hai. It takes care of:

- `Cluster` ke referenced **Infrastructure** + **ControlPlane** objects ko reconcile karna
- `Cluster` ke saare **descendants** collect karna (Machines/MachineSets/MachineDeployments/MachinePools, etc.)
- `kubeconfig`/credentials wiring ko reconcile karna
- `Cluster.status.conditions` ko summarize karke patch karna (taaki users ko ek clear status mile)
- deletion me dependent cheezen clean karna (finalizer ke through)

## SetupWithManager: ye controller kis par trigger hota hai?

Core code me `SetupWithManager(...)` Cluster events par:

- `For(&clusterv1.Cluster{})`
- `ClusterCache` (probe failure wali situations me) se enqueues
- `Machine`, `MachineDeployment` aur (feature gate ke under) `MachinePool` changes se: Cluster ko enqueue kiya jata hai

## Reconcile (waterfall) — new contributor ke liye simple flow

`Reconcile(ctx, req)` ka high-level waterfall:

1. `Cluster` object fetch (`r.Client.Get`)
2. `Cluster` finalizer ensure (`finalizers.EnsureFinalizer`)
3. `patch.NewHelper(...)` banata hai (end me status/patch ke liye)
4. `paused.EnsurePausedCondition(...)` se check hota hai
5. Agar `spec.topology` defined hai:
   - `ClusterClass` load karta hai (topology-related reconcile ke liye)
6. Defer block me hamesha:
   - `updateStatus(...)`
   - `patchCluster(...)` (owned conditions + observedGeneration)
7. Normal vs deletion:
   - deletion ho rahi hai (`DeletionTimestamp` set): `reconcileDelete(...)`
   - warna normal loop:
     - topology wait (agar `controlPlaneRef`/`infrastructureRef` missing)
     - phases run:
       - `reconcileInfrastructure`
       - `reconcileControlPlane`
       - `getDescendants`
       - `reconcileKubeconfig`
       - `reconcileV1Beta1ControlPlaneInitialized`

## “Kaunse major functions/phases chalte hain?”

- `SetupWithManager`
- `Reconcile`
- `reconcileInfrastructure`
- `reconcileControlPlane`
- `getDescendants`
- `reconcileKubeconfig`
- `reconcileV1Beta1ControlPlaneInitialized`
- `reconcileDelete`
- mapping helpers:
  - `controlPlaneMachineToCluster`
  - `machineDeploymentToCluster`
  - `machinePoolToCluster`

## Dusre controllers se link (simple mental model)

Think like:

- `Machine/MachineSet/MachineDeployment/MachinePool` “apna apna kaam” karte hain
- `Cluster` controller un sab ki progress ko “summarize” karta hai:
  - `getDescendants` -> descendants ka state padhta hai
  - `updateStatus/patchCluster` -> Cluster conditions me reflect karta hai

