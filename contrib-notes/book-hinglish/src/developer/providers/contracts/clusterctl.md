# clusterctl Provider Contract (contract version v1beta2) — Simple Hinglish

> **Note:** Yahan goal “clusterctl provider repository contract” ka simple mental model dena hai. Exact schema/examples ke liye English source dekho.

## aadhikaarika srota

- ripojaitarii: [`docs/book/src/developer/providers/contracts/clusterctl.md`](../../../../../../../docs/book/src/developer/providers/contracts/clusterctl.md)
- veba (angrejaii): [clusterctl Provider Contract (contract version v1beta2)](https://cluster-api.sigs.k8s.io/developer/providers/contracts/clusterctl.html)

## Provider repository contract (simple mental model)

Clusterctl “provider repository” ko predictable layout + files ke through read karta hai, jisse ye cheeze possible hoti hain:

- `clusterctl init` -> provider **components** install
- `clusterctl generate cluster` -> workload cluster **templates** output
- `clusterctl upgrade` -> versions resolve + components update
- `clusterctl move` -> objects/dependencies move ke time expectations clear

### Provider repositories (source of truth)

Provider repository ka matlab: ek GitHub/GitLab/local location jahan provider publish karta hai:

- versions (releases/tags)
- metadata + components files
- workload cluster templates / ClusterClass definitions

### Metadata YAML (what clusterctl needs to know)

Metadata me usually declare hota hai:

- provider ka name/type + available versions
- files ka mapping (components/templates)
- validation rules (taaki wrong layout/inputs detect ho jaye)

### Components YAML (management cluster install)

Ye wo manifests hote hain jo management cluster me provider install karte hain:

- controllers/webhooks Deployments
- RBAC, CRDs (where applicable), etc.

Contract mindset:

- naming conventions consistent hon
- target namespace behavior predictable ho
- controllers ka watch scope/namespace model clear ho (all namespaces vs specific)

### Variables, labels, and naming (template processing)

Clusterctl templates ko process karta hai:

- variables substitution (config file / env vars)
- labels/annotations (ownership/management ke liye)

Goal: deterministic outputs, upgrades/move ke time matching easy ho.

### Workload cluster templates

Workload templates ka output:

- `Cluster`, `MachineDeployment`, `KubeadmControlPlane`, infra objects, etc. generate karne me use hota hai
- flavors/variants possible hote hain (provider specific)

### ClusterClass definitions (topology/managed clusters)

Provider agar ClusterClass-based management support karta hai to repo me ClusterClass + templates provide hote hain.

### OwnerReferences chain (garbage collection + move)

OwnerReferences chain important hai because:

- delete ke time Kubernetes garbage collection predictable rahe
- `clusterctl move` dependencies ko safely discover/transfer kar sake

### Transformations + links + move (high-level)

Clusterctl provider components/templates par transformations karta hai (variables, versions, flavors).

External objects (e.g. etcd) ke links/refs clear hone chahiye, warna move/upgrade flows break ho sakte hain.

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
