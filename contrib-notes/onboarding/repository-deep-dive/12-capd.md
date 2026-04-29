# 12 — CAPD: Docker infrastructure provider (`test/infrastructure/docker/`)

**Cluster API Provider Docker (CAPD)** implements the **infrastructure provider contract** using Linux containers as stand-ins for VMs. It is for **development**, **CI**, and learning—not production workloads.

> **Hinglish:** *CAPD = “cheap practice ground”—asli production cloud nahi. Laptop pe kind+CAPD se flow samajh sakte ho; par boss ko keh dena prod mein CAPA/CAPZ wagairah.*

## `DockerMachine` type

```161:170:test/infrastructure/docker/api/v1beta2/dockermachine_types.go
// DockerMachine is the Schema for the dockermachines API.
//
// Deprecated: DockerMachine is deprecated. Use DevMachine instead.
type DockerMachine struct {
	metav1.TypeMeta   `json:",inline"`
	metav1.ObjectMeta `json:"metadata,omitempty"`

	Spec   DockerMachineSpec   `json:"spec,omitempty"`
	Status DockerMachineStatus `json:"status,omitempty"`
}
```

**Reading the code:**

- **Same structural pattern** as core types: `TypeMeta`, `ObjectMeta`, `Spec`, `Status`.
- **Deprecation comment:** The project may introduce **`DevMachine`** as the next shape—when reading CAPD, check release notes for migration guidance.
- **`+kubebuilder:printcolumn` markers** (above this struct in the file) add **`kubectl get`** columns (Provisioned, IP, Paused, Age)—great UX for operators.

Condition helpers mirror core:

```191:199:test/infrastructure/docker/api/v1beta2/dockermachine_types.go
// GetConditions returns the set of conditions for this object.
func (c *DockerMachine) GetConditions() []metav1.Condition {
	return c.Status.Conditions
}

// SetConditions sets conditions for an API object.
func (c *DockerMachine) SetConditions(conditions []metav1.Condition) {
	c.Status.Conditions = conditions
}
```

**Why this matters:** Generic code (summary helpers, printers, tests) can treat CAPD machines like core resources via shared interfaces.

## Controllers in this module

Under `test/infrastructure/docker/` you will find controllers that:

1. Create/remove Docker containers representing Machines.
2. Plumb **bootstrap data** into them (like a cloud’s user-data path).
3. Report **addresses** and readiness into `status`.

**DevOps engineer:** Use CAPD with **kind** + **Tilt** to reproduce e2e failures locally without cloud spend.

> **Hinglish:** *Deprecation notice dhyan se—open source mein types kabhi replace ho jaate hain; upgrade guide release notes mein milega.*

**Next:** [`clusterctl`](./13-clusterctl.md).
