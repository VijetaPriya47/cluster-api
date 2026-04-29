# `cmd/clusterctl/` — CLI

> **Hinglish:** *Management cluster setup, provider versions, templates, kubeconfig—`cobra` commands yahan define.*

## Purpose

User-facing **clusterctl** binary: thin [`main.go`](../../cmd/clusterctl/main.go) calls `cmd.Execute()`; real commands in [`cmd/clusterctl/cmd/`](../../cmd/clusterctl/cmd/) (`RootCmd`, subcommands).

## Start reading here

- [`cmd/clusterctl/main.go`](../../cmd/clusterctl/main.go)
- [`cmd/clusterctl/cmd/root.go`](../../cmd/clusterctl/cmd/root.go) — `RootCmd` short description
- [`cmd/clusterctl/client/`](../../cmd/clusterctl/client/) — business logic behind commands

## Execution path

`main` → blank import auth plugins → `cmd.Execute()` → cobra dispatches to `init`, `generate cluster`, etc.

## Official docs

- [clusterctl overview](https://cluster-api.sigs.k8s.io/clusterctl/overview.html)
- [clusterctl for developers](https://cluster-api.sigs.k8s.io/clusterctl/developers.html)

## See also

- [10 — `test/framework`](10-test-framework.md) (`clusterctl` package reused in e2e)
