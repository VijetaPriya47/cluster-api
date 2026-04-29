# API Reference — hindii vyaakhyaa

> **nota:** yaha peja aadhikaarika pustaka kaa **hindii saara** hai. kamaanda, poorna YAML aura truti sandesha angrejaii moola men dekhen.

## aadhikaarika srota

- ripojaitarii: [`docs/book/src/reference/api/crd-api-reference-v1beta1.md`](../../../../../../docs/book/src/reference/api/crd-api-reference-v1beta1.md)
- veba (angrejaii): [API Reference](https://cluster-api.sigs.k8s.io/reference/api/crd-api-reference-v1beta1.html)

## yaha phaaaila kyaa hai?

yaha **svachaalita roopa se banii API sandarbha pustikaa** hai. isamen hara Custom Resource ke phaiilda, prakaara aura maanyataa taalikaaon men hain—angrejaii men. hindii nota kaa uddeshya: **kahaan dekhen** aura **kauna-se API samooha maayane rakhate hain**.

### mukhya `apiVersion` samooha (sankshepa)

- `addons.cluster.x-k8s.io/v1beta1`
- `bootstrap.cluster.x-k8s.io/v1beta1`
- `cluster.x-k8s.io/v1beta1`
- `controlplane.cluster.x-k8s.io/v1beta1`
- `ipam.cluster.x-k8s.io/v1alpha1`
- `ipam.cluster.x-k8s.io/v1beta1`
- `runtime.cluster.x-k8s.io/v1alpha1`

### kaise padhaen

1. apane kaama kaa **Kind** (jaise `Cluster`, `Machine`) dhoondhen.
2. `spec` aura `status` alaga—eka ichchhita sthiti, doosaraa vaastavika.
3. `metadata.ownerReferences` se dekhen kisa pairenta CR ne ise banaayaa.

---

*yaha saara `contrib-notes/book-hinglish` men hai.*
