# Auto-rotating certificates using Kubeadm Control Plane (KCP) — Simple Hinglish

KCP me certificate rotation ka common approach:

- cert expiry detect
- phir control-plane machines ka rollout trigger
- so new machines fresh certs ke saath join ho jayein

## Official source

- Repo: [`docs/book/src/tasks/certs/auto-rotate-certificates-in-kcp.md`](../../../../../../docs/book/src/tasks/certs/auto-rotate-certificates-in-kcp.md)
- Web: [Auto-rotating certificates in KCP](https://cluster-api.sigs.k8s.io/tasks/certs/auto-rotate-certificates-in-kcp.html)

## Rollout kaise fit hota hai?

Certificates rotate karne ke liye KCP generally:

- next control plane machine create karta hai
- old machine replace karta hai (rolling)

Isse:

- etcd quorum safe rehta hai
- API server availability maintain hoti hai

## Configuring / triggering rollout (high level)

- rollout strategy/controls configure karte ho (provider-specific knobs)
- expiry threshold aate hi rollout trigger hota hai (or aap manually trigger karte ho)

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
