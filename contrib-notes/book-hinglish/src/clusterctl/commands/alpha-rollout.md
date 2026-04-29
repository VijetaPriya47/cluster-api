# clusterctl alpha rollout — Simple Hinglish

`clusterctl alpha rollout` ek alpha command-set hai jo **kuch Cluster API resources** par operational rollout actions karta hai.

## Supported ideas (based on code/flags)

### `restart`

- `clusterctl alpha rollout restart RESOURCE`
- code: `cmd/clusterctl/cmd/rollout/restart.go`
- “resource rollout restart” (bas reconcile ko force karne/refresh karne ka operational nudge)

### `pause` / `resume`

- `pause RESOURCE`:
  - pausing ka meaning: resource ko controller reconcile nahi karega
  - code comments ke hisaab se currently mainly `MachineDeployment` aur `KubeadmControlPlane` pause/resume support karte hain
- `resume RESOURCE`:
  - paused state remove hoti hai, phir controller reconcile dubara start karta hai

## Controllers relation

Yeh “controllers” khud start/stop nahi karta.

Yeh sirf resources ki state/annotations/paused condition ko change karta hai, jiske baad **controllers apni reconcile decision change** karte hain.

