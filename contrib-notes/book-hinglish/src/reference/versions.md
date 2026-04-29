# Cluster API and Kubernetes version support — hindii vyaakhyaa

> **nota:** yaha peja aadhikaarika pustaka kaa **hindii saara** hai. kamaanda, poorna YAML aura truti sandesha angrejaii moola men dekhen.

## aadhikaarika srota

- ripojaitarii: [`docs/book/src/reference/versions.md`](../../../../../docs/book/src/reference/versions.md)
- veba (angrejaii): [Cluster API and Kubernetes version support](https://cluster-api.sigs.k8s.io/reference/versions.html)

## khanda-vaara saara (hindii)

### Version support policies

sanskarana samarthana aura maitriksa.

#### Cluster API release support

netavarka porta soochii.

##### Skip upgrades

sanskarana oopara uthaanaa—yojanaa aura laagoo karanaa.

##### Downgrades

**Downgrades**—isa upashiirshaka ke antargata moola peja men vistrita nirdesha, udaaharana yaa taalikaaen hain. satiika aadesha aura YAML ke lie oopara dii gaii angrejaii srota phaaaila kholen.

##### Cluster API release vs API versions

sahaayaka yaa atirikta upa-aadesha.

##### API changes, multiple API versions, and recommendations for users and applications interacting with Cluster API objects

sahaayaka yaa atirikta upa-aadesha.

##### Cluster API release vs contract versions

provaaidara ko kora ke saatha jodane kaa anubandha.

##### Supported Cluster API - Cluster API provider version Skew

sanskarana samarthana aura maitriksa.

#### Kubernetes versions support

netavarka porta soochii.

##### Maximum version skew between various Kubernetes components

sahaayaka yaa atirikta upa-aadesha.

### Supported versions matrix by provider or component

sanskarana samarthana aura maitriksa.

#### Core provider (`cluster-api-controller`)

inphraa/bootastraipa/kantrola-plena provaaidara.

#### Kubeadm Bootstrap provider (`kubeadm-bootstrap-controller`)

noda para pahalaa klastara / kubelet setaapa (bootastraipa).

##### Kubeadm configuration API Support

netavarka porta soochii.

#### Kubeadm Control Plane provider (`kubeadm-control-plane-controller`)

niyantrana tala (API server, etcd, …) prabandhana.

##### Bootstrap provider Support

noda para pahalaa klastara / kubelet setaapa (bootastraipa).

##### Etcd API Support

etcd sthaapanaa yaa baaharii etcd.

##### CoreDNS Support

netavarka porta soochii.

#### Other providers

inphraa/bootastraipa/kantrola-plena provaaidara.

#### clusterctl

clusterctl CLI se sanbandhita aadesha yaa setinga.

### Annexes

**Annexes**—isa upashiirshaka ke antargata moola peja men vistrita nirdesha, udaaharana yaa taalikaaen hain. satiika aadesha aura YAML ke lie oopara dii gaii angrejaii srota phaaaila kholen.

#### Kubernetes version Support and Cluster API deployment model

sanskarana samarthana aura maitriksa.

#### Kubernetes version specific notes

sahaayaka yaa atirikta upa-aadesha.

---

*vyaktigata hindii saara — `contrib-notes/book-hinglish`. aadhikaarika dastaaveja apastriima ripo men.*
