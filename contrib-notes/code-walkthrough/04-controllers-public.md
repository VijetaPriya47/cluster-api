# `controllers/` — public reconciler facades

> **Hinglish:** *Bahar wale projects `internal` import nahi kar sakte—yeh package thin wrapper hai jo andar wale `Reconciler` ko `SetupWithManager` se lagata hai.*

## Purpose

Exported types like `ClusterReconciler` embed `client.Client`, `ClusterCache`, etc., and **delegate** to `internal/controllers/...` implementations.

## Start reading here

- [`controllers/alias.go`](../../controllers/alias.go) — `ClusterReconciler.SetupWithManager` forwards to `clustercontroller.Reconciler`

## Code pattern

```63:71:controllers/alias.go
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

## Wiring

[`main.go`](../../main.go) constructs `controllers.ClusterReconciler{...}` with `mgr.GetClient()` and calls `SetupWithManager`.

## See also

- [01 — `main.go`](01-main-and-manager.md)
- [03 — `internal/controllers`](03-internal-controllers.md)
