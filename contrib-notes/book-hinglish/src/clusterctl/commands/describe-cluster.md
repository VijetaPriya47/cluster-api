# clusterctl describe cluster — Simple Hinglish

## Ye command kya karta hai?

`clusterctl describe cluster NAME` workload cluster ka status “tree view” me print karta hai.

Iska purpose:

- quickly samajhna ki cluster me problems kahan ho rahi hain (conditions/reasons)
- machines/machinesets/templates related context ek jagah dekhna

## Code-level mapping (rough)

Entrypoint: `cmd/clusterctl/cmd/describe_cluster.go`

Flow:

1. `client.New(...)`
2. `c.DescribeCluster(ctx, DescribeClusterOptions{...})`
3. Output `cmdtree.PrintObjectTree(...)` se STDOUT par print

## Key options (from flags)

- `--show-conditions <Kind[/name]>`: kis kind ke conditions show karne hain
- `--show-machinesets`, `--show-resourcesets`, `--show-templates`
- `--echo`: ready condition true ho to extra machine infra/bootstrap echo
- `--grouping`: same ready condition status wale nodes ko group karna

## Controllers relation

Describe cluster controllers run nahi karta.

Yeh sirf controllers ke outputs (conditions/status) ko read karke visualize karta hai.

## Official source

- Repo: [`docs/book/src/clusterctl/commands/describe-cluster.md`](../../../../../../docs/book/src/clusterctl/commands/describe-cluster.md)

