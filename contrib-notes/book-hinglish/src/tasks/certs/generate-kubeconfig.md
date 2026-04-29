# Generating a kubeconfig with your own CA — Simple Hinglish

Kabhi-kabhi aap chahte ho ki workload cluster ka kubeconfig **aapki own CA** se signed ho (org PKI rules, compliance, etc.).

## Official source

- Repo: [`docs/book/src/tasks/certs/generate-kubeconfig.md`](../../../../../../docs/book/src/tasks/certs/generate-kubeconfig.md)
- Web: [Generating a Kubeconfig with your own CA](https://cluster-api.sigs.k8s.io/tasks/certs/generate-kubeconfig.html)

## Simple mental model

Kubeconfig me typically ye parts hote hain:

- cluster CA bundle (server verify ke liye)
- user client cert + key (client auth)
- server endpoint (API server URL)

“Own CA” ka meaning:

- CA certificate chain aap control karte ho
- client certs us CA se issue/rotate hote hain (process provider/controller dependent)

## Practical flow (high level)

1. Aap CA material prepare karte ho (CA cert + key OR signing process)
2. CAPI components ko batate ho ki kubeconfig/certs ke liye custom CA use karo
3. Generated kubeconfig ko validate karte ho (kubectl can connect)

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
