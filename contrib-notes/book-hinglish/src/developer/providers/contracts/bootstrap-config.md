# Contract rules for BootstrapConfig — Simple Hinglish

> **Note:** Ye page “BootstrapConfig provider contract” ka simple mental model deta hai. Exact fields/rules ke liye English source follow karo.

## Official source

- Repo: [`docs/book/src/developer/providers/contracts/bootstrap-config.md`](../../../../../../../docs/book/src/developer/providers/contracts/bootstrap-config.md)
- Web: [Contract rules for BootstrapConfig](https://cluster-api.sigs.k8s.io/developer/providers/contracts/bootstrap-config.html)

## BootstrapConfig provider ka role

Bootstrap provider ka kaam: Machine ko “first boot” pe Kubernetes node banane ke liye required **bootstrap data** (usually cloud-init / ignition / scripts) generate karna.

Core side (CAPI `Machine` controller) ko mostly yeh chahiye:

- BootstrapConfig ready ho
- bootstrap “data secret” produce ho
- conditions/status se clear signal mile ki data ready hai ya failure hua

## Contract rules ka simple map (v1beta2 mindset)

### 1) Common rules (all resources)

BootstrapConfig/BootstrapConfigTemplate me:

- correct `TypeMeta`/`ObjectMeta`
- correct API group + version
- predictable scope conventions follow

### 2) BootstrapConfig: data secret (most important)

BootstrapConfig provider usually ek **Secret reference** set karta hai jisme actual bootstrap data hota hai.

Machine controller phir:

- us secret ko read karke infra provider ko pass karta hai (so VM/instance user-data me inject ho sake)

### 3) Initialization completed

BootstrapConfig status me ye signal hota hai ki:

- initial bootstrap data generate/consumed stage complete ho gaya

### 4) Conditions + terminal failures

Contract me yeh important hai:

- conditions consistent hon (Ready/error)
- “terminal failure” clearly indicate kare (non-retriable), taaki core infinite retries na kare

### 5) In-place changes support

Kuch providers allow karte hain ki bootstrap config me changes in-place handle ho (without full machine replace).
Contract is capability ko define/limit karta hai.

### 6) BootstrapConfigTemplate + SSA dry-run

ClusterClass/topology workflows me templates use hote hain:

- template = “blueprint” for many Machines
- SSA dry-run support ka matlab: server-side apply dry-run se validate/preview possible ho

### 7) Sentinel file & taints (node behavior)

Contract me kuch “behavior” conventions aati hain, jaise:

- sentinel file: node pe ek marker file to indicate bootstrap already applied (double-run avoid)
- node taints at creation: bootstrap time pe taint set karke scheduling control

### 8) Multiple instances + clusterctl support + pausing

- multiple provider instances: labels/namespaces se identify & isolate
- clusterctl support: provider repository layout/components/templates expectations match
- pausing: paused object reconcile nahi hota (consistent semantics)

## Typical BootstrapConfig reconciliation workflow (high-level)

1. `Machine` has a `spec.bootstrap.configRef`
2. Bootstrap provider sees BootstrapConfig, generates bootstrap data
3. Provider sets `status.dataSecretName` (or equivalent reference) + conditions
4. Machine controller consumes the secret and proceeds with infra provisioning + node joining

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
