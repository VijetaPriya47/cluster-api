# 19 — Architecture guarantees

This page summarizes **intentional** properties of Cluster API’s architecture—things the code and APIs are **designed** to preserve.

> **Hinglish:** *Ye points “accidental” nahi hain—maintainers ne jaan-bujh ke boundaries banayi hain taaki providers alag ho saken aur core stable rahe.*

1. **Portability at the core**  
   `Cluster` and `Machine` avoid cloud-specific fields; **`infrastructureRef`**, **`bootstrap.configRef`**, and **`controlPlaneRef`** compose provider CRs.

2. **Composable providers**  
   Bootstrap, control plane, and infrastructure implementations **swap** as long as they honor contracts—enables a **CAP\* ecosystem**.

3. **Declarative reconciliation**  
   Controllers are **level-triggered**: missed events don’t permanently break state; periodic resync and dependency watches recover.

4. **Machine immutability**  
   Most spec changes roll out by **replacing** Machines—reduces undefined partial states on nodes.

5. **Internal vs public Go surface**  
   `internal/controllers` can evolve; `controllers` aliases expose a **narrow embedding API**.

6. **Versioned APIs**  
   Multiple `apiVersion` folders + conversion machinery support **gradual migration**.

**Next:** [Security design](./20-security.md).
