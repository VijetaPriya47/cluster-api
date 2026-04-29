# Certificate Management — Simple Hinglish

Certificates ka topic CAPI me mostly 3 areas me aata hai:

1. **workload cluster kubeconfig** generate/access (CA + client certs)
2. **custom certificates** use karna (org policies / existing PKI)
3. **certificate rotation** (expiry aane par rollout/renew)

## Official source

- Repo: [`docs/book/src/tasks/certs/index.md`](../../../../../../docs/book/src/tasks/certs/index.md)
- Web: [Certificate Management](https://cluster-api.sigs.k8s.io/tasks/certs/index.html)

## Core controllers se relation (simple)

- `Cluster` controller kubeconfig secrets / access-related resources manage kar sakta hai (provider behavior pe depend)
- `KubeadmControlPlane` (KCP) certificates/rotation workflow ko drive kar sakta hai, usually machine rollout ke through

Is folder ki pages me aapko practical “how-to” steps milenge:

- apni CA se kubeconfig generate
- custom certs inject/use
- auto-rotation configure

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
