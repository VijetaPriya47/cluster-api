# 10 — Kubeadm bootstrap controllers (`bootstrap/kubeadm/`)

API types for kubeadm bootstrap live in `api/bootstrap/kubeadm/`. **Controllers** that generate bootstrap secrets / data live under `bootstrap/kubeadm/internal/controllers/`.

> **Hinglish:** *Yeh controller KubeadmConfig ko Machine/Cluster ke context se jodta hai—owner nahi mila? Thik hai, dubara reconcile hoga; Cluster nahi bana? Wait karo. Yehi eventual consistency hai.*

## `KubeadmConfigReconciler.Reconcile` (first half)

```147:206:bootstrap/kubeadm/internal/controllers/kubeadmconfig_controller.go
// Reconcile handles KubeadmConfig events.
func (r *KubeadmConfigReconciler) Reconcile(ctx context.Context, req ctrl.Request) (retRes ctrl.Result, rerr error) {
	log := ctrl.LoggerFrom(ctx)

	// Look up the kubeadm config
	config := &bootstrapv1.KubeadmConfig{}
	if err := r.Client.Get(ctx, req.NamespacedName, config); err != nil {
		if apierrors.IsNotFound(err) {
			return ctrl.Result{}, nil
		}
		return ctrl.Result{}, err
	}

	// Look up the owner of this kubeadm config if there is one
	configOwner, err := bsutil.GetTypedConfigOwner(ctx, r.Client, config)
	if err != nil {
		if apierrors.IsNotFound(err) {
			// Could not find the owner yet, this is not an error and will rereconcile when the owner gets set.
			return ctrl.Result{}, nil
		}
		return ctrl.Result{}, errors.Wrapf(err, "failed to get owner")
	}
	if configOwner == nil {
		return ctrl.Result{}, nil
	}
	log = log.WithValues(configOwner.GetKind(), klog.KRef(configOwner.GetNamespace(), configOwner.GetName()), "resourceVersion", configOwner.GetResourceVersion())
	ctx = ctrl.LoggerInto(ctx, log)

	if configOwner.GetKind() == "Machine" {
		// AddOwners adds the owners of Machine as k/v pairs to the logger.
		// Specifically, it will add KubeadmControlPlane, MachineSet and MachineDeployment.
		ctx, log, err = clog.AddOwners(ctx, r.Client, configOwner)
		if err != nil {
			return ctrl.Result{}, err
		}
	}

	log = log.WithValues("Cluster", klog.KRef(configOwner.GetNamespace(), configOwner.ClusterName()))
	ctx = ctrl.LoggerInto(ctx, log)

	// Lookup the cluster the config owner is associated with
	cluster, err := util.GetClusterByName(ctx, r.Client, configOwner.GetNamespace(), configOwner.ClusterName())
	if err != nil {
		if apierrors.IsNotFound(err) {
			log.Info("Cluster does not exist yet, waiting until it is created")
			return ctrl.Result{}, nil
		}
		log.Error(err, "Could not get cluster with metadata")
		return ctrl.Result{}, err
	}

	// Initialize the patch helper.
	patchHelper, err := patch.NewHelper(config, r.Client)
	if err != nil {
		return ctrl.Result{}, err
	}

	if isPaused, requeue, err := paused.EnsurePausedCondition(ctx, r.Client, cluster, config); err != nil || isPaused || requeue {
		return ctrl.Result{}, err
	}
```

**Line-by-line meaning:**

1. **Load `KubeadmConfig`:** Same pattern as Cluster controller—missing object → done.
2. **`GetTypedConfigOwner`:** Bootstrap configs are usually owned by a **Machine** (or pool abstraction). If owner not yet set, exit quietly—**eventual consistency**; next watch will retry.
3. **Rich logging:** Adds owner name/namespace and, for Machines, walks owner chain to include **MachineDeployment / KCP** context—critical for debugging fleet issues from a single log line.
4. **Fetch `Cluster`:** Bootstrap behavior depends on **cluster-wide** settings (pause, topology, version). If `Cluster` does not exist yet, log and wait—ordering is explicit, not guessed.
5. **`patchHelper` + `paused`:** Same cross-cutting concerns as core controllers.

**Later in the same function** (defer + bootstrap data generation—not quoted): the controller writes **Secrets** with cloud-init/Ignition payloads and sets **conditions** like “bootstrap data ready”—the **Machine** controller and infrastructure provider consume that output.

**Real-world analogy:** This is the HR onboarding desk: it can’t print a badge until it knows **which employee** (owner Machine) and **which site policy** (Cluster) apply.

> **Hinglish:** *Logging mein owners chain isliye: production mein error milte hi pata chalna chahiye “kaunsa MachineDeployment/KCP is bootstrap se juda hai”—warna debug mushkil.*

**Next:** [Control plane controllers](./11-controlplane-controllers.md).
