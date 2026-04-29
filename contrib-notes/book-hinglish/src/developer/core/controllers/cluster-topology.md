# `ClusterTopology` Controller — Simple Hinglish

> **Note:** Is page ka focus managed topology (ClusterClass-driven) orchestration par hai. Commands/YAML ke liye official English source check karo.

## Official source

- Repo: [`docs/book/src/developer/core/controllers/cluster-topology.md`](../../../../../../../docs/book/src/developer/core/controllers/cluster-topology.md)
- Web: [`ClusterTopology` Controller](https://cluster-api.sigs.k8s.io/developer/core/controllers/cluster-topology.html)

## ClusterTopology controller ka kaam

`ClusterTopology` tab chalti hai jab `Cluster` ka `spec.topology` defined ho (aur managed topology feature flow active ho).

Iska responsibility:

- `ClusterClass` + referenced templates se **blueprint** banana
- blueprint + current state se **desired state** generate karna
- runtime hooks (`BeforeClusterCreate`, etc.) call karna (RuntimeSDK gate ke under)
- desired state ko reconcile karke actual objects ko create/update karna
- conditions update karke “topology reconciled” ka clear output dena

## SetupWithManager: ye controller kis par trigger hota hai?

Core code me `SetupWithManager(...)` mostly:

- `Cluster` events (sirf topology + relevant changes ke liye)
- `ClusterClass` changes (clusters enqueue)
- `MachineDeployment` changes (jab topology-owned ho)
- `MachinePool` changes (jab topology-owned ho)

## Reconcile (waterfall) — simple flow

`Reconcile(ctx, req)`:

1. `Cluster` fetch
2. guard: agar topology defined nahi hai -> return
3. patch helper + `scope.New(cluster)` banata hai
4. defer:
   - conditions reconcile (`reconcileConditions`)
   - patch: `TopologyReconciled` + `ClusterTopologyReconciled`
5. paused check: `spec.paused` / paused annotations -> skip
6. deletionTimestamp ho to `reconcileDelete(...)`
7. normal: `reconcile(ctx, s)`

### `reconcile(ctx, s)` me major steps

- `ClusterClass` load (aur ready/variables checks)
- `webhooks.DefaultAndValidateVariables(...)` (Cluster variables default/validate)
- `getBlueprint(...)`
- `getCurrentState(...)`
- (RuntimeSDK) `callBeforeClusterCreateHook(...)` (jab tak infra/control-plane objects ready nahi hue)
- `setupDynamicWatches(...)` (InfraCluster/ControlPlane CRs ke owners par)
- `mitigateManagedFieldsIssue(...)`
- `desiredStateGenerator.Generate(...)`
- `reconcileState(...)`
- runtime hooks se blocking retry: `HookResponseTracker.AggregateRetryAfter()`

## Dusre controllers se link (graph intuition)

- `ClusterClass` controller (templates + variables readiness) -> topology controller ke liye prerequisite
- Core `Cluster` controller -> topology mode me wait + orchestrate + conditions summarize
- `MachineDeployment` / `MachineSet` / `MachinePool` controllers -> topology se generated objects ko actualize karte hain
- Runtime Extensions (RuntimeSDK) -> hooks/variables/discovery support

