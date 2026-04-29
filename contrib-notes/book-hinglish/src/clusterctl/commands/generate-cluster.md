# clusterctl generate cluster — Simple Hinglish

## Is command ka kaam

`clusterctl generate cluster NAME` workload cluster banane ke liye **templates/YAML** generate karta hai.

Simple idea:

- Provider repository (ya ConfigMap/URL/local file) se cluster template read hota hai
- Template ke andar `variables` hoti hain
- `variables` ki values (env vars + config file se) substitute karke final YAML output milta hai

## Code me entrypoint (rough mapping)

`cmd/clusterctl/cmd/generate_cluster.go`

Yahan `RunE` ka flow:

1. `client.New(ctx, cfgFile)` se config load
2. `client.GetClusterTemplate(...)` call
3. `--list-variables` ho to variables print, warna YAML print/output file me

## Main options (flags) — new contributor cheat-sheet

- `--kubeconfig` + `--kubeconfig-context`: management cluster access
- `--target-namespace`: workload cluster ka namespace
- `--kubernetes-version`: workload cluster ke liye k8s version
- `--control-plane-machine-count` / `--worker-machine-count`: nodes count (agar provider supports kare)
- `--infrastructure` + `--flavor`: kis infra provider ka template use karna hai
- `--from <URL|file|->`: template source override
- `--from-config-map ...`: ConfigMap se template
- `--from-config-map-key`: ConfigMap.Data key

## “Controllers” se relation

Yeh command controllers start nahi karta.

`generate cluster` ka output baad me workload cluster me apply/created resources banata hai, aur phir **workload cluster** me controllers (provider + core) reconcile karna start karte hain.

