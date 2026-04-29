# `util/` — shared helpers

> **Hinglish:** *Conditions, patch, predicates, collections—controllers in sab ko import karte hain; yahan duplicate logic kam.*

## Purpose

Cross-cutting **Go utilities** safe for provider import: patching, conditions, machine collections, logging helpers, etc. Large surface—browse subpackages as needed.

## Start reading here

- [`util/conditions/`](../../util/conditions/) — condition aggregation
- [`util/patch/`](../../util/patch/) — patch helpers used in reconcilers
- [`util/predicates/`](../../util/predicates/) — controller-runtime predicates (pause, labels)

## How it connects

Nearly every **`internal/controllers`** package imports `sigs.k8s.io/cluster-api/util/...`.

## Official docs

- No single book page; follow call sites from controllers you are debugging.

## See also

- [03 — `internal/controllers`](03-internal-controllers.md)
