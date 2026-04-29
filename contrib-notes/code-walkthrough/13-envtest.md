# `internal/test/envtest/` — integration test environment

> **Hinglish:** *Local apiserver+etcd for controller tests—`make test` wala fast feedback loop.*

## Purpose

Wraps **controller-runtime `envtest`**: registers CAPI schemes, installs CRDs, can spin up **Manager** + reconcilers for [`internal/controllers/.../suite_test.go`](../../internal/controllers) patterns.

## Start reading here

- [`internal/test/envtest/environment.go`](../../internal/test/envtest/environment.go) — `Run`, `RunInput`, scheme registration
- Example: [`internal/controllers/cluster/suite_test.go`](../../internal/controllers/cluster/suite_test.go)

## Execution path

`Run` → optional skip via `CAPI_DISABLE_TEST_ENV` → build scheme → `newEnvironment` → `SetupReconcilers` → `env.start` → `m.Run()` → teardown.

## Official docs

- [Testing](https://cluster-api.sigs.k8s.io/developer/core/testing.html)
- [kubebuilder envtest book](https://book.kubebuilder.io/reference/envtest.html)

## See also

- [03 — `internal/controllers`](03-internal-controllers.md)
