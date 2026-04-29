# 20 — Security design (high level)

Cluster API touches **highly privileged** operations (cloud resources, kubeconfigs, join tokens). The codebase reflects that with several layers:

> **Hinglish:** *Security yahan ppt slide nahi—RBAC markers, webhooks, Secrets: har layer ka reason hai. Galat permission = cluster hijack ya leak, isliye audit important hai.*

## RBAC generated from code

`+kubebuilder:rbac` markers next to reconcilers become **ClusterRole** fragments. Reviewers can audit permissions **next to** the logic that needs them.

## Admission webhooks

Validating webhooks reject impossible or unsafe specs; mutating webhooks apply defaults consistently. CRD patches under `config/crd` wire conversion/validation paths.

## TLS for webhooks

Typical installs integrate **cert-manager** to rotate serving certificates for webhook servers—avoids long-lived static certs in Git.

## Secrets, not ConfigMaps, for credentials

Bootstrap and kubeconfig material belong in **Secret** objects with tight RBAC. The codebase and docs warn against logging sensitive fields.

## Finalizers and owner references

Prevent **orphaned** cloud resources and unsafe etcd teardown; comments in controllers reference admission plugins like **OwnerReferencesPermissionEnforcement** when extra RBAC is required.

## Supply chain hygiene

Tooling versions live under `hack/tools`; CI runs verify targets. Study release processes for how images are built and signed (project docs evolve—read current release docs).

**Next:** [Design patterns](./21-design-patterns.md).
