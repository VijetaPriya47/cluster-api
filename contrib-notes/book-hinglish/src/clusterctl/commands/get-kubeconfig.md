# clusterctl get kubeconfig — Simple Hinglish

`clusterctl get kubeconfig <workload-cluster-name>` workload cluster ke liye kubeconfig file ka content print karta hai.

## Code-level mapping (rough)

Entrypoint: `cmd/clusterctl/cmd/get_kubeconfig.go`

Flow:

1. `client.New(ctx, cfgFile)` se clusterctl config load
2. `c.GetKubeconfig(ctx, client.GetKubeconfigOptions{...})` call
3. result string ko `fmt.Println(out)` se STDOUT pe print

## Common flags

- `--namespace/-n`: workload cluster kis namespace me hai
- `--kubeconfig`: management cluster access ke liye kubeconfig path
- `--kubeconfig-context`: management kubeconfig context

## Controllers relation

Yeh command controllers start nahi karta. Yeh sirf “access/correct kubeconfig” deta hai—taaki workload cluster ke controllers/reconcilers se properly interact ho sake.

## Official source

- Repo: [`docs/book/src/clusterctl/commands/get-kubeconfig.md`](../../../../../../docs/book/src/clusterctl/commands/get-kubeconfig.md)

