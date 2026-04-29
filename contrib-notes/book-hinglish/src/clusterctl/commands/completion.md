# clusterctl completion — Simple Hinglish

## Ye command kya karta hai?

`clusterctl completion <bash|zsh|fish>` output me **shell completion code** deta hai.

Iska use case:

- jab aap terminal me type karte ho to `clusterctl <TAB>` auto-complete ho jaye

## Code-level idea

Implementation entry:

- `cmd/clusterctl/cmd/completion.go`

Wahan:

- bash: `cmd.Root().GenBashCompletion(...)`
- zsh/fish: Cobra ke corresponding generators

Bonus: `cmd/clusterctl/cmd/root.go` me “common flags” ke liye completion functions register hoti hain (e.g. kubeconfig context/namespace completions).

