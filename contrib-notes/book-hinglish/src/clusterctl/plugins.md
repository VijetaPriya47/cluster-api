# clusterctl Extensions with Plugins — Simple Hinglish

`clusterctl` me **plugin** mechanism hota hai. Matlab: agar aap koi command run karte ho jo built-in commands list me nahi hai, to clusterctl PATH me extra executables search karke run kar sakta hai.

## Code-level idea (root command)

`cmd/clusterctl/cmd/root.go` me `handlePlugins()`:

- args[1:] dekhta hai
- agar requested command built-in root commands me nahi milta,
- to `handlePluginCommand(...)` call karta hai

`handlePluginCommand()` me:

- non-flag args collect hoti hain (jo `-` se start nahi karte)
- dash (`-`) ko underscore (`_`) me convert kiya jata hai plugin-name parts me
- plugin executable ko try kiya jata hai PATH me: longest possible name se shortest possible name tak
- mil gaya to `pluginHandler.Execute(...)` karke execute ho jata hai

## Plugin executable ka expected naming (concept)

Plugin binaries usually `clusterctl-<something>` pattern me hote hain, aur `<something>` me aapke non-flag args ka concatenation hota hai (dash-separated search).

## Controllers relation

Plugin khud controllers start nahi karte. Plugins typically:

- additional admin commands provide karte hain, ya
- templates/config generate karte hain,

aur phir controllers ka work wahi rehta hai (management/workload cluster reconcile).

