# `main.go` — core Cluster API manager

> **Hinglish:** *Yeh binary “cluster-api-controller-manager” ka entry point hai—scheme register, flags, phir sab controllers webhook server par chalte hain.*

## Purpose

Bootstraps the **core provider** process: Kubernetes scheme registration, feature gates, `controller-runtime` **Manager**, webhooks, and registration of every core reconciler (via [`controllers/`](./04-controllers-public.md)).

## Start reading here

- [`main.go`](../../main.go) (repo root)
- [`internal/setup/`](../../internal/setup/) — wiring helpers referenced from `main`

## Execution path (high level)

1. **`init()`** registers API types on the global `scheme` and runtime hook catalog:

```132:152:main.go
func init() {
	_ = clientgoscheme.AddToScheme(scheme)
	_ = apiextensionsv1.AddToScheme(scheme)
	_ = storagev1.AddToScheme(scheme)

	_ = clusterv1beta1.AddToScheme(scheme)
	_ = clusterv1.AddToScheme(scheme)

	_ = addonsv1beta1.AddToScheme(scheme)
	_ = addonsv1.AddToScheme(scheme)

	_ = runtimev1alpha1.AddToScheme(scheme)
	_ = runtimev1.AddToScheme(scheme)

	_ = ipamv1alpha1.AddToScheme(scheme)
	_ = ipamv1beta1.AddToScheme(scheme)
	_ = ipamv1.AddToScheme(scheme)

	// Register the RuntimeHook types into the catalog.
	_ = runtimehooksv1.AddToCatalog(catalog)
}
```

2. **`main()`** (later in file) parses flags (`InitFlags`), builds **Manager** with cache/client options, registers webhooks, then **`SetupWithManager`** on each `controllers.*Reconciler` with **concurrency** settings (e.g. `clusterConcurrency`).

3. **`mgr.Start(ctx)`** runs the process until shutdown.

## Key flags (examples)

Leader election, namespace / watch-filter, per-controller **concurrency** (how many objects reconcile in parallel):

```158:197:main.go
	fs.BoolVar(&enableLeaderElection, "leader-elect", false,
		"Enable leader election for controller manager. Enabling this will ensure there is only one active controller manager.")
	// ...
	fs.IntVar(&clusterConcurrency, "cluster-concurrency", 50,
		"Number of clusters to process simultaneously")
```

## Official docs

- [Developing core Cluster API](https://cluster-api.sigs.k8s.io/developer/core/overview.html)

## See also

- [04 — Public `controllers`](./04-controllers-public.md)
