# `test/infrastructure/docker/` — CAPD

> **Hinglish:** *Docker = fake VMs for dev/CI; production cloud provider nahi.*

## Purpose

**Infrastructure provider** implementation using containers: API types under [`test/infrastructure/docker/api/`](../../test/infrastructure/docker/api/), controllers talking to Docker API, manifests under `config/`.

## Start reading here

- [`test/infrastructure/docker/README.md`](../../test/infrastructure/docker/README.md)
- [`test/infrastructure/docker/api/v1beta2/dockermachine_types.go`](../../test/infrastructure/docker/api/v1beta2/dockermachine_types.go)

## Official docs

- CAPD is documented in developer guides / Tilt; see [Tilt](https://cluster-api.sigs.k8s.io/developer/core/tilt.html)

## See also

- [Infra contract](https://cluster-api.sigs.k8s.io/developer/providers/contracts/infra-machine.html)
