# clusterctl delete — Simple Hinglish

`clusterctl delete ...` management cluster se **providers** (core/bootstrap/infrastructure/control-plane/ipam/runtime-extension/addon) ya unke parts ko delete karta hai.

## Code-level flow (rough)

Entrypoint: `cmd/clusterctl/cmd/delete.go`

1. flags se decide hota hai:
   - `--all` ya
   - kaunse providers types/names (e.g. `--infrastructure aws`)
2. validation:
   - `--all` ke saath provider flags nahi use ho sakte
3. `c.Delete(ctx, client.DeleteOptions{...})` call hota hai

## Important flags (simple meaning)

- `--infrastructure/--bootstrap/--control-plane/--core/...`: konse provider delete karne
- `--include-namespace`: provider hosting namespace ko bhi delete (dangerous)
- `--include-crd`: provider CRDs ko bhi delete
- `--all`: sab providers delete (CRDs + resources orphan ho sakte hain)

## Controllers relation

Providers delete karne se management cluster me chal rahe controllers/reconcilers bhi stop ho sakte hain (kyunki their Deployments/CRDs delete ho jate hain ya unavailable ho jati hai).

## Official source

- Repo: [`docs/book/src/clusterctl/commands/delete.md`](../../../../../../docs/book/src/clusterctl/commands/delete.md)

