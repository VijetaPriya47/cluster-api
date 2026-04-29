# 02 — How to read Cluster API Go code

Cluster API is mostly **Go** plus **generated YAML**. This page maps file types to responsibilities and shows two canonical snippets.

> **Hinglish:** *Socho: `api/` mein “form ka design” hai (spec/status), `internal/controllers/` mein “form process karne wala office” hai, aur `config/` mein “install karne wala printed manual” (CRD/RBAC YAML). Finalizer = “delete se pehle cleanup complete karo” wala checkpoint.*

## File types in the repo

| Location | Role |
|----------|------|
| `api/**/**_types.go` | Structs for `spec` and `status`; kubebuilder markers drive CRDs and validation. |
| `internal/controllers/**` | Private reconciliation logic (the “how”). |
| `controllers/**` (e.g. `alias.go`) | Thin **public** wrappers so other projects can embed reconcilers. |
| `config/**` | Kustomize + generated CRD YAML under `crd/bases/`. |
| `webhooks/**`, `internal/webhooks/**` | Admission hooks; markers point generator at them. |

## Snippet 1: finalizer constant on `Cluster`

A **finalizer** is a string in `metadata.finalizers`. While it is present, Kubernetes **will not fully delete** the object. The controller removes the finalizer after cleanup (orphan children, tear down cloud resources, etc.).

```34:41:api/core/v1beta2/cluster_types.go
const (
	// ClusterFinalizer is the finalizer used by the cluster controller to
	// cleanup the cluster resources when a Cluster is being deleted.
	ClusterFinalizer = "cluster.cluster.x-k8s.io"

	// ClusterKind represents the Kind of Cluster.
	ClusterKind = "Cluster"
)
```

- **`ClusterFinalizer`**: Domain-qualified name avoids clashes with other controllers’ finalizers.
- **`ClusterKind`**: Convenience constant for logs, tests, and generic code that needs the Kind string.

## Snippet 2: `Cluster` object shape (`spec` / `status`)

Every Kubernetes resource embeds **TypeMeta** (apiVersion/kind), **ObjectMeta** (name/namespace/labels), then **Spec** (desired) and **Status** (observed).

```1655:1668:api/core/v1beta2/cluster_types.go
type Cluster struct {
	metav1.TypeMeta `json:",inline"`
	// metadata is the standard object's metadata.
	// More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
	// +optional
	metav1.ObjectMeta `json:"metadata,omitempty"`

	// spec is the desired state of Cluster.
	// +required
	Spec ClusterSpec `json:"spec,omitempty,omitzero"`
	// status is the observed state of Cluster.
	// +optional
	Status ClusterStatus `json:"status,omitempty,omitzero"`
}
```

- **`Spec`**: What the user (or GitOps) asked for—**only this** should be edited by normal clients; controllers should not “fight” users by rewriting spec without a webhook/defaulting rule.
- **`Status`**: What controllers report back—conditions, phase, derived fields. Updated via the **status subresource** in well-behaved controllers.

Methods like `GetConditions` / `SetConditions` implement shared interfaces so generic libraries can treat many CAPI types uniformly:

```1699:1707:api/core/v1beta2/cluster_types.go
// GetConditions returns the set of conditions for this object.
func (c *Cluster) GetConditions() []metav1.Condition {
	return c.Status.Conditions
}

// SetConditions sets conditions for an API object.
func (c *Cluster) SetConditions(conditions []metav1.Condition) {
	c.Status.Conditions = conditions
}
```

## Snippet 3: RBAC markers on the cluster reconciler

Comments starting with `+kubebuilder:rbac:` are **not** ignored—they are consumed by **controller-gen** to emit RBAC rules into `config/rbac/*.yaml`.

```67:79:internal/controllers/cluster/cluster_controller.go
// Update permissions on /finalizers subresrouce is required on management clusters with 'OwnerReferencesPermissionEnforcement' plugin enabled.
// See: https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#ownerreferencespermissionenforcement
//
// +kubebuilder:rbac:groups=core,resources=events,verbs=create;patch
// +kubebuilder:rbac:groups=core,resources=secrets,verbs=get;list;watch;create;patch;update
// +kubebuilder:rbac:groups=infrastructure.cluster.x-k8s.io;bootstrap.cluster.x-k8s.io;controlplane.cluster.x-k8s.io,resources=*,verbs=get;list;watch;create;update;patch;delete
// +kubebuilder:rbac:groups=cluster.x-k8s.io,resources=clusters;clusters/status;clusters/finalizers,verbs=get;list;watch;update;patch
// +kubebuilder:rbac:groups=apiextensions.k8s.io,resources=customresourcedefinitions,verbs=get;list;watch

// Reconciler reconciles a Cluster object.
type Reconciler struct {
	Client       client.Client
	APIReader    client.Reader
	ClusterCache clustercache.ClusterCache
```

**Line-by-line meaning:**

- **Events `create;patch`**: Emit Kubernetes **Events** so `kubectl describe cluster` shows human-readable progress.
- **Secrets**: Cluster reconciler may read/write Secrets (kubeconfig material, tokens)—narrow verbs are better than `*`.
- **Provider groups** (`infrastructure.*`, `bootstrap.*`, `controlplane.*`): Core orchestrates **referenced** objects owned by other providers.
- **`clusters/finalizers`**: Needed when the API server enforces that only controllers with update permission on finalizers may set owner references with blocking behavior.
- **CRDs `get;list;watch`**: Sometimes needed for discovery or migration helpers—not full admin.

**`Reconciler` fields:**

- **`Client`**: Cached read/write client (fast, may be slightly stale).
- **`APIReader`**: Uncached reads when you must see etcd-consistent state.
- **`ClusterCache`**: Connection to **remote** workload clusters for status without merging their data into the management informer by accident.

> **Hinglish:** *RBAC wale comments ignore nahi hote—unse Makefile/`controller-gen` security rules banata hai. `Client` thoda cache se padh sakta hai (fast), `APIReader` “seedha etcd jaisa fresh” read; remote cluster ka data alag cache se aata hai taaki mix-up na ho.*

**Next:** [api/core](./03-api-core.md).
