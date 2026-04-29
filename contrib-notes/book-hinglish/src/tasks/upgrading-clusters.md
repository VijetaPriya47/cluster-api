# Upgrading management and workload clusters — Simple Hinglish

> **Note:** Is page ka goal “upgrade mindset + flow” samjhana hai. Exact steps/commands provider-specific hote hain—English source follow karo.

## Official source

- Repo: [`docs/book/src/tasks/upgrading-clusters.md`](../../../../../docs/book/src/tasks/upgrading-clusters.md)
- Web: [Upgrading management and workload clusters](https://cluster-api.sigs.k8s.io/tasks/upgrading-clusters.html)

## Upgrade ka basic mental model

Do alag cheeze upgrade hoti hain:

1. **Management cluster components** (CAPI core + providers)
2. **Workload cluster** itself (Kubernetes version, machine images, etc.)

Common mistake: pehle workload cluster upgrade karna, jab management side components mismatch ho—isse reconciliation issues aa sakte hain.

## Considerations (high level)

### Supported Kubernetes versions

Har provider + CAPI version ka Kubernetes version support matrix hota hai.

Upgrade plan banate time ensure karo:

- current -> target versions supported hain
- control plane + workers ki upgrade sequence sane hai

### Images

“Kubernetes version bump” aur “underlying machine image bump” alag cheeze hain:

- image upgrade = OS/AMI/base-image change
- k8s upgrade = kubeadm/kubelet/k8s binaries version change

Dono ko mix karna possible hai, but troubleshoot hard ho jata hai—normally ek change at a time safe.

## Upgrading using Cluster API (how it happens)

Cluster API controllers upgrade ko rolling workflows se drive karte hain:

- Control plane upgrades (KCP / provider control-plane object)
- Workers upgrades (MachineDeployment/MachineSet rollout)

### Control plane machines upgrade

Typically:

- desired version/image update
- provider rolls control-plane machines (one-by-one) to maintain quorum

### Scheduling a machine rollout

Rollout triggers:

- template change
- version/image change
- rolloutAfter type controls (provider support)

### Machines managed by MachineDeployment

MachineDeployment controller:

- new MachineSet create karta hai
- replicas gradually shift karta hai (strategy dependent)

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
