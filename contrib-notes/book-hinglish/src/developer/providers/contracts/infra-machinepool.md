# Contract rules for InfraMachinePool — Simple Hinglish

> **Note:** Ye page “Infrastructure MachinePool provider contract” ka simple mental model deta hai. Exact fields/rules ke liye English source follow karo.

## Official source

- Repo: [`docs/book/src/developer/providers/contracts/infra-machinepool.md`](../../../../../../../docs/book/src/developer/providers/contracts/infra-machinepool.md)
- Web: [Contract rules for InfraMachinePool](https://cluster-api.sigs.k8s.io/developer/providers/contracts/infra-machinepool.html)

## InfraMachinePool provider ka role

InfraMachinePool provider ka kaam: “managed node pool” style resource manage karna.

Example (provider-specific):

- cloud managed node pools (EKS/GKE/AKS style)
- ya provider ka own “pool” abstraction

Core side (CAPI `MachinePool` controller) ko mainly chahiye:

- desired replicas ko actual pool size se align karna
- pool ke instances / providerIDs track karna
- conditions + terminal failures se clear status

## Contract rules ka simple map (v1beta2 mindset)

### 1) Common rules (all resources)

InfraMachinePool/InfraMachinePoolTemplate me:

- correct `TypeMeta`/`ObjectMeta`
- correct API group + version
- predictable scope conventions follow

### 2) Instances + MachinePoolMachines support

InfraMachinePool status me instances list / machine references provide ki ja sakti hain, taaki:

- MachinePool controller nodes tracking (NodeRefs, UpToDate) support kare

### 3) providerID + providerIDList

Pools me ek single providerID ya list of providerIDs aati hai:

- stable identity milti hai (debug, delete, drain style operations)

### 4) Replicas

Contract me define hota hai:

- desired replicas ka signal
- aur status me actual replicas / size reporting

### 5) Initialization completed

Signal that:

- pool initial provisioning ready state me aa gaya

### 6) Conditions + terminal failures + pausing

- consistent conditions (Ready/error)
- terminal failure explicitly mark (non-retriable)
- pausing: paused objects reconcile nahi hote

### 7) Templates + SSA dry-run

ClusterClass/topology me templates use hote hain:

- template = blueprint for pools
- SSA dry-run support = validate/preview possible

### 8) Multi-tenancy + clusterctl support

- multi tenancy: isolation + identity conventions
- clusterctl support: provider repo components/templates expectations match

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
