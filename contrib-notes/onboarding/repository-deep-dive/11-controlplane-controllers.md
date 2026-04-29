# 11 — Kubeadm control plane controllers (`controlplane/kubeadm/`)

The **KubeadmControlPlane (KCP)** reconciler ensures the **right number** of control plane Machines exist, handles **rollouts**, **certificates**, **etcd membership**, and coordinates with the **Machine** and **bootstrap** controllers.

> **Hinglish:** *KCP HA control plane ka “boss controller” hai—etcd quorum bigadna easy hai, isliye finalizer + owner Cluster check strict hai; agar owner ref abhi set nahi hua to shant raho, dubara try hoga.*

## `Reconcile` opening: KCP + Cluster ownership

```176:216:controlplane/kubeadm/internal/controllers/controller.go
func (r *KubeadmControlPlaneReconciler) Reconcile(ctx context.Context, req ctrl.Request) (res ctrl.Result, reterr error) {
	log := ctrl.LoggerFrom(ctx)

	// Fetch the KubeadmControlPlane instance.
	kcp := &controlplanev1.KubeadmControlPlane{}
	if err := r.Client.Get(ctx, req.NamespacedName, kcp); err != nil {
		if apierrors.IsNotFound(err) {
			return ctrl.Result{}, nil
		}
		return ctrl.Result{}, err
	}

	// Add finalizer first if not set to avoid the race condition between init and delete.
	if finalizerAdded, err := finalizers.EnsureFinalizer(ctx, r.Client, kcp, controlplanev1.KubeadmControlPlaneFinalizer); err != nil || finalizerAdded {
		return ctrl.Result{}, err
	}

	// Fetch the Cluster.
	cluster, err := util.GetOwnerCluster(ctx, r.Client, kcp.ObjectMeta)
	if err != nil {
		// It should be an issue to be investigated if the controller get the NotFound status.
		// So, it should return the error.
		return ctrl.Result{}, errors.Wrapf(err, "failed to retrieve owner Cluster")
	}
	if cluster == nil {
		log.Info("Cluster Controller has not yet set OwnerRef")
		return ctrl.Result{}, nil
	}

	log = log.WithValues("Cluster", klog.KObj(cluster))
	ctx = ctrl.LoggerInto(ctx, log)

	// Initialize the patch helper.
	patchHelper, err := patch.NewHelper(kcp, r.Client)
	if err != nil {
		return ctrl.Result{}, err
	}

	if isPaused, requeue, err := paused.EnsurePausedCondition(ctx, r.Client, cluster, kcp); err != nil || isPaused || requeue {
		return ctrl.Result{}, err
	}
```

**Reading the code:**

- **Finalizer on KCP:** Control plane teardown is **sensitive** (etcd quorum). The finalizer guarantees the controller can run cleanup **before** the KCP object disappears.
- **`GetOwnerCluster`:** KCP must be **owned by** the `Cluster` (ownerReference). If the Cluster controller has not linked ownership yet, KCP **waits**—again, explicit ordering instead of guessing namespaces.
- **Logging + patch helper + pause:** Same cross-cutting patterns as other core controllers—**consistency** across the codebase reduces reviewer surprise.

**What comes later in this reconciler (conceptually):**

- Reconcile **Machine** count vs `spec.replicas`.
- Plan **rolling upgrades** when `spec.version` changes.
- Inspect **static pod** / **etcd** health signals surfaced into **conditions** (see API doc comments in `kubeadm_control_plane_types.go`).

**DevOps engineer:** When debugging KCP, read **`kubectl describe kubeadmcontrolplane`** and child **Machines** together—KCP is the **controller-of-controllers** for the HA control plane.

> **Hinglish:** *Debug tip: sirf `kubectl describe machine` mat dekho—`kubeadmcontrolplane` aur uske child Machines saath mein padho, warna half story dikhegi.*

**Next:** [CAPD](./12-capd.md).
