# clusterctl generate provider — Simple Hinglish

## Is command ka kaam

`clusterctl generate provider` provider components ke liye YAML/templates generate karta hai.

Example:

- `clusterctl generate provider --infrastructure aws`
- `clusterctl generate provider --infrastructure aws --describe` (variable substitution ke bina)
- `clusterctl generate provider --infrastructure aws:v0.4.1 --raw` (yaml me raw config)

## Code-level mapping (waterfall idea)

Entrypoint: `cmd/clusterctl/cmd/generate_provider.go`

Main flow:

1. `parseProvider()`:
   - jo `--core/--bootstrap/--control-plane/--infrastructure/...` flag diya hai uske basis par provider type decide hota hai
   - aur validate hota hai ki multiple provider flags ek saath set na ho
2. `client.New(...)` se clusterctl config load hoti hai
3. `c.GenerateProvider(...)` call hota hai:
   - provider repository se provider components fetch
   - variable substitution / raw processing ke hisaab se output format decide
4. final output:
   - `--describe` -> text output
   - warna -> YAML print (STDOUT ya `--write-to`)

## “Controllers” relation

Yeh command **controllers start** nahi karta.

Yeh provider templates/YAML output karta hai. Jab aap in YAML ko management cluster me apply karte ho (typically `clusterctl init` ya `upgrade apply` se), phir **management cluster me controllers/reconcilers** chalna start hote hain.

