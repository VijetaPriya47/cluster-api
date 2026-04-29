# Control Plane Management — Simple Hinglish

Control plane management ka matlab: workload cluster ka API server + etcd + control-plane machines lifecycle manage karna.

Ye normally control-plane provider (e.g. KubeadmControlPlane / MicroK8sControlPlane) handle karta hai.

## Official source

- Repo: [`docs/book/src/tasks/control-plane/index.md`](../../../../../../docs/book/src/tasks/control-plane/index.md)
- Web: [Control Plane Management](https://cluster-api.sigs.k8s.io/tasks/control-plane/index.html)

## Is section me kya milega?

- kubeadm control plane related how-tos (upgrade/rollout/rotation)
- microk8s control plane

## Core controllers se relation (simple)

1. `Cluster.spec.controlPlaneRef` control-plane object ko point karta hai
2. control-plane provider machines create/update karta hai
3. endpoint + conditions/status publish hoti hai
4. Cluster controller kubeconfig, descendants, rollout workflows drive karta hai

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
