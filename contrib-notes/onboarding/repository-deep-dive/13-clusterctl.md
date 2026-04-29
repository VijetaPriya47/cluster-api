# 13 — `clusterctl` CLI (`cmd/clusterctl/`)

`clusterctl` is the **user-facing command line** for **management cluster** operations: init providers, upgrade components, generate manifests, fetch kubeconfigs, describe clusters.

> **Hinglish:** *clusterctl = day-0 helper—“kaunsa provider version lagana hai, kubeconfig kaise nikaalna hai”—taaki tum khud 50 YAML jod ke na baithe raho.*

## `main.go`: thin entrypoint

```17:28:cmd/clusterctl/main.go
// main is the main package for clusterctl.
package main

import (
	_ "k8s.io/client-go/plugin/pkg/client/auth"

	"sigs.k8s.io/cluster-api/cmd/clusterctl/cmd"
)

func main() {
	cmd.Execute()
}
```

**Meaning:**

- **Blank import** `client-go/plugin/pkg/client/auth` registers cloud **credential plugins** (GCP, Azure, OIDC, …) so `clusterctl` can reuse your kubeconfig auth providers.
- **`cmd.Execute()`** delegates to the **cobra** command tree—real logic lives in `cmd/clusterctl/cmd/`.

## Root command: purpose statement

```56:60:cmd/clusterctl/cmd/root.go
// RootCmd is clusterctl root CLI command.
var RootCmd = &cobra.Command{
	Use:          "clusterctl",
	SilenceUsage: true,
	Short:        "clusterctl controls the lifecycle of a Cluster API management cluster",
```

**DevOps engineer:** Think of `clusterctl` as **helm-for-CAPI-providers** in spirit: it knows **provider metadata**, **version skew rules**, and **repository layout**, so you don’t hand-assemble dozens of YAML files for day-0.

> **Hinglish:** *Auth import blank isliye: GCP/Azure OIDC wala kubeconfig bhi kaam kare—warna CLI cluster tak pahunch hi na paaye.*

**Next:** [`test/e2e`](./14-test-e2e.md).
