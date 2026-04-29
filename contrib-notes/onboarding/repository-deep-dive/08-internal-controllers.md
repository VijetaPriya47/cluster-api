# 08 — Core controller implementation (`internal/controllers/`)

This tree is the **implementation** of core reconciliation: **Cluster**, **Machine**, **MachineDeployment**, topology, ClusterResourceSet, etc. It is **internal** so the project can refactor freely; external Go code should use the thin wrappers in [`controllers/`](./09-controllers-public-alias.md).

> **Hinglish:** *Yahan “asli kaam” hota hai—har change par `Reconcile` chalta hai, finalizer lagta hai, pause check hota hai, status update hota hai. `internal` isliye ki public Go API stable rahe, andar refactoring chalti rahe.*

## `Reconcile` entry: Cluster controller

When a `Cluster` object changes (or related objects enqueue it), controller-runtime calls `Reconcile` with a `NamespacedName`.

```136:181:internal/controllers/cluster/cluster_controller.go
func (r *Reconciler) Reconcile(ctx context.Context, req ctrl.Request) (retRes ctrl.Result, reterr error) {
	log := ctrl.LoggerFrom(ctx)

	// Fetch the Cluster instance.
	cluster := &clusterv1.Cluster{}
	if err := r.Client.Get(ctx, req.NamespacedName, cluster); err != nil {
		if apierrors.IsNotFound(err) {
			// Object not found, return.  Created objects are automatically garbage collected.
			// For additional cleanup logic use finalizers.
			return ctrl.Result{}, nil
		}

		// Error reading the object - requeue the request.
		return ctrl.Result{}, err
	}

	// Add finalizer first if not set to avoid the race condition between init and delete.
	if finalizerAdded, err := finalizers.EnsureFinalizer(ctx, r.Client, cluster, clusterv1.ClusterFinalizer); err != nil || finalizerAdded {
		return ctrl.Result{}, err
	}

	// Initialize the patch helper.
	patchHelper, err := patch.NewHelper(cluster, r.Client)
	if err != nil {
		return ctrl.Result{}, err
	}

	if isPaused, requeue, err := paused.EnsurePausedCondition(ctx, r.Client, cluster, cluster); err != nil || isPaused || requeue {
		return ctrl.Result{}, err
	}

	s := &scope{
		cluster: cluster,
	}
	if cluster.Spec.Topology.IsDefined() {
		s.clusterClass = &clusterv1.ClusterClass{}
		if err := r.Client.Get(ctx, cluster.GetClassKey(), s.clusterClass); err != nil {
			return ctrl.Result{}, errors.Wrapf(err, "failed to get ClusterClass %s", cluster.GetClassKey())
		}
	}

	defer func() {
		// Always reconcile the Status.
		if err := r.updateStatus(ctx, s); err != nil {
			reterr = kerrors.NewAggregate([]error{reterr, err})
			return
```

**Line-by-line meaning:**

1. **Fetch Cluster:** If the object was deleted and removed from cache, `IsNotFound` → success with no requeue (GC handled elsewhere; finalizers handle extra cleanup).
2. **Transient API errors:** Return `err` so the work queue **retries** with backoff.
3. **Ensure finalizer:** If missing, add `cluster.cluster.x-k8s.io` and **return** early so the next reconcile sees a stable object for deletion ordering.
4. **`patch.NewHelper`:** Utility to compute minimal **patch** bytes at end of reconcile—reduces conflict with other writers.
5. **`paused.EnsurePausedCondition`:** If cluster is “paused”, skip mutating work but keep status honest—**GitOps freeze** or break-glass during incidents.
6. **Topology scope:** If the Cluster uses **ClusterClass** / managed topology, load the `ClusterClass` object for template expansion.
7. **`defer updateStatus`:** Even if reconciliation errors midway, **status** (conditions) is refreshed—users see progress instead of silent stalls.

**Real-world analogy:** This is the **project manager checking the Gantt chart**: read the latest approved plan (`Get`), make sure you’re allowed to touch work (finalizers, pause), pull referenced templates (`ClusterClass`), then update stakeholders (`status`) no matter what failed in the middle.

> **Hinglish:** *Flow aasaan bhasha mein: object uthao → delete ho chuka ho to return → finalizer ensure karo → pause ho to aage mat badho → ClusterClass lao agar topology hai → defer mein status hamesha refresh. “defer” ka matlab: error aaya to bhi user ko conditions dikhni chahiye.*

**Next:** [Public `controllers` package](./09-controllers-public-alias.md).
