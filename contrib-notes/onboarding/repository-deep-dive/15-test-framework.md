# 15 — E2E framework (`test/framework/`)

Shared libraries for e2e and provider tests: **clusterctl helpers**, **cluster proxies**, **bootstrap** abstractions, **Ginkgo** extensions.

> **Hinglish:** *Framework = test ka “shared toolbox”—har provider apna e2e likhe, par cluster create/wait/assert yahi se reuse ho.*

## Loading `E2EConfig`

```56:72:test/framework/clusterctl/e2e_config.go
// LoadE2EConfig loads the configuration for the e2e test environment.
func LoadE2EConfig(ctx context.Context, input LoadE2EConfigInput) *E2EConfig {
	configData, err := os.ReadFile(input.ConfigPath)
	Expect(err).ToNot(HaveOccurred(), "Failed to read the e2e test config file")
	Expect(configData).ToNot(BeEmpty(), "The e2e test config file should not be empty")

	config := &E2EConfig{}
	Expect(yaml.Unmarshal(configData, config)).To(Succeed(), "Failed to convert the e2e test config file to yaml")

	Expect(config.ResolveReleases(ctx)).To(Succeed(), "Failed to resolve release markers in e2e test config file")
	config.Defaults()
	config.AbsPaths(filepath.Dir(input.ConfigPath))

	Expect(config.Validate()).To(Succeed(), "The e2e test config file is not valid")

	return config
}
```

**Line-by-line meaning:**

1. **Read file** from disk—config is **data-driven** so CI can swap versions without recompiling tests.
2. **Unmarshal YAML** into `E2EConfig` struct tags map fields like `managementClusterName`, `images`, provider lists (see struct definition later in the same file).
3. **`ResolveReleases`:** Substitutes **version markers** (e.g. latest patch of a minor line) using network or cached metadata—keeps tests pinned but not brittle.
4. **`Defaults` / `AbsPaths`:** Normalize relative paths so jobs work from any working directory.
5. **`Validate`:** Fail fast if images/providers are inconsistent.

**Pattern:** This is **declarative test configuration**—the same discipline CAPI applies to clusters, applied to **test environments**.

> **Hinglish:** *YAML config + `ResolveReleases` = versions pin ho par “latest patch” jaisa marker bhi chal sake—CI friendly.*

**Next:** [`internal/test/envtest`](./16-envtest.md).
