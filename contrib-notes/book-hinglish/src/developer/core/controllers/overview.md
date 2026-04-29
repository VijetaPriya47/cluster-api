# Controllers (Core) — Simple Hinglish

> **Note:** Yahan “simple/Hinglish” explanation hai. Commands, full YAML, aur exact error messages ke liye official English page dekhna best rahega.

## Official source

- Repo: [`docs/book/src/developer/core/controllers/overview.md`](../../../../../../../docs/book/src/developer/core/controllers/overview.md)
- Web: [Controllers](https://cluster-api.sigs.k8s.io/developer/core/controllers/overview.html)

## Cluster API ke “controllers” ka idea

Cluster API me controllers = Kubernetes me chalne wale controllers/reconcilers. Inka kaam hota hai:

1. Koi resource change hota hai (jaise `Cluster`, `Machine`, `MachineSet`, …)
2. Controller usko “read” karta hai
3. Phir decide karta hai ki next step kya hona chahiye
4. Status/conditions aur required child objects ko create/update/patch karta hai
5. Deletion case me dependent cheezein clean karta hai (finalizers ki help se)

## Core ka “overall wiring” (waterfall) — code ka flow

Core Cluster API manager ka entrypoint root `main.go` hai. Usme:

- `setupReconcilers()`:
  - `ClusterCache` setup karta hai (workload cluster se probing/health read karne ke liye)
  - CRD migration (`CRDMigrator`) setup karta hai
  - Feature gates ke hisaab se controllers ko `SetupWithManager(...)` se register karta hai
  - RuntimeSDK enabled ho to RuntimeClient setup karta hai
- `setupWebhooks()`:
  - Admission webhooks register karta hai (Cluster/Machine/… par create/update ko guard + validate/default karne ke liye)

### Core controllers (is book page set me)

Yahan `developer/core/controllers/` ke andar jo pages hain (book structure ke hisaab se):

- `Cluster` controller
- `Machine` controller
- `MachineSet` controller
- `MachineDeployment` controller
- `MachinePool` controller
- `MachineHealthCheck` controller
- `ClusterResourceSet` controller
- `ClusterTopology` controller (managed topology / blueprint orchestration)

## Controllers aapas me kaise jude hain (mental model)

Simple chain:

- `Cluster` controller: “infra + control-plane + kubeconfig + descendants” orchestration karta hai
- `Machine` controller: har `Machine` ka bootstrap/infra + node lifecycle (provisioning/deletion) handle karta hai
- `MachineSet` controller: “replicas” + templates se `Machine` objects ko sync/adopt karta hai
- `MachineDeployment` controller: rollout strategy ke basis par `MachineSets` ka desired state plan + apply karta hai
- `MachinePool` controller: `MachineSet` jaisa but “pool” aur `nodeRefs` oriented behavior
- `MachineHealthCheck` controller: unhealthy machines ko detect karke remediation flow trigger karta hai
- `ClusterResourceSet` controller: selector se clusters choose karke add-on resources (ConfigMaps/Secrets) apply karta hai
- `ClusterTopology` controller: jab managed topology use ho, to Blueprint + desired-state generation + reconcile-state orchestration karta hai

