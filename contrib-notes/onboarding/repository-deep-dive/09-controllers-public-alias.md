# 09 — Public `controllers` package (embedding)

The [`controllers`](https://github.com/kubernetes-sigs/cluster-api/tree/main/controllers) package at repo root is **not** the same as `internal/controllers`. It exposes **typed reconcilers** that forward to internal implementations—so downstream binaries can do:

```go
import "sigs.k8s.io/cluster-api/controllers"
```

without importing `internal/...` paths (which Go forbids across module boundaries for external consumers).

> **Hinglish:** *Samjho dukaan (`controllers`) aur godown (`internal`)—bahar wale sirf dukaan se import karte hain; andar ka samaan rearrange ho sakta hai bina duniya tod ke.*

## Alias pattern: `ClusterReconciler`

```48:71:controllers/alias.go
// Following types provides access to reconcilers implemented in internal/controllers, thus
// allowing users to provide a single binary "batteries included" with Cluster API and providers of choice.

// ClusterReconciler reconciles a Cluster object.
type ClusterReconciler struct {
	Client       client.Client
	APIReader    client.Reader
	ClusterCache clustercache.ClusterCache

	// WatchFilterValue is the label value used to filter events prior to reconciliation.
	WatchFilterValue string

	RemoteConnectionGracePeriod time.Duration
}

func (r *ClusterReconciler) SetupWithManager(ctx context.Context, mgr ctrl.Manager, options controller.Options) error {
	return (&clustercontroller.Reconciler{
		Client:                      r.Client,
		APIReader:                   r.APIReader,
		ClusterCache:                r.ClusterCache,
		WatchFilterValue:            r.WatchFilterValue,
		RemoteConnectionGracePeriod: r.RemoteConnectionGracePeriod,
	}).SetupWithManager(ctx, mgr, options)
}
```

**Reading the code:**

- **Exported struct** `ClusterReconciler` holds the **dependencies** users must inject (clients, caches, tuning knobs).
- **`SetupWithManager`** constructs the **internal** `clustercontroller.Reconciler` with the same fields and registers watches with the shared `Manager`.

This is the **Adapter / Facade** pattern: stable exported type, internal type can gain fields without breaking callers until maintainers choose to expose them.

## Where `main.go` uses it

The core manager binary wires real clients from `mgr` into the public reconciler:

```596:605:main.go
	if err := (&controllers.ClusterReconciler{
		Client:                      mgr.GetClient(),
		APIReader:                   mgr.GetAPIReader(),
		ClusterCache:                clusterCache,
		WatchFilterValue:            watchFilterValue,
		RemoteConnectionGracePeriod: remoteConnectionGracePeriod,
	}).SetupWithManager(ctx, mgr, concurrency(clusterConcurrency)); err != nil {
		setupLog.Error(err, "Unable to create controller", "controller", "Cluster")
		os.Exit(1)
	}
```

**Meaning:** `main.go` is “composition root”—it creates one `Manager`, shared caches, feature gates, then **registers** each controller with concurrency options.

**DevOps note:** Most teams don’t compile custom `main.go`; they install upstream manifests. This matters when you **vendor** CAPI into a larger platform binary.

> **Hinglish:** *`main.go` yahan wires karta hai: real client/cache de do, concurrency set karo, phir `SetupWithManager` se controller register—yahi composition root hai.*

**Next:** [Bootstrap controllers](./10-bootstrap-controllers.md).
