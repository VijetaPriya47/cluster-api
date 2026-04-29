# Provider contract — Simple Hinglish

> **Note:** Exact CR/spec wording ke liye English source dekho. Yahan “provider contract” ka simple matlab samjha raha hoon.

## aadhikaarika srota

- ripojaitarii: [`docs/book/src/developer/providers/contracts/overview.md`](../../../../../../../docs/book/src/developer/providers/contracts/overview.md)
- veba (angrejaii): [Provider contract](https://cluster-api.sigs.k8s.io/developer/providers/contracts/overview.html)

## Provider contract ka simple matlab

### Contract kyu zaroori hai?

Provider contract ek **spec/agreement** hai jisme define hota hai:

- provider ke CRs/fields ka meaning
- aur provider ke CR lifecycle me Core controllers ko kaunse **status/conditions/relationships** milni chahiye

## Controllers relation (mental model)

Management cluster me Core controllers (jaise `Cluster`, `Machine`, `MachineDeployment` etc.) reconciliation chalate hain.

Provider contract un reconciliation steps ko “expected behavior” ke saath align karta hai, taaki different providers core workflow me compatible rahein.

## Contribute kaise karein

Contract improve karne ke liye PRs/feedback submit karo (clarifications, edge cases, aur compatibility changes ke saath).

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
