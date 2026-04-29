# Repository deep dive (overview)

This chapter walks through the **kubernetes-sigs/cluster-api** tree **one area at a time**. For **how code runs** in each major package, see the [contrib-notes code walkthroughs](../../INDEX.md). Each page includes **real code** from the repo and **line-by-line style explanations** for readers who are still learning Kubernetes and Go operators.

> **Hinglish:** *Is chapter ka idea simple hai—repo ka har folder alag page pe hai, aur saath mein actual Go/YAML code bhi explain kiya gaya hai. Pehle Kubernetes basics samajh lo, phir CAPI padhna easy lagega. Matlab, “kahan kya hai” aur “ye code kya keh raha hai” dono ek saath.*

**Start here if you are new:** optional full Hinglish pass—[00 — Hinglish glossary & big picture](./00-hinglish-glossary-and-big-picture.md). Then [Kubernetes in 60 seconds](./01-kubernetes-primer.md), [How to read CAPI Go code](./02-reading-go-code.md), then pick any folder below.

## Chapter map

| Page | What you learn |
|------|----------------|
| [00 — Hinglish glossary & big picture](./00-hinglish-glossary-and-big-picture.md) | Technical terms explained in Hinglish; how pieces fit; K8s vs CAPI; SIG context |
| [01 — Kubernetes primer](./01-kubernetes-primer.md) | Pods, API server, CRDs, controllers—minimum background for CAPI |
| [02 — Reading CAPI Go code](./02-reading-go-code.md) | Where `spec`/`status` live, finalizers, RBAC markers |
| [03 — `api/core`](./03-api-core.md) | `Cluster`, `Machine`, conditions, API conventions |
| [04 — Addons, IPAM, Runtime](./04-api-addons-ipam-runtime.md) | ClusterResourceSet, IPAM, ExtensionConfig |
| [05 — Bootstrap API (`kubeadm`)](./05-api-bootstrap-kubeadm.md) | `KubeadmConfigSpec`, cloud-config vs Ignition |
| [06 — Control plane API (`kubeadm`)](./06-api-controlplane-kubeadm.md) | `KubeadmControlPlane`, rollouts, finalizers |
| [07 — `config/` manifests](./07-config-manifests.md) | CRD kustomize, webhooks, how YAML is produced |
| [08 — `internal/controllers`](./08-internal-controllers.md) | Real `Reconcile` loops (Cluster controller) |
| [09 — Public `controllers` package](./09-controllers-public-alias.md) | Embedding: alias types and `SetupWithManager` |
| [10 — Bootstrap controllers](./10-bootstrap-controllers.md) | `KubeadmConfigReconciler` |
| [11 — Control plane controllers](./11-controlplane-controllers.md) | Kubeadm control plane reconciliation (overview) |
| [12 — CAPD (Docker provider)](./12-capd.md) | `DockerMachine` and dev infrastructure |
| [13 — `clusterctl`](./13-clusterctl.md) | CLI entrypoint and command package |
| [14 — `test/e2e`](./14-test-e2e.md) | Ginkgo suite, flags, bootstrap cluster |
| [15 — `test/framework`](./15-test-framework.md) | `E2EConfig` and shared test helpers |
| [16 — `internal/test/envtest`](./16-envtest.md) | Local test apiserver + scheme registration |
| [17 — Proposals (CAEPs)](./17-proposals.md) | Design docs folder |
| [18 — Developer book (`docs/book`)](./18-dev-book.md) | mdBook source |
| [19 — Architecture guarantees](./19-architecture.md) | Portability, immutability, versioning |
| [20 — Security design](./20-security.md) | RBAC, webhooks, secrets |
| [21 — Design patterns](./21-design-patterns.md) | Reconciler, facade, template, etc. |
| [22 — DevOps practice](./22-devops-practice.md) | Day-2 checklist |

## Case study (one paragraph)

**Without Cluster API**, clusters are often built with ad hoc scripts, Terraform, or cloud consoles—hard to treat as one declarative object inside Kubernetes.

**With Cluster API**, you run a **management cluster** where controllers watch CRs like `Cluster` and `Machine`, then talk to infrastructure and bootstrap providers until a **workload cluster** exists and stays healthy. Desired state lives in etcd as YAML resources; reconcilers close the gap between intent and reality—same idea as a Deployment reconciling Pods, but for whole clusters.

**Why read the code:** CAPI is a reference-quality example of multi-controller systems, API evolution, generated RBAC, and layered testing (envtest + e2e).

> **Hinglish:** *Bina CAPI ke cluster banana alag-alag tools se hota hai; CAPI ke saath wohi “desired state” Kubernetes ke andar CR ban jaati hai—controllers phir usko real VMs/nodes se match karte rehte hain. Code isliye padho kyunki yahan industry-grade operator design dikhta hai.*

## Related book pages

- [First contributor guide](../first-contributor-guide.md)
- [Repository layout](https://cluster-api.sigs.k8s.io/developer/core/repository-layout.html)
- [Concepts (users)](https://cluster-api.sigs.k8s.io/user/concepts.html)
