# Diagnostics — Simple Hinglish

> **Note:** Yeh page “debugging/observability” guide hai. Exact commands/YAML ke liye English source follow karo.

## Official source

- Repo: [`docs/book/src/tasks/diagnostics.md`](../../../../../docs/book/src/tasks/diagnostics.md)
- Web: [Diagnostics](https://cluster-api.sigs.k8s.io/tasks/diagnostics.html)

## Diagnostics me kya-kya aata hai?

Cluster API controllers (core + providers) running hone par aapko 3 main cheeze chahiye hoti hain:

1. **metrics**: controllers ka health/perf signals
2. **profiles**: CPU/memory profiling for deep performance debugging
3. **logs**: reconcile issues, errors, conditions changes

## 1) Scraping metrics

### via Prometheus

Idea:

- Prometheus cluster API controllers ke metrics endpoints scrape karta hai
- phir aap graphs/alerts bana sakte ho

### via kubectl

Idea:

- quick debug ke liye port-forward karke metrics endpoint hit karo
- “is controller alive + what is it doing” quickly check hota hai

## 2) Collecting profiles

Profiles ka use tab hota hai jab:

- controller slow/CPU heavy lag raha ho
- reconcile loops unexpected spikes de rahe ho

### via Parca

Idea:

- Parca continuous profiling stack
- time-range me call stacks dekh ke bottlenecks spot karte ho

### via kubectl

Idea:

- targeted profiling endpoints (pprof) ko port-forward karke capture
- local analysis (go tool pprof etc.)

## 3) Changing log level

Log level increase tab karte ho jab:

- issue reproduce ho raha hai but logs me detail nahi

via `kubectl` typically:

- deployment/args/env update karke verbosity bump
- phir logs collect

---

*Simple/Hinglish notes — `contrib-notes/book-hinglish`.*
