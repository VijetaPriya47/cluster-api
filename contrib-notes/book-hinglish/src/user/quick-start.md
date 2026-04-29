# Quick Start — hindii vyaakhyaa

> **nota:** yaha peja aadhikaarika pustaka kaa **hindii saara** hai. kamaanda, poorna YAML aura truti sandesha angrejaii moola men dekhen.

## aadhikaarika srota

- ripojaitarii: [`docs/book/src/user/quick-start.md`](../../../../../docs/book/src/user/quick-start.md)
- veba (angrejaii): [Quick Start](https://cluster-api.sigs.k8s.io/user/quick-start.html)

## isa gaaida kaa uddeshya

**kvika staarta** aapako sabase kama kadamon men eka **prabandhana klastara** taiyaara karake **pahalaa varkaloda klastara** banaanaa sikhaataa hai. angrejaii moola men kaii klaauda provaaidara ke lie taiba aura aadesha hain; sanrachanaa hara jagaha samaana hai.

## kadamon kaa taaratamya (hindii men)

1. **poorvaapekshaaen** — `kubectl`, maujoodaa Kubernetes (aksara kind), aura chune hue provaaidara ke lie klaauda khaataa/tokana.
2. **clusterctl instola** — OS ke anusaara baainarii yaa homabroo.
3. **`clusterctl init`** — kora Cluster API aura chune inphraa/bootastraipa/kantrola-plena provaaidara ko prabandhana klastara para lagaanaa; provaaidara ke anusaara env/siikreta.
4. **varkaloda klastara** — tempaleta taiyaara karanaa (`generate cluster`), YAML laagoo karanaa, **kubeconfig** lekara API sarvara se judanaa.
5. **CNI** — poda netavarka ke binaa noda `Ready` nahiin honge; eka CNI instola karen.
6. **saphaaii** — prayoga ke baada sansaadhana hataanaa.

## niiche khanda-vaara saara

pratyeka khanda ke tahata vahii krama vistaara se hai—jaba aapa kisii eka provaaidara (AWS, Azure, Docker, …) chunate hain, moola peja para usii ke aadesha dikhenge.

## khanda-vaara saara (hindii)

### Installation

sthaapanaa ke charana, vikalpa aura jaancha.

#### Common Prerequisites

shuroo karane se pahale jaroorii aujaaara, sanskarana aura pahuncha.

#### Install and/or configure a Kubernetes cluster

sthaapanaa ke charana, vikalpa aura jaancha.

#### Install clusterctl

sthaapanaa ke charana, vikalpa aura jaancha.

##### Install clusterctl binary with curl on Linux

sthaapanaa ke charana, vikalpa aura jaancha.

##### Install clusterctl binary with curl on macOS

sthaapanaa ke charana, vikalpa aura jaancha.

##### Install clusterctl with homebrew on macOS and Linux

sthaapanaa ke charana, vikalpa aura jaancha.

##### Install clusterctl binary with curl on Windows using PowerShell

sthaapanaa ke charana, vikalpa aura jaancha.

#### Initialize the management cluster

jahaan Cluster API niyantraka chalate hain.

##### Enabling Feature Gates

praayogika phaiichara chaaloo karanaa.

##### Initialization for common providers

inphraa/bootastraipa/kantrola-plena provaaidara.

##### Install MetalLB for load balancing

sthaapanaa ke charana, vikalpa aura jaancha.

##### Install KubeVirt on the kind cluster

sthaapanaa ke charana, vikalpa aura jaancha.

##### Initialize the management cluster with the KubeVirt Provider

inphraa/bootastraipa/kantrola-plena provaaidara.

#### Create your first workload cluster

vaha klastara jisa para aipa chalenge—banaanaa aura kubeconfig.

##### Preparing the workload cluster configuration

vaha klastara jisa para aipa chalenge—banaanaa aura kubeconfig.

##### Required configuration for common providers

inphraa/bootastraipa/kantrola-plena provaaidara.

##### Generating the cluster configuration

**Generating the cluster configuration**—isa upashiirshaka ke antargata moola peja men vistrita nirdesha, udaaharana yaa taalikaaen hain. satiika aadesha aura YAML ke lie oopara dii gaii angrejaii srota phaaaila kholen.

##### Apply the workload cluster

vaha klastara jisa para aipa chalenge—banaanaa aura kubeconfig.

##### Accessing the workload cluster

vaha klastara jisa para aipa chalenge—banaanaa aura kubeconfig.

#### Install a Cloud Provider

sthaapanaa ke charana, vikalpa aura jaancha.

#### Deploy a CNI solution

poda netavarka (CNI) lagaanaa.

#### Clean Up

sansaadhana saapha karanaa.

### Next steps

aage kyaa padhanaa yaa karanaa hai.

---

*vyaktigata hindii saara — `contrib-notes/book-hinglish`. aadhikaarika dastaaveja apastriima ripo men.*
