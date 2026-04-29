# 22 — DevOps practice checklist

> **Hinglish:** *Monday morning list: context alag rakho, versions match karo, GitOps se drift kam karo, debug mein conditions dekho—sirf Pod logs pe depend mat raho.*

1. **Separate kubectl contexts** for management vs workload clusters—avoid “kubectl delete” accidents on the wrong API server.
2. **Install** core + bootstrap + control plane + infra providers with compatible versions (`clusterctl` helps).
3. **GitOps** your `Cluster`, `ClusterClass`, templates, and provider version pins—etcd on the management cluster becomes your audit trail.
4. **Debug via conditions and events** (`kubectl describe cluster`, controller logs), not only workload-cluster Pod logs.
5. **Stage upgrades**—bump Kubernetes version fields and provider images in non-prod first; read CAEPs/release notes.
6. **Contribute** documentation or tests when you find gaps—platform engineers often have the best operational feedback.

**Back to:** [Overview](./overview.md) · [First contributor guide](../first-contributor-guide.md)
