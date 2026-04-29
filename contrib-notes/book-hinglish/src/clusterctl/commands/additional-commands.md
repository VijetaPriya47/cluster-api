# clusterctl — additional commands (Simple Hinglish)

## clusterctl help

Kisi bhi command ka help dekhne ke liye:

`clusterctl help [command]`

## clusterctl version

Installed `clusterctl` ka version print hota hai (`cmd/clusterctl/cmd/version.go`).

## clusterctl init list-images

Yeh “dry-run” style command hai:

- jo images install karni padengi unki list print karta hai
- install nahi karta

## Code me “version check” ka note

`cmd/root.go` me har command ke baad `PersistentPostRunE` me version check run hota hai.

`CLUSTERCTL_DISABLE_VERSIONCHECK=true` set ho to skip ho jata hai.

