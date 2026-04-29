# Overview of clusterctl — Simple Hinglish

> **Note:** Exact flags/YAML ke liye official English pages dekho. Yahan ka goal: “clusterctl kis tarah kaam karta hai” ko simple words me samjhana.

## clusterctl ka main purpose

`clusterctl` ek CLI hai jo **Cluster API management cluster** ka lifecycle manage karta hai.

Simple version:

- `clusterctl init` = management cluster me **core components + selected providers** install karna (CRDs, Deployments, etc.)
- `clusterctl generate ...` = **workload cluster** ke liye templates/YAML banwana (variable substitution ke saath)
- `clusterctl get/delete/describe/move/upgrade` = management cluster par operations

## “Controllers” kahan fit hote hain?

`clusterctl init` ke baad jo controllers/reconcilers chalne lagte hain, woh **Core provider** se aate hain.

Core provider ke controllers (jaise `Cluster`, `Machine`, `MachineSet`, `MachineDeployment`, `MachinePool`, `MachineHealthCheck`, `ClusterResourceSet`, `ClusterTopology`) management cluster me reconciliation karte hain:

- `Cluster` orchestrate karta hai (infra/control-plane + kubeconfig + descendants)
- `MachineSet` replicas/machines sync karta hai
- `MachineDeployment` rollout strategy ke basis par MachineSets plan/apply karta hai
- `Machine` bootstrap/infra/node lifecycle complete karta hai

Yani: **clusterctl = install/template tool**, aur **controllers = running logic**.

## Root command ka “waterfall” (code high-level)

`cmd/clusterctl/main.go` me bas:

`cmd.Execute()` -> `cmd/root.go` ka `RootCmd.Execute()`.

`RootCmd` me:

1. `handlePlugins()`:
   - agar requested sub-command root commands me nahi mila, to plugin executable search karke run ho sakta hai
2. command execute:
   - har command `config.New(ctx, cfgFile)` aur `client.New(ctx, cfgFile)` use karta hai
3. `PersistentPostRunE`:
   - version check karta hai (agar `CLUSTERCTL_DISABLE_VERSIONCHECK=true` ho to skip)
   - remote config download hua ho to file delete karta hai

## Official source

- Repo: [`docs/book/src/clusterctl/overview.md`](../../../../../docs/book/src/clusterctl/overview.md)
- Web: [Overview of clusterctl](https://cluster-api.sigs.k8s.io/clusterctl/overview.html)

