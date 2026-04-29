# Using Custom Certificates — Simple Hinglish

Custom certificates ka use tab hota hai jab:

- aapki org PKI policies strict hain
- aap default self-signed/cert-manager generated certs avoid karna chahte ho

## Official source

- Repo: [`docs/book/src/tasks/certs/using-custom-certificates.md`](../../../../../../docs/book/src/tasks/certs/using-custom-certificates.md)
- Web: [Using Custom Certificates](https://cluster-api.sigs.k8s.io/tasks/certs/using-custom-certificates.html)

## Simple mental model

Control plane me multiple certs hoti hain (API server, etcd, front-proxy, client certs, etc.).

“Custom certs” ka matlab:

- aap apne certs/keys provide karte ho (usually as Secrets)
- bootstrap/control-plane provider unko use karke cluster bring-up karta hai

Important: custom certs use karte time rotation/renewal strategy clear honi chahiye (manual vs automated).

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
