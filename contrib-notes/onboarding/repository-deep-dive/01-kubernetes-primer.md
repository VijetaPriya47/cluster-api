# 01 — Kubernetes in 60 seconds

This page assumes you might **not** know Kubernetes yet. Everything here is background for reading Cluster API.

> **Hinglish:** *Agar tum Kubernetes newbie ho, tension mat lo—yeh page sirf itna kehta hai: API server “sach ka register” hai, controllers usko real duniya se milaate hain. CAPI bas isi idea ko clusters par laga deta hai.*

## What is Kubernetes?

**Kubernetes (K8s)** is a system that runs **containers** (usually Docker/OCI images) across many machines. It gives you one **control plane** (API + controllers) and many **worker** nodes that run your workloads.

**Real-world analogy:** Instead of SSH-ing into 50 servers and starting processes by hand, you submit a **declaration** (“run 10 copies of this app, spread them out, restart if unhealthy”) and the system keeps trying to make that true.

## API server and etcd

- The **kube-apiserver** is the front door. All state (Pods, ConfigMaps, your CRs) is stored in **etcd** (a distributed key-value store).
- You normally interact via **kubectl** and YAML manifests.

**Takeaway for CAPI:** Cluster API adds **new kinds** of objects (`Cluster`, `Machine`, …) to that same API server on the **management cluster**.

## Pods and workloads

- A **Pod** is the smallest deployable unit—often one main container plus sidecars.
- A **Deployment** owns a set of Pods and performs rolling updates when you change the Pod template.

**Takeaway for CAPI:** A **Machine** is not a Pod—it represents a **host** (VM or metal) that will run a **Kubernetes Node**. But the *reconciliation idea* (desired count, rollouts) is similar in spirit to Deployments.

## Custom Resources (CRs) and CRDs

- A **CustomResourceDefinition (CRD)** teaches the API server a new `kind` and `apiVersion`.
- After a CRD is installed, you can `kubectl apply` YAML with that `apiVersion`/`kind`.

**Takeaway for CAPI:** `Cluster` and `Machine` are **CRs**. Their schemas are generated from Go types under `api/`.

## Controllers and operators

- A **controller** is a loop: watch objects, compare desired vs actual state, take action, repeat.
- An **operator** usually means: controllers + often **admission webhooks** + RBAC, packaged as software you install on the cluster.

**Takeaway for CAPI:** The `cluster-api-controller-manager` is an operator for cluster lifecycle. Provider operators (AWS, Azure, Docker, …) extend it.

## Management cluster vs workload cluster (preview)

- **Management cluster:** Where CAPI controllers run and where `Cluster`/`Machine` objects live.
- **Workload cluster:** The cluster you are creating for apps.

> **Hinglish:** *Management cluster = jahan CAPI controllers *baith ke* clusters banate hain; workload cluster = jahan tumhara app chalega. Dono confuse mat karna—warna `kubectl delete` galat cluster pe chal sakta hai.*

**Next:** [How to read CAPI Go code](./02-reading-go-code.md).
