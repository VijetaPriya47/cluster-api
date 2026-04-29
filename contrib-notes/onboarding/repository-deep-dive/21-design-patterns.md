# 21 — Design patterns (quick map)

> **Hinglish:** *Ye table “interview prep + code read map” dono ke liye—har pattern ke liye repo mein seedha example mil jata hai.*

| Pattern | Example in CAPI |
|--------|------------------|
| **Reconciler loop** | `Reconcile` methods in `internal/controllers/**` |
| **Finalizer** | `ClusterFinalizer`, `KubeadmControlPlaneFinalizer` |
| **Owner references** | `GetOwnerCluster`, child objects owned by Machine/Cluster |
| **Conditions** | `GetConditions` / `SetConditions`; aggregated Available signals |
| **Admission webhooks** | Generated under `config/webhook`; implementations in `webhooks/` |
| **Codegen / markers** | `+kubebuilder` validation and RBAC markers |
| **Facade CLI** | `clusterctl` over raw YAML assembly |
| **Adapter / embedding** | `controllers.ClusterReconciler` → `internal` reconciler |

**Next:** [DevOps practice](./22-devops-practice.md).
