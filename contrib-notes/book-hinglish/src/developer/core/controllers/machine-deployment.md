# MachineDeployment Controller — Simple Hinglish

> **Note:** Exact behavior/yaml commands ke liye official English page dekhna.

## Official source

- Repo: [`docs/book/src/developer/core/controllers/machine-deployment.md`](../../../../../../../docs/book/src/developer/core/controllers/machine-deployment.md)
- Web: [MachineDeployment](https://cluster-api.sigs.k8s.io/developer/core/controllers/machine-deployment.html)

## MachineDeployment ka kaam

`MachineDeployment` ek “rollout unit” hai. Ye decide karta hai:

- kaun se `MachineSet`/`replicas` rakhne hain
- rollout strategy (`RollingUpdate` ya `OnDelete`) kya hogi
- scale up/down + revision management

Iske baad `MachineSets` (aur unke through `Machines`) actual provisioning ke liye chain me aate hain.

## SetupWithManager: controller kis par trigger hota hai?

Core code me:

- `For(&MachineDeployment{})`
- `Owns(&MachineSet{})` (MachineDeployment apne MachineSets manage karta hai)
- `MachineSet` changes ko map karke `MachineDeployment` enqueue
- `Cluster` changes (pause/topology relevant logic) par enqueue

## Reconcile (waterfall) — kya hota hai?

`Reconcile(ctx, req)` high-level:

1. `MachineDeployment` fetch
2. `MachineDeploymentFinalizer` ensure
3. `Cluster` fetch
4. patch helper + `paused.EnsurePausedCondition`
5. scope build
6. deletion ho rahi ho to `reconcileDelete(...)`
7. warna `reconcile(...)`

### reconcile(ctx, s) me main steps

- labels/selector/spec defaults saaf karta hai
- Cluster ke saath ownerRef ensure karta hai
- templates/infra-bootstrap objects handle karta hai:
  - `getTemplatesAndSetOwner(...)`
  - `getAndAdoptMachineSetsForDeployment(...)`
- `MachineSets` par revision/labels consistent karta hai
- rollout strategy ke hisaab se:
  - `sync(...)` (jab paused)
  - `rolloutRollingUpdate(...)`
  - `rolloutOnDelete(...)`

## Major functions/phases (code me main names)

- `reconcile(ctx, s)`
- `createOrUpdateMachineSetsAndSyncMachineDeploymentRevision(...)`
- `getAndAdoptMachineSetsForDeployment(...)`
- `getTemplatesAndSetOwner(...)`
- `reconcileDelete(...)`
- `adoptOrphan(...)`
- `MachineSetToDeployments(...)` (watch mapping)

## Dusre controllers se link

- `MachineDeployment` -> `MachineSet` chain: deployment desired rollout plan banata hai, machineset templates + machines ka kaam karta hai.
- `Machine` controller -> machineset/machines ke through actual node/drain/provisioning complete karta hai.

