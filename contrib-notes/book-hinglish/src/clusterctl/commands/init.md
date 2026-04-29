# clusterctl init — Simple Hinglish

> **Note:** Detailed flags/YAML ke liye English source check karo. Yahan sirf “what happens” ko simple samjhaya hai.

## Official source

- Repo: [`docs/book/src/clusterctl/commands/init.md`](../../../../../../docs/book/src/clusterctl/commands/init.md)
- Web: [clusterctl init](https://cluster-api.sigs.k8s.io/clusterctl/commands/init.html)

## `clusterctl init` ka matlab

`clusterctl init` aapke **management cluster** ko ready karta hai.

Management cluster me (Core provider + selected providers) install hote hain, jisse wahan:

- **Cluster API controllers/reconcilers** chalne lagte hain (management cluster CRs reconcile)
- CRDs + Deployments/objects exist hone lagte hain

## Code-level flow (simple waterfall)

Command entrypoint: `cmd/clusterctl/cmd/init.go`

1. `runInit()`:
   - `client.New(ctx, cfgFile)` se clusterctl config load hota hai
2. `c.Init(ctx, options)` call hota hai:
   - `InitOptions` me core/bootstrap/infrastructure/control-plane providers + target namespace + wait/validate flags aate hain
3. Result:
   - provider components ke manifests generate/process hote hain (templates + variable substitution)
   - management cluster me apply hote hain
   - agar `--wait-providers` hai to deployments ready hone ka wait hota hai
   - agar `--validate` true hai to management cluster par success check hota hai

## Most important flags (quick map)

- `--kubeconfig` + `--kubeconfig-context`: management cluster access
- `--core`: core provider version (Cluster API core)
- `--infrastructure`, `--bootstrap`, `--control-plane`: selected providers
- `--ipam`, `--runtime-extension`, `--addon`: optional extra provider types
- `--target-namespace`: providers kahan deploy honge
- `--wait-providers` + `--wait-provider-timeout`: wait behavior
- `--validate/--no-validate`: deploy validation

## Subcommand: `init list-images`

`clusterctl init list-images` dry-run ki tarah hai:
- jo images install karni padengi unki list print karta hai

