# MachineSet Controller — Simple Hinglish

> **Note:** Exact details + YAML ke liye English source check karo.

## Official source

- Repo: [`docs/book/src/developer/core/controllers/machine-set.md`](../../../../../../../docs/book/src/developer/core/controllers/machine-set.md)
- Web: [MachineSet](https://cluster-api.sigs.k8s.io/developer/core/controllers/machine-set.html)

## MachineSet controller ka purpose

`MachineSet` controller mainly yeh karta hai:

- `replicas` / desired state ke basis par `Machines` create + delete karna
- `MachineSet` templates se `BootstrapConfig` aur `InfraMachine` references ko sync karna
- unhealthy machines ko detect karke remediation flow ko trigger karna
- scaling/move ke operations ke liye in-place update trigger karna

## SetupWithManager: controller kya watch karta hai?

- `MachineSet` events (`For(&MachineSet{})`)
- `Machine` -> `MachineSets` mapping (enqueue if owner ref absent)
- `MachineDeployment` -> `MachineSets` mapping
- `Cluster` events (pause/filters relevant hone par)
- `ClusterCache` raw source (probe failure / remote health related)

## Reconcile (waterfall) — step-by-step

1. `MachineSet` fetch + `MachineSetFinalizer` ensure
2. `Cluster` fetch (`spec.clusterName`)
3. `patch.NewHelper(...)` + `paused.EnsurePausedCondition(...)`
4. Scope build:
   - machineSet
   - machines list (sync/unhealthy/move ke liye)
   - owning `MachineDeployment` (agar apply hota hai)
5. Defer me:
   - `updateStatus(...)`
   - `reconcileV1Beta1Status(...)`
   - `patchMachineSet(...)` + observedGeneration
6. Deletion vs normal:
   - Deletion: `reconcileDelete(...)`
   - Normal: in phases order:
     - `reconcileMachineSetOwnerAndLabels`
     - `reconcileInfrastructure`
     - `reconcileBootstrapConfig`
     - `getAndAdoptMachinesForMachineSet`
     - `reconcileUnhealthyMachines`
     - `syncMachines`
     - `triggerInPlaceUpdate`
     - `syncReplicas`

## Key functions/phases (main names)

- `reconcileMachineSetOwnerAndLabels`
- `reconcileInfrastructure`
- `reconcileBootstrapConfig`
- `getAndAdoptMachinesForMachineSet`
- `reconcileUnhealthyMachines`
- `syncMachines`
- `triggerInPlaceUpdate`
- `syncReplicas`

Deeper mechanics:

- `createMachines`, `deleteMachines`
- `startMoveMachines`, `completeMoveMachine`
- `computeDesiredMachine`, `adoptOrphan`
- `computeDesiredBootstrapConfig`, `computeDesiredInfraMachine`

## Dusre controllers se link

- `MachineDeployment` rollout decide karta hai (kaunsi MachineSets + replicas)
- `MachineSet` templates + adoption se `Machines` materialize karta hai
- `Machine` controller actual provisioning node level pe complete karta hai

