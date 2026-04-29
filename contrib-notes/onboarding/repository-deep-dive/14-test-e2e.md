# 14 — End-to-end tests (`test/e2e/`)

E2E tests run **real controllers** against a **real management cluster** (often **kind** locally), using **Ginkgo** for structured specs.

> **Hinglish:** *E2E = poora natak stage pe—unit test jitna fast nahi, par “asli world jaisa” pakka karta hai. Isliye `-tags=e2e` alag; warna har `go test` ghanton le leta.*

## Build tag `e2e`

The suite file begins with:

```1:4:test/e2e/e2e_suite_test.go
//go:build e2e
// +build e2e

/*
```

**Meaning:** Normal `go test ./...` **does not** compile these files—only builds with `-tags=e2e` (see `make test-e2e`). Keeps default test runs fast.

## Suite flags and global state

```45:90:test/e2e/e2e_suite_test.go
// Test suite flags.
var (
	// configPath is the path to the e2e config file.
	configPath string

	// useExistingCluster instructs the test to use the current cluster instead of creating a new one (default discovery rules apply).
	useExistingCluster bool

	// artifactFolder is the folder to store e2e test artifacts.
	artifactFolder string

	// clusterctlConfig is the file which tests will use as a clusterctl config.
	// If it is not set, a local clusterctl repository (including a clusterctl config) will be created automatically.
	clusterctlConfig string
	// ...
)

// Test suite global vars.
var (
	ctx = ctrl.SetupSignalHandler()

	// watchesCtx is used in log streaming to be able to get canceld via cancelWatches after ending the test suite.
	watchesCtx, cancelWatches = context.WithCancel(ctx)

	// e2eConfig to be used for this test, read from configPath.
	e2eConfig *clusterctl.E2EConfig

	// clusterctlConfigPath to be used for this test, created by generating a clusterctl local repository
	// with the providers specified in the configPath.
	clusterctlConfigPath string

	// bootstrapClusterProvider manages provisioning of the bootstrap cluster to be used for the e2e tests.
	// Please note that provisioning will be skipped if e2e.use-existing-cluster is provided.
	bootstrapClusterProvider bootstrap.ClusterProvider

	// bootstrapClusterProxy allows to interact with the bootstrap cluster to be used for the e2e tests.
	bootstrapClusterProxy framework.ClusterProxy
)
```

**Reading the code:**

- **`configPath` → `e2eConfig`:** YAML describes **which provider versions/images** to install—same structure `clusterctl` understands.
- **`useExistingCluster`:** Speeds local iteration by reusing your kind cluster.
- **`bootstrapClusterProvider` / `bootstrapClusterProxy`:** Abstractions to **create** or **attach** to the management cluster and run kubectl-like operations from Go.
- **`ctrl.SetupSignalHandler()`:** Ensures **Ctrl+C** tears down watches cleanly.

**DevOps engineer:** E2E configs mirror how **CI** proves releases—studying them teaches **supported upgrade paths** and **provider combinations**.

> **Hinglish:** *Flags se samajh aata hai CI kya karti hai: config path, artifacts folder, existing cluster reuse—local debug ke liye bhi same knobs.*

**Next:** [`test/framework`](./15-test-framework.md).
