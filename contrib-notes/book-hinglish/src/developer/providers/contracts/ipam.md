# IPAM Provider Specification — Simple Hinglish

> **Note:** Ye page IPAM (IP Address Management) provider contract/spec ka simple mental model deta hai. Exact types/fields ke liye English source follow karo.

## Official source

- Repo: [`docs/book/src/developer/providers/contracts/ipam.md`](../../../../../../../docs/book/src/developer/providers/contracts/ipam.md)
- Web: [IPAM Provider Specification](https://cluster-api.sigs.k8s.io/developer/providers/contracts/ipam.html)

## IPAM ka role (simple)

IPAM provider ka kaam:

- IP addresses allocate/release karna
- “claim” based workflow provide karna, taaki infra provider/machine provisioning me deterministic IP assignment ho

## Core concepts (high level)

Spec me generally do main resources hote hain:

- `IPAddressClaim`: “mujhe ek IP chahiye” request/claim
- `IPAddress`: allocated IP (actual assignment record)

Infra providers / controllers IPAM ko use karke:

- Machine/LoadBalancer/ControlPlane endpoints ke liye IP reserve kar sakte hain

## Behaviour (simple waterfall)

### IPAM Provider side

#### Normal `IPAddressClaim`

1. Claim create hota hai
2. IPAM provider suitable IP choose/allocate karta hai
3. Provider claim ko bind karta hai (usually by creating/updating corresponding `IPAddress`)
4. status/conditions update hoti hain so users/controllers know “allocated/failed”

#### Deleted `IPAddressClaim`

1. Claim delete hota hai
2. IPAM provider allocation release karta hai
3. related `IPAddress` cleanup/mark release hota hai (provider rules ke hisaab se)

#### `clusterctl move` considerations

Move ke time owner refs/labels/relationships consistent hone chahiye, taaki IP claims/allocations correctly transfer ho saken (double-allocate na ho).

### Infrastructure Provider side

Infra providers IPAM ko integrate karte hain:

- instance/endpoint provisioning se pehle claim create karke
- allocated IP ko apne resources me set karke

## Why this contract matters

Without a predictable IPAM contract:

- duplicate allocations
- leaked IPs
- inconsistent “ready” signals

ho sakte hain, jo cluster bring-up/upgrade/move ko break kar dete hain.

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
