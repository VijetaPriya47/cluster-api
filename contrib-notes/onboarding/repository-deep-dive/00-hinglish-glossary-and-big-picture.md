# 00 — Hinglish glossary aur poora scene (Kubernetes + Cluster API)

Ye page **bade technical shabdon** ka matlab **Hinglish** mein batata hai, phir batata hai **ye sab milkar kaise kaam karte hain**, aur **kubernetes-sigs/cluster-api** aur **pure Kubernetes** project mein kyun matter karte hain. English terms **as-is** rehti hain kyunki codebase aur docs mein wahi dikhte hain—bas explain Hinglish mein hai.

> **Note:** *Yeh “textbook definition” + “engineer wali intuition” dono hai. Agar koi term pe aur depth chahiye to official docs ([kubernetes.io](https://kubernetes.io), [cluster-api.sigs.k8s.io](https://cluster-api.sigs.k8s.io)) aur is book ke baaki chapters dekho.*

---

## 1. Shabdon ki dictionary (A–Z style, practical order)

### API Server (`kube-apiserver`)

**Matlab:** Kubernetes ka **single entry gate** jahan se tum YAML apply karte ho, `kubectl get` karte ho. Ye **validate** karta hai, **store** karta hai (etcd ke through), aur **watch** events bhejta hai.

**Hinglish intuition:** *Socho “bank ka main counter”—sab transaction yahi se register hota hai; seedha vault (etcd) se juda hai.*

**K8s mein matter:** Bina API server ke koi “Kubernetes cluster” nahi—yahi contract hai.

**CAPI mein matter:** Management cluster ka API server hi **`Cluster` / `Machine`** jaise CRs hold karta hai; CAPI controllers isi se read/write karte hain.

---

### etcd

**Matlab:** **Distributed, consistent key-value store** jahan Kubernetes apna **desired + observed state** rakhta hai.

**Hinglish intuition:** *“Sach ka register” / ledger—API server isi ko truth maanta hai.*

**K8s mein matter:** Control plane ka **brain storage**; backup/restore strategy yahi se judi hoti hai.

**CAPI mein matter:** Tumhara `Cluster` YAML bhi yahi persist hota hai; GitOps + etcd = **two sources of truth** agar sync na ho—isliye process important hai.

---

### Node

**Matlab:** Machine (VM/bare metal) jahan **kubelet** chalta hai aur workload **Pods** schedule hote hain.

**Hinglish intuition:** *Worker “site” jahan containers actually chalte hain.*

**CAPI mein:** **`Machine`** resource often **ek Node banne ka intent** dikhata hai; cloud mein pehle VM, phir Node register.

---

### Pod

**Matlab:** Smallest deployable unit—ek ya zyada containers share karte hain network/storage context.

**Hinglish intuition:** *“Ek chhota group” jo saath schedule hota hai.*

**CAPI se farq:** **`Machine` Pod nahi hai**—Machine = **host-level** abstraction; Pod us host *andar* chalta hai workload cluster pe.

---

### Deployment (core Kubernetes)

**Matlab:** Declarative rollout of **ReplicaSet** → **Pods**; rolling update, scale.

**Hinglish intuition:** *“Itne replicas chahiye, template ye hai—khud manage karo.”*

**CAPI analogy:** **`MachineDeployment`** same *idea* worker Machines par lagayi gayi hai—Machines “cattle” style replace hoti hain.

---

### Controller

**Matlab:** Loop jo **desired state** (spec) aur **actual state** (real world / status) ko compare karke actions leta hai.

**Hinglish intuition:** *“Auto-pilot jo slack nahi khaata—bar-bar check karta hai.”*

**K8s:** Deployment controller, ReplicaSet controller, etc.

**CAPI:** `cluster-api-controller-manager` ke andar **Cluster controller**, **Machine controller**, … sab “controllers” hi hain.

---

### Operator

**Matlab:** Usually **controllers + webhooks + RBAC + packaging** ka bundle jo **complex app** ko Kubernetes par manage kare.

**Hinglish intuition:** *“Human operator ka software version”—rules + automation ek saath.*

**CAPI:** Core provider + bootstrap + control-plane + infra provider milke **Cluster API ecosystem** banate hain—practical taur par “operators ka network”.

---

### CRD (CustomResourceDefinition)

**Matlab:** Built-in resource jo **naya `kind`** API server mein register karta hai (schema ke saath).

**Hinglish intuition:** *“Naya form type bank mein register karna”—ab tum `kubectl apply` se woh form bhar sakte ho.*

**CAPI:** `clusters.cluster.x-k8s.io` jaise CRDs `config/crd/bases` se aate hain, Go types se generate.

---

### CR (Custom Resource)

**Matlab:** CRD ke baad tum jo object create karte ho—e.g. `kind: Cluster`.

**Hinglish intuition:** *Bhar hua form / record.*

---

### Spec vs Status

**Matlab:**

- **Spec:** User ne **kya maanga** (desired).
- **Status:** System ne **kya dekha / kiya** (observed).

**Hinglish intuition:** *Spec = “mujhe yeh chahiye”; Status = “abhi tak yeh hua, yeh pending hai”.*

**Rule of thumb:** Normal clients **spec** edit karte hain; controllers **status** update karte hain (achhi practice / subresource).

---

### Reconcile / Reconciliation loop

**Matlab:** Controller ka ek **iteration**: object fetch → compare → act → maybe requeue.

**Hinglish intuition:** *“Ek round jhaadu”—ghar saaf nahi hua to dubara aaunga.*

**controller-runtime:** `Reconcile(ctx, req) (Result, error)` yehi entry point hai.

---

### Level-triggered vs edge-triggered (concept)

**Level-triggered:** *“Final desired state kya hai?”* — beech mein event miss ho to bhi dubara sync se theek ho sakta hai.

**Edge-triggered:** *“Is pal kya change hua?”* — miss hua to problem.

**Hinglish:** *CAPI/K8s controllers zyada **level-triggered** soch pasand karte hain—isliye idempotent code important hai.*

---

### Idempotent

**Matlab:** Same operation do baar karo to **bhi safe**—world weird state mein na jaaye.

**Hinglish:** *“Dobara button dabao, blast na ho.”*

---

### Finalizer

**Matlab:** `metadata.finalizers` mein string; jab tak finalizer hai, object **fully delete** nahi hota—controller pehle cleanup karta hai, phir finalizer hataata hai.

**Hinglish intuition:** *“Delete se pehle checklist poori karo” wala checkpoint.*

**CAPI:** `ClusterFinalizer`, `KubeadmControlPlaneFinalizer`, etc.

---

### Owner reference / garbage collection

**Matlab:** Child object parent se **jura** hota hai; parent delete → often children **GC** ho jaate hain (rules ke hisaab se).

**Hinglish intuition:** *“Boss delete hua to team ka kya hoga?”—Kubernetes isko automate karta hai.*

---

### Admission webhook (Validating / Mutating)

**Matlab:** Object etcd mein save hone **se pehle** API server **webhook** ko pooch sakta hai—**reject** (validating) ya **default/change** (mutating).

**Hinglish intuition:** *“Gatekeeper + editor” — galat YAML andar hi nahi jaati, ya auto-fix milta hai.*

---

### RBAC (Role, ClusterRole, Binding)

**Matlab:** Kaunsa **ServiceAccount** kis resource par **kaun sa verb** (`get`, `list`, `watch`, `create`, …) chala sakta hai.

**Hinglish intuition:** *“Permit room”—har controller ko sirf utni permission jitni kaam ke liye zaroori.*

**CAPI:** `+kubebuilder:rbac` markers se **generate** hota hai—code aur security policy saath chalte hain.

---

### ServiceAccount

**Matlab:** Pod / controller ke liye **cluster identity** jisse API server pe calls jaati hain.

---

### kubelet

**Matlab:** Har Node par agent jo Pods run karta hai, Node status report karta hai.

**CAPI context:** Bootstrap + infra milkar Node tak **pahunchate** hain; kubelet tab tak “hero” hai workload cluster mein.

---

### CNI / CSI / CRI (short)

**Matlab:** Networking / storage / container runtime interfaces—pluggable ecosystem.

**Hinglish:** *“Kubernetes ke plug points”—alag vendors apna solution laga sakte hain.*

**CAPI:** Cluster `clusterNetwork` portable fields; actual CNI install often **add-ons** / GitOps se.

---

### Management cluster vs workload cluster

**Management:** Jahan **CAPI + providers** chal rahe hain aur CRs live hain.

**Workload:** Jahan **apps** chalte hain—tumhara “customer” cluster.

**Hinglish:** *Remote control wala room vs actual stage jahan play ho raha hai.*

---

### Provider (Core / Infra / Bootstrap / Control plane)

**Core:** Portable orchestration (`Cluster`, `Machine`, …).

**Infrastructure:** VM/network/LB **banata** hai.

**Bootstrap:** Pehli boot user-data / kubeadm **data** banata hai.

**Control plane:** HA control plane Machines **rollout/scale** karta hai (e.g. KCP).

**Hinglish:** *Ek hi play ke alag departments—ek dusre ke bina show adhoora.*

---

### clusterctl

**Matlab:** CLI jo management cluster setup, provider versions, templates, kubeconfig helpers deta hai.

**Hinglish:** *“CAPI ka project manager CLI”.*

---

### Kubebuilder / controller-gen / markers

**Matlab:** Go types par comments (`+kubebuilder:...`) se **CRD, deepcopy, RBAC** generate karna.

**Hinglish:** *“Types se boilerplate kam”—human error kam, drift kam.*

---

### envtest

**Matlab:** Tests ke liye local **real apiserver + etcd** binaries (poora cluster nahi).

**Hinglish:** *“Simulator cockpit”—cheap integration tests.*

---

### E2E (end-to-end)

**Matlab:** Poora flow—management cluster, providers, `clusterctl`, real-ish journey.

**Hinglish:** *Dress rehearsal—mehenga par confidence zyada.*

---

### Feature gate

**Matlab:** Experimental behavior **flag** se on/off—graduation path Kubernetes style.

---

### CAEP vs KEP

**KEP:** Core **kubernetes/kubernetes** enhancements process.

**CAEP:** **Cluster API** repo ke design proposals.

**Hinglish:** *Dono “RFC” jaisa—bas jurisdiction alag hai.*

---

### kubernetes-sigs

**Matlab:** Kubernetes **Special Interest Groups** ke under **SIG-hosted** repos—community maintained, CNCF/K8s ecosystem ke rules (CLA, review, release).

**Hinglish:** *“Official family ke paas wale cousins”—core repo se alag repo, par same governance culture.*

---

## 2. Ye sab milkar kaise chalta hai? (flow, Hinglish)

**Step-by-step story:**

1. Tum **management cluster** pe CRDs install karte ho (core + providers). *Matlab API server ko naye “forms” mil gaye.*

2. Tum **`Cluster` / `Machine` / KCP / KubeadmConfig / InfraMachine`** apply karte ho—ye **etcd** mein store hota hai. *Desired state lock ho gayi.*

3. **Controllers** (operators) watch karke **reconcile** karte hain:

   - Infra controller: **VM/container** banata hai.
   - Bootstrap controller: **cloud-init/Ignition + kubeadm** data banata hai.
   - Machine controller: **ordering** / conditions / node ref.
   - Cluster controller: **topology**, pause, child coordination.
   - KCP: **control plane replicas + rollout**.

4. **Webhooks** beech mein **validate/default** karte hain—kharab spec andar na jaaye.

5. **RBAC** har controller ko **sirf required powers** deta hai—zyada permission = zyada risk.

6. **Finalizers** delete par **cleanup** ensure karte hain—cloud orphan resources kam.

**Ek line mein:** *YAML desired state hai, etcd usko rakhta hai, controllers + webhooks milkar real duniya ko uske paas laate hain, RBAC risk kam karta hai.*

---

## 3. Kubernetes “core” vs Cluster API — rishta kya hai?

| Idea | Core Kubernetes | Cluster API |
|------|------------------|-------------|
| Unit of work | Pod, Deployment, Service | Machine, Cluster, MachineDeployment |
| Kya manage karte ho? | Apps **inside** a cluster | **Khud clusters** (lifecycle) |
| Infra | Scheduler assumes Nodes exist | **Providers** Nodes banate hain |
| Pattern | Controllers + API | Same pattern, higher layer |

**Hinglish:** *Kubernetes ne “andar” ka orchestra banaya; CAPI ne “cluster khud banana” ka orchestra banaya—dono same instrument family (API + controllers) bajate hain, bas scale alag hai.*

---

## 4. kubernetes-sigs/cluster-api kyun important hai?

- **Extensibility:** Alag cloud, alag bootstrap, alag control plane—**contracts** se juda ecosystem.
- **Real-world operator design:** Conditions, finalizers, pause, versioning—**production patterns**.
- **Community governance:** Reviews, CAEPs, compatibility—**large OSS discipline**.

**Hinglish:** *Sirf tool nahi hai—yeh “seekhne layak architecture museum” bhi hai.*

---

## 5. Agla kya padhna hai?

- Is chapter ka sequence: [Overview](./overview.md) → [01 — Kubernetes primer](./01-kubernetes-primer.md) → baaki numbered pages.
- User-facing concepts: [Concepts](https://cluster-api.sigs.k8s.io/user/concepts.html)
- Pehla contributor workflow: [First contributor guide](../first-contributor-guide.md)

---

*Yaad rakho: English terms exam / interview / codebase mein wahi rahenge; Hinglish tumhe **jaldi map** karne mein madad karta hai—dono saath chalao.*
