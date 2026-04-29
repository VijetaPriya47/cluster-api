# 16 — envtest harness (`internal/test/envtest/`)

**envtest** starts a real **`kube-apiserver` + `etcd`** pair on localhost for tests—no kubelet, no cloud. CAPI wraps controller-runtime’s envtest with opinionated defaults: schemes, CRDs, webhooks, and manager setup.

> **Hinglish:** *envtest = “mini API server ghar pe”—cloud bill zero, phir bhi admission/CRD logic test ho sakta hai. `CAPI_DISABLE_TEST_ENV` se fast pure-unit runs bhi possible.*

## `Run`: one entrypoint for controller integration tests

```131:215:internal/test/envtest/environment.go
// RunInput is the input for Run.
type RunInput struct {
	M                           *testing.M
	ManagerCacheOptions         cache.Options
	ManagerClientOptions        client.Options
	SetupIndexes                func(ctx context.Context, mgr ctrl.Manager)
	SetupReconcilers            func(ctx context.Context, mgr ctrl.Manager)
	SetupEnv                    func(e *Environment)
	MinK8sVersion               string
	AdditionalSchemeBuilder     runtime.SchemeBuilder
	AdditionalCRDDirectoryPaths []string
}

// Run executes the tests of the given testing.M in a test environment.
func Run(ctx context.Context, input RunInput) int {
	if os.Getenv("CAPI_DISABLE_TEST_ENV") != "" {
		klog.Info("Skipping test env start as CAPI_DISABLE_TEST_ENV is set")
		return input.M.Run()
	}

	// Calculate the scheme.
	scheme := runtime.NewScheme()
	registerSchemes(scheme)
	// Register additional schemes from k8s APIs.
	utilruntime.Must(appsv1.AddToScheme(scheme))
	utilruntime.Must(corev1.AddToScheme(scheme))
	utilruntime.Must(rbacv1.AddToScheme(scheme))
	utilruntime.Must(storagev1.AddToScheme(scheme))
	// Register additionally passed schemes.
	if input.AdditionalSchemeBuilder != nil {
		utilruntime.Must(input.AdditionalSchemeBuilder.AddToScheme(scheme))
	}

	// Bootstrapping test environment
	env := newEnvironment(ctx, scheme, input.AdditionalCRDDirectoryPaths, input.ManagerCacheOptions, input.ManagerClientOptions)
	// ...
	if input.SetupIndexes != nil {
		input.SetupIndexes(ctx, env.Manager)
	}
	if input.SetupReconcilers != nil {
		input.SetupReconcilers(ctx, env.Manager)
	}

	// Start the environment.
	env.start(ctx)
	// ...
	// Expose the environment.
	input.SetupEnv(env)

	// Run tests
	code := input.M.Run()
```

**Reading the code:**

- **`RunInput.SetupReconcilers`:** Each controller suite registers the reconciler under test against a real `Manager`—closest thing to production without a cloud.
- **Scheme registration:** Teaches why tests import dozens of `AddToScheme` lines—**the client must know** how to decode every Kind you `Get`/`List`.
- **`CAPI_DISABLE_TEST_ENV`:** Escape hatch for **pure unit tests** using fake clients only.
- **`input.M.Run()`:** Standard Go test entry; `Run` wraps it with lifecycle.

**Why study this package:** It shows how mature projects **standardize** test environments so every suite doesn’t copy-paste boilerplate.

> **Hinglish:** *Scheme register karna zaroori hai warna client ko object decode hi nahi aata—yahi error newcomers ko aksar uljha deta hai.*

**Next:** [Proposals](./17-proposals.md).
