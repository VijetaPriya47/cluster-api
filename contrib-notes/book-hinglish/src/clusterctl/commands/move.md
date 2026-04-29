# clusterctl move — Simple Hinglish

`clusterctl move` management clusters ke beech **Cluster API objects + dependencies** ko move karta hai.

## Kab use hota hai?

- jab aap management cluster ko replace/migrate kar rahe ho
- destination cluster par required provider components already installed hone chahiye

## Code-level mapping (rough)

Entrypoint: `cmd/clusterctl/cmd/move.go`

Main idea:

- `--to-kubeconfig` / `--to-directory` / `--from-directory` / `--from-kubeconfig` combinations se source & destination decide hota hai
- optional `--dry-run` se actions preview
- `--hide-api-warnings` se kubernetes apiserver warnings hide/log behavior adjust hota hai
- `c.Move(ctx, client.MoveOptions{...})` se actual move hota hai

## Useful flags quick map

- `--kubeconfig` / `--kubeconfig-context`: source management cluster
- `--to-kubeconfig` / `--to-kubeconfig-context`: destination management cluster
- `--from-directory` / `--to-directory`: directory based transfer
- `--namespace/-n`: workload cluster namespace

## Controllers relation

Move ke baad controllers new management cluster me reconcile continue karte hain, kyunki objects wahan exist/updated hote hain.

