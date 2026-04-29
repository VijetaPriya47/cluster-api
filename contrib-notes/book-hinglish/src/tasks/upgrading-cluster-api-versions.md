# Upgrading Cluster API components — Simple Hinglish

> **Note:** Ye page management cluster side ke components upgrade par focus karta hai (CAPI core + providers). Exact upgrade commands ke liye English source follow karo.

## Official source

- Repo: [`docs/book/src/tasks/upgrading-cluster-api-versions.md`](../../../../../docs/book/src/tasks/upgrading-cluster-api-versions.md)
- Web: [Upgrading Cluster API components](https://cluster-api.sigs.k8s.io/tasks/upgrading-cluster-api-versions.html)

## “When to upgrade” (simple)

Upgrade tab karo jab:

- aapko bugfix/security fix chahiye
- aap next contract/API version adopt kar rahe ho
- providers ke compatibility requirements change ho gaye

## Considerations (high level)

### Contract compatibility

Core + providers ko compatible contract versions support karne chahiye.

`clusterctl upgrade plan/apply` ka reason bhi yahi hai: ek sane set of versions select karna.

### CRDs + webhooks

Management cluster upgrade me:

- CRDs changes aate hain
- webhooks/conversions ka impact hota hai

Isliye upgrade steps carefully order me follow karne chahiye.

## 1.0.x → newer versions (idea)

Patch/minor upgrades me generally:

- newer provider versions install
- controllers roll out
- compatibility checks pass hon

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
