# Introduction — simple / Hinglish notes

> **Ek line:** Cluster API = “Kubernetes ke andar se **aur Kubernetes clusters** banane / upgrade / operate karne” ka tareeka—YAML + controllers, jaise tum apps ke liye Deployment use karte ho.

## Official English (source of truth)

- Repo: [`docs/book/src/introduction.md`](../../../../docs/book/src/introduction.md)
- Web: [Introduction](https://cluster-api.sigs.k8s.io/introduction.html)

---

## Simple story (Hinglish + English)

**Problem:** Har cloud / distro ka apna installer hai—100+ tarah se cluster banta hai. Day-2 (upgrade, scale, delete) har jagah alag.

**Cluster API ka idea:**

- **Declarative:** Tum `Cluster`, `Machine` jaise **Custom Resources** likhte ho—yeh “desired state” etcd mein store hoti hai.
- **Controllers** (operators) cloud API / Docker (CAPD) se baat karke **reality** ko us state ke paas laate hain.
- **Extensible:** Infra (AWS, Azure, …), bootstrap (kubeadm, …), control-plane provider **alag repos** mein plug hote hain—core contract same.

**Management vs workload (yaad rakho):**

- **Management cluster:** Jahan CAPI controllers chal rahe hain.
- **Workload cluster:** Jo cluster tumne banaya—wahan apps chalti hain.

**Kubeadm se rishta:** Kubeadm = node bootstrap tool; CAPI usko **orchestrate** karta hai saath saath infra providers ke.

## Is page pe aage kya padhna hai (book jaisa order)

- [Quick Start](./user/quick-start.md) — haath se try karo  
- [Concepts](./user/concepts.md) — `Cluster`, `Machine`, providers  
- [Developer guide](./developer/getting-started.md) — code / dev setup  

---

*Companion file — `contrib-notes/book-hinglish`. Poori detail official English page par.*
