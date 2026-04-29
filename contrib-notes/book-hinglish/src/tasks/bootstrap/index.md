# Bootstrap — Simple Hinglish

Bootstrap ka matlab: Machine ko “pehli baar” boot hote hi Kubernetes node banane ke steps provide karna.

Yeh usually bootstrap provider karta hai (e.g. kubeadm bootstrap, microk8s bootstrap), jo cloud-init/ignition scripts generate karke secret me store karta hai.

## Official source

- Repo: [`docs/book/src/tasks/bootstrap/index.md`](../../../../../../docs/book/src/tasks/bootstrap/index.md)
- Web: [Bootstrap](https://cluster-api.sigs.k8s.io/tasks/bootstrap/index.html)

## Is section me kya milega?

- kubeadm bootstrap related how-tos
- kubelet config tuning
- alternate bootstraps (microk8s, etc.)

## Core controllers se relation (simple)

1. `Machine.spec.bootstrap.configRef` bootstrap object ko point karta hai
2. bootstrap provider `status.dataSecretName` set karta hai
3. Machine controller us secret ko infra provider ke saath combine karke instance create/boot karwata hai

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
