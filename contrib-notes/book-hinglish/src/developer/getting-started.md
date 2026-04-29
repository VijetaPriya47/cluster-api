# Developer Guide — simple / Hinglish notes

> **Ek line:** CAPI **ka code** chalane / badalne ke liye—Docker, kind, kubebuilder, cert-manager, Tilt—yeh entry page hai.

## Official English

- Repo: [`docs/book/src/developer/getting-started.md`](../../../../docs/book/src/developer/getting-started.md)
- Web: [Developer getting started](https://cluster-api.sigs.k8s.io/developer/getting-started.html)

---

## Mental model

- **Kai binaries:** Core manager, kubeadm bootstrap manager, kubeadm control-plane manager, **infrastructure provider** (e.g. CAPA, ya dev mein **CAPD**). Sabko sahi version par **management cluster** pe chalna padta hai.
- **CAPD:** Laptop / CI ke liye “fake VMs” = Docker containers; production nahi.
- **Tilt:** Bar-bar `docker build` + reload—fast inner loop.

## Prerequisites (simple list)

1. **Docker** — images build.  
2. **kind** — chhota Kubernetes = management cluster.  
3. **Registry** — images push/pull (ya kind load).  
4. **kustomize** — manifests.  
5. **kubebuilder** — local dev tooling alignment.  
6. **cert-manager** — webhook certs (management cluster par).  

## Flow (high level)

1. Management cluster ready karo (kind).  
2. cert-manager lagao.  
3. CAPI + providers install (clusterctl ya dev mein Tilt).  
4. `Cluster` / `Machine` YAML apply karo; controllers reconcile karenge.

## Aage kahan jayein (book tree)

- [Core overview](./core/overview.md)  
- [Tilt](./core/tilt.md)  
- [Repository layout](./core/repository-layout.md)  
- [Contributing](../CONTRIBUTING.md) — CLA, PR process  

---

*Companion — `contrib-notes/book-hinglish`.*
