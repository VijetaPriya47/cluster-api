# clusterctl commands — Simple Hinglish

> **Note:** Yahan main “kaunse major commands” aur unka code-level idea likh raha hoon. Detailed flags ke liye English pages dekho.

## Built-in commands (management workflow)

- `clusterctl init`
  - management cluster me core + providers install
- `clusterctl config repositories`
  - clusterctl.yaml me providers ke repository URLs ki list
- `clusterctl generate cluster NAME`
  - workload cluster template/YAML generate
- `clusterctl generate provider --infrastructure ...`
  - provider component templates generate
- `clusterctl generate yaml --from ...`
  - clusterctl YAML processor se variable substitution
- `clusterctl get kubeconfig NAME`
  - workload cluster ka kubeconfig print
- `clusterctl delete ...`
  - providers/resources ko delete
- `clusterctl describe cluster NAME`
  - workload cluster ka “tree view” status print
- `clusterctl move ...`
  - management clusters ke beech Cluster API objects/dependencies move
- `clusterctl upgrade plan`
  - recommended next versions list
- `clusterctl upgrade apply`
  - upgrade plan apply karke providers update

## Alpha / debugging-type commands

- `clusterctl alpha rollout restart|pause|resume ...`
  - (alpha) rollout management (kuch resource types par)
- `clusterctl completion <bash|zsh|fish>`
  - shell completion code
- `clusterctl version`
  - clusterctl version output

## Plugins (extensions)

`cmd/root.go` me `handlePlugins()` hota hai:

- agar requested command built-in commands me nahi mila,
- clusterctl plugin executable search karke run kar sakta hai.

## Official source

- Repo: [`docs/book/src/clusterctl/commands/commands.md`](../../../../../../docs/book/src/clusterctl/commands/commands.md)
- Web: [clusterctl commands](https://cluster-api.sigs.k8s.io/clusterctl/commands/commands.html)

