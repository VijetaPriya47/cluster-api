# `ClusterResourceSet` Controller — Simple Hinglish

> **Note:** English source me exact fields/YAML mil jayega.

## ClusterResourceSet ka main kaam

`ClusterResourceSet` ek “template-to-multiple-clusters” concept hai:

- Aap ek `ClusterResourceSet` define karte ho
- Usme selector hota hai (kaun se `Cluster` match karein)
- Phir controller selected clusters ke liye add-on resources apply karta hai
  - usually `ConfigMap`/`Secret` ke data ke basis par

Result: selected workload clusters me add-on resources automatically ban/updated rehte hain.

## SetupWithManager: controller kya watch karta hai?

- `ClusterResourceSet` objects
- `Cluster` (selector matching ke liye)
- `ConfigMap` metadata/resources create/update
- `Secret` partial metadata (taaki secret changes par re-trigger ho)

## Reconcile (waterfall) — simple flow

1. `ClusterResourceSet` fetch
2. finalizer ensure
3. patch helper + paused check
4. `getClustersByClusterResourceSetSelector(...)` se matching clusters nikaalna
5. Deletion case:
   - `reconcileDelete(...)`:
     - har matching cluster ke corresponding `ClusterResourceSetBinding` se CRS remove
6. Normal case:
   - har matching cluster pe `ApplyClusterResourceSet(...)`
7. end me patch conditions/status (ResourcesApplied ...)

## Major functions (code me)

- `getClustersByClusterResourceSetSelector`
- `ApplyClusterResourceSet`
- `reconcileDelete`
- `getResource`
- `ensureResourceOwnerRef`
- `clusterToClusterResourceSet` (mapping for watches)

## Dusre cheezo se relation

- `ClusterResourceSet` -> `ClusterResourceSetBinding`:
  - binding yeh track karta hai ki kaunsa CRS ka resource set kaunsa Cluster par apply hua hai

