# clusterctl for Developers — Simple Hinglish

> **Note:** Yeh page “developers” workflow ko simple Hinglish me samjhata hai. Exact commands/flags ke liye English source check karo.

## aadhikaarika srota

- ripojaitarii: [`docs/book/src/clusterctl/developers.md`](../../../../../docs/book/src/clusterctl/developers.md)
- veba (angrejaii): [clusterctl for Developers](https://cluster-api.sigs.k8s.io/clusterctl/developers.html)

## Developer workflow (simple)

### 1) Tools/version setup

Sabse pehle dev ke liye required tools/versions set karo (details English source me dekho).

### 2) Local artifacts/offline setup

- `clusterctl-settings.json` jaise config se local artifact locations map hoti hain
- “local repository” se providers/components/templates generate/serve hote hain

### 3) Management cluster create aur run

`kind` management cluster banao, phir `clusterctl init` se Core controllers/reconcilers start karo.

### 4) Output validate karo

Generated templates/YAML ka behavior verify karo. Docker Desktop provider ke case me workload kubeconfig handling par focus rakho.

---

*vyaktigata hindii saara — `contrib-notes/book-hinglish`. aadhikaarika dastaaveja apastriima ripo men.*
