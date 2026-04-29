# clusterctl generate yaml — Simple Hinglish

## Is command ka kaam

`clusterctl generate yaml --from ...` ek YAML “template” ko:

1. read karta hai (URL/file/stdin)
2. uske andar jo `variables` placeholders hain unki values substitute karta hai
3. final YAML output deta hai

Yeh **provider template** processing ka general-purpose tool hai.

## Code-level mapping

Entrypoint: `cmd/clusterctl/cmd/generate_yaml.go`

`generateYAML(r, w)` me:

- `client.New(ctx, cfgFile)` -> clusterctl config load
- `client.ProcessYAML(ctx, options)` -> YAML processor run
- `--list-variables` ho to template ko process kiye bagair variable list print hoti hai
- warna generated YAML STDOUT me print hota hai

## Example usage (idea)

- `clusterctl generate yaml --from https://.../template.yaml`
- `clusterctl generate yaml --from ~/workspace/template.yaml`
- `cat template.yaml | clusterctl generate yaml --list-variables`

## Controllers relation

Yeh command controllers start nahi karta. Yeh sirf YAML banata hai.

Jab aap generated YAML ko management cluster me apply karte ho, tab controllers running start hote hain.

