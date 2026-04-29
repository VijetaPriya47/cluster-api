# clusterctl Configuration File — Simple Hinglish

> **Note:** Yahan config file ke blocks ka simple idea hai. Exact YAML/schema ke liye English source check karo.

## aadhikaarika srota

- ripojaitarii: [`docs/book/src/clusterctl/configuration.md`](../../../../../docs/book/src/clusterctl/configuration.md)
- veba (angrejaii): [clusterctl Configuration File](https://cluster-api.sigs.k8s.io/clusterctl/configuration.html)

## Simple blocks (kaunsi cheez kis kaam ke liye)

### Provider repositories

Yahan clusterctl ko bataya jata hai ki kaunse providers kahan se download/resolve karne hain.

Har provider ke saath `name`, `type`, aur provider repository `URL` hota hai (plus defaults bhi aate hain).

### Variables

Templates aur provider YAML process karne ke time jo values chahiye hoti hain unko clusterctl:

- environment variables se read kar sakta hai
- config file se bhi read kar sakta hai

Same key dono jagah ho to **env var priority** leti hai.

### Cert-Manager configuration

`clusterctl init/upgrade` cert-manager ko ensure karta hai (webhook/API ready hone ke liye).

Config me cert-manager ka source (URL/repo), version/timeout type cheezen hoti hain. Agar cert-manager “externally managed” detected ho (clusterctl labels absent), to upgrade/version checks skip hote hain.

### Migrating to user-managed cert-manager

Agar aap cert-manager khud manage karte ho, clusterctl us case ko detect karke “cert-manager upgrade” wali steps chhod deta hai. (Management responsibility aapki hoti hai.)

### Avoiding GitHub rate limiting

Clusterctl aksar provider manifests GitHub releases se fetch karta hai. Rate limit avoid karne ke liye:

- config/env me GitHub token set kiya ja sakta hai
- clusterctl config download/caching behavior use hota hai (temporary downloaded config clean-up bhi hota hai)

### Overrides Layer

Overrides ka matlab: provider/cert-manager manifests ke kuch parts ko custom values se override karna.

Yeh private registries, air-gapped environments, ya custom images ki wajah se kaam aata hai.

### Image overrides

Image overrides ek specific override type hai: “jo image tag/provider yaml me hai, use aapke desired registry/tag se replace” karna.

### Debugging/Logging

clusterctl ke outputs ko debug karne ke liye log-level/config/log usage related flags/env use hote hain. (RootCmd initConfig me log threshold set hota hai.)

### Skip checking for updates

`CLUSTERCTL_DISABLE_VERSIONCHECK=true` ho to RootCmd ka `PersistentPostRunE` version check skip karta hai.

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
