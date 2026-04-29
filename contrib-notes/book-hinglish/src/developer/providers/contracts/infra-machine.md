# Contract rules for InfraMachine — Simple Hinglish

> **Note:** Ye page “Infrastructure Machine provider contract” ka simple mental model deta hai. Exact fields/rules ke liye English source follow karo.

## Official source

- Repo: [`docs/book/src/developer/providers/contracts/infra-machine.md`](../../../../../../../docs/book/src/developer/providers/contracts/infra-machine.md)
- Web: [Contract rules for InfraMachine](https://cluster-api.sigs.k8s.io/developer/providers/contracts/infra-machine.html)

## InfraMachine provider ka role

InfraMachine provider ka kaam: ek Machine ke liye actual **compute instance/VM** (infra-side) create/manage karna.

Core side (CAPI `Machine` controller) ko yeh things chahiye:

- providerID (cloud provider identity)
- addresses (IP/DNS) so Node discovery/connection possible ho
- failureDomain placement info (zones/regions)
- conditions + ready/failure signals

## Contract rules ka simple map (v1beta2 mindset)

### 1) Common rules (all resources)

InfraMachine/InfraMachineTemplate me:

- correct `TypeMeta`/`ObjectMeta`
- correct API group + version
- predictable scope conventions follow

### 2) providerID (identity)

Infra provider ko `providerID` set karna hota hai, so:

- Node/Cloud integration possible ho
- CAPI core ko stable identity mile (delete/drain/etc. flows me help)

### 3) failure domain

Provider failureDomain publish karta hai:

- scheduling/HA decisions better ho
- control-plane/worker placement consistent rahe

### 4) addresses

InfraMachine status me addresses (internal/external IP/DNS) aati hain:

- Machine controller inko use karke NodeRef/connection flows assist karta hai

### 5) initialization completed

Signal that:

- initial infra provisioning step complete hai (provider-specific)

### 6) conditions + terminal failures

Contract ensure karta hai:

- consistent conditions (Ready/error)
- terminal failures explicitly mark, taaki core infinite retries na kare

### 7) in-place changes support

Kuch providers allow karte hain in-place updates (without full replace).
Contract me capability/scope clarify hota hai.

### 8) Templates + SSA dry-run

ClusterClass/topology workflows me templates use hote hain:

- template = blueprint for many machines
- SSA dry-run support = server-side apply dry-run se validate/preview possible

### 9) Autoscaling from zero + multi-tenancy + pausing

- autoscaling from zero: templates/fields aise hon ki scale-up from 0 possible ho
- multi-tenancy: isolation + identity conventions
- pausing: paused object reconcile nahi hota

## Typical InfraMachine reconciliation workflow (high-level)

### Normal

1. `Machine` has `spec.infrastructureRef`
2. Infra provider creates/updates VM/instance
3. Provider sets `providerID` + addresses + conditions
4. Core Machine controller continues with NodeRef, health, rollout, etc.

### Delete

1. Machine deletion starts
2. Infra provider deletes instance/VM
3. Final status/conditions reflect completion

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
