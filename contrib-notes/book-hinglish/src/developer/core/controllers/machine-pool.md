# MachinePool Controller — Simple Hinglish

> **Note:** Exact contracts/YAML details ke liye English source check karein.

## Official source

- Repo: [`docs/book/src/developer/core/controllers/machine-pool.md`](../../../../../../../docs/book/src/developer/core/controllers/machine-pool.md)
- Web: [MachinePool Controller](https://cluster-api.sigs.k8s.io/developer/core/controllers/machine-pool.html)

## MachinePool controller ka kaam

`MachinePool` controller ka focus hota hai:

- `MachinePool` ke desired state ke hisaab se **pool machines** manage karna
- `nodeRefs` (Nodes<->Pool) ka reconciliation
- bootstrap + infra resources ko reconcile karna
- deletion me external references + Nodes ko clean karna (timeout/gates ke saath)

Simple words: MachineSet jaisa behavior, but “pool oriented” lifecycle.

## SetupWithManager: ye controller kis cheez ko watch karta hai?

Core code me:

- `For(&MachinePool{})`
- `Cluster` -> `MachinePool` mapping (Cluster changes par enqueue)
- `ClusterCache` se raw source (probe failure on workload cluster side)

## Reconcile (waterfall) — normal vs deletion

### Normal flow

1. `MachinePool` fetch
2. `MachinePoolFinalizer` ensure
3. `Cluster` fetch (`spec.clusterName` se)
4. `patch.NewHelper(...)`
5. `paused.EnsurePausedCondition(...)`
6. Defer: `updateStatus(...)` + readyConditions summary + patch
7. Phases:
   - `reconcileBootstrap`
   - `reconcileInfrastructure`
   - `getMachinesForMachinePool`
   - `reconcileNodeRefs`
   - `setMachinesUptoDate`

### Deletion flow

1. `reconcileDelete(...)`
2. external references delete karna (`reconcileDeleteExternal`)
3. node delete timeout check:
   - timeout pass ho to skip nodes deletion
   - warna `reconcileDeleteNodes(...)`
4. finalizer remove

## Major functions/phases (code me)

- `reconcileSetOwnerAndLabels`
- `reconcileBootstrap`
- `reconcileInfrastructure`
- `getMachinesForMachinePool`
- `reconcileNodeRefs`
- `setMachinesUptoDate`

Deletion ke liye:

- `reconcileDelete`
- `reconcileDeleteExternal`
- `reconcileDeleteNodes`
- `isMachinePoolNodeDeleteTimeoutPassed`
- `watchClusterNodes` (+ `nodeToMachinePool`)  (Nodes changes par pool enqueue)

