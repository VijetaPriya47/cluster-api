# Machine Controller — Simple Hinglish

> **Note:** Commands/YAML aur exact errors ke liye official English page check karein.

## Official source

- Repo: [`docs/book/src/developer/core/controllers/machine.md`](../../../../../../../docs/book/src/developer/core/controllers/machine.md)
- Web: [Machine Controller](https://cluster-api.sigs.k8s.io/developer/core/controllers/machine.html)

## Is controller ka kaam kya hai?

`Machine` controller ka kaam hai har `Machine` ke liye “provisioning lifecycle” handle karna:

- owner/labels ensure karna (Cluster + parents tak ownership traceable ho)
- `BootstrapConfig` aur `InfraMachine` ko reconcile karna (provider se contract objects)
- Node lifecycle (drain, volume detach, deletion) ko safe tarike se execute karna
- certificate expiry/renewal related reconcile
- feature gate (`InPlaceUpdates`) on ho to in-place update trigger karna

## SetupWithManager: ye controller kis par trigger hota hai?

Core code me:

- `For(&Machine{})`
- Watches:
  - `Cluster` (mapping helpers ke through machines enqueue)
  - `ClusterCache` raw source (probe failure on machines)
  - `MachineSet` + `MachineDeployment` changes -> affected machines enqueued

## Reconcile (waterfall) — major steps

`Reconcile(ctx, req)` ka simple flow:

1. `Machine` fetch
2. `Machine` finalizer ensure (`MachineFinalizer`)
3. Logging me owners add (Cluster/MachineSet/MachineDeployment)
4. `Cluster` fetch + `paused.EnsurePausedCondition(...)`
5. Scope build:
   - owning MachineSet (`getOwnerMachineSet`)
   - owning MachineDeployment (`getOwnerMachineDeployment`)
6. Defer block:
   - `updateStatus(...)`
   - patch machine conditions + observedGeneration
7. Deletion vs normal:
   - deletion: always phases + `reconcileDelete(...)`
   - normal: always phases + `reconcileInPlaceUpdate(...)`

## Major phases/functions (code me dikhne wale key names)

Reconcile me ye phases directly call hote hain:

- `reconcileMachineOwnerAndLabels`
- `reconcileBootstrap`
- `reconcileInfrastructure`
- `reconcileNode`
- `reconcileCertificateExpiry`
- normal-only:
  - `reconcileInPlaceUpdate`
- deletion-only:
  - `reconcileDelete`

Deletion me relevant helper functions (high-level idea):

- `isDeleteNodeAllowed`
- `drainNode`
- `shouldWaitForNodeVolumes`
- `deleteNode`
- `reconcileDeleteBootstrap`
- `reconcileDeleteInfrastructure`
- `watchClusterNodes` (+ `nodeToMachine`)

## Dusre controllers se kaise linked?

- `MachineSet controller` replica/template logic manage karta hai
- `MachineDeployment controller` rollout logic manage karta hai
- `Machine controller` “actual machine instance” ko bootstrap/infra/node level pe materialize karta hai

