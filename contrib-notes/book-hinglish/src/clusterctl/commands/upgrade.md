# clusterctl upgrade — Simple Hinglish

`clusterctl upgrade` ka concept:

1. **plan**: kaunsa provider version available hai uski recommended list
2. **apply**: plan ke hisaab se management cluster me providers/core ko update install apply karna

## Subcommands

### `clusterctl upgrade plan`

- Cert-manager ke upgrade ka plan bhi check ho sakta hai
- `c.PlanUpgrade(...)` se upgrade plans milte hain
- output me table/tabwriter ke through “current -> next” versions dikhte hain

Entrypoint (approx): `cmd/clusterctl/cmd/upgrade_plan.go`

### `clusterctl upgrade apply`

- `c.ApplyUpgrade(...)` call karta hai
- options me:
  - `--contract` (Cluster API contract version, e.g. `v1beta2`)
  - ya individual provider flags (`--core`, `--infrastructure`, `--bootstrap`, `--control-plane`, `--ipam`, `--runtime-extension`, `--addon`)
  - `--wait-providers` optional wait

Entrypoint (approx): `cmd/clusterctl/cmd/upgrade_apply.go`

## Controllers relation

Upgrade ke baad management cluster me controllers Deployments/CRDs update hote hain.
Wahi controllers phir nayi versions ke hisaab se reconciliation continue karte hain.

