# Concepts — simple / Hinglish notes

> **Ek line:** Yeh chapter **shabdon ka map** hai—`Cluster`, `Machine`, provider types—bina iske baaki book uljhegi.

## Official English

- Repo: [`docs/book/src/user/concepts.md`](../../../../docs/book/src/user/concepts.md)
- Web: [Concepts](https://cluster-api.sigs.k8s.io/user/concepts.html)

---

## Sabse important ideas

### Deployment jaisa, par Machines ke liye

- **Deployment** → Pods control karta hai.  
- **MachineDeployment** → **worker Machines** (hosts / Nodes) control karta hai.  
- **KubeadmControlPlane** → **control plane** Machines (API server wala hissa) manage karta hai.

### Management cluster

Jahan **Cluster API + providers** chalte hain; yahi par `Cluster`, `Machine` CRs rehti hain. Isi se tum **workload cluster** ka lifecycle chalate ho.

### Cluster (CR)

- **Matlab:** “Ek aisa Kubernetes cluster jisko CAPI manage kare.”  
- **Portable cheez:** Network CIDRs jaise common fields `spec` par.  
- **Cloud-specific cheez:** `infrastructureRef`, `controlPlaneRef` se **alag CRs** point karte ho (jaise `VSphereCluster`, `KubeadmControlPlane`).

### Machine (CR)

- **Matlab:** “Ek host jo Node banega.”  
- **`infrastructureRef`:** VM / machine cloud mein kaise bane.  
- **`bootstrap.configRef`:** Pehli boot par kubeadm / cloud-init kya kare.  
- Machines **immutable** treat hoti hain—spec badli toh aksar **naya Machine**, purana replace (Deployment jaisa rollout).

### Provider types (char)

1. **Core** — `Cluster`, `Machine`, topology… portable contract.  
2. **Infrastructure** — VM, network, LB (e.g. `AWSMachine`).  
3. **Bootstrap** — join/init data (e.g. `KubeadmConfig`).  
4. **Control plane** — HA control plane rollout (e.g. `KubeadmControlPlane`).

### CRD / CR short

- **CRD** = API server ko naya `kind` sikhana.  
- **CR** = us kind ka ek object (tumhara YAML).

---

## Next in book

- [Quick start](quick-start.md)  
- [Tasks](../tasks/index.md) — practical recipes  

---

*Companion — `contrib-notes/book-hinglish`. Diagrams official Concepts page par.*
