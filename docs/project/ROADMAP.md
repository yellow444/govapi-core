# GovAPI Hub roadmap

November 26, 2026

GovAPI Hub brings country plugins and Bell together in one interface. The public distribution supports one operator and organization. The team edition adds roles, multiple organizations, scheduling, routing, and an audit trail.

| Phase | Deliverables | Exit criteria |
|---|---|---|
| **01 · Foundation** | Plugin and feed contracts, quick start, and reproducible local demo | A clean checkout runs without government credentials. Verify country switching, a demo receipt, and reimport without duplicates. |
| **02 · Guides and R&D** | Step-by-step guides for Russia, Kazakhstan, and Germany, a single-organization Bell guide, and research on access and source availability | Another developer can reproduce the guide. The pilot has a current official contract, an eligible role, a TEST environment, and an observable result. |
| **03 · Platform pilots** | One end-to-end operation in an official test environment, then one authorized notification source | Verify structured case status and notifications separately. Record permissions, identifiers, retries, and error handling. Evaluate the second adapter and team features afterward. |

## Current focus

1. Finalize the manifest and country context. Verify that Core can read the Bell feed.
2. Publish a quick start and run a minimal smoke check. Limit code changes to issues that prevent startup or foundation acceptance.
3. Prepare the country guides and select the first pilot. FIT-Connect is the leading candidate for a technical demo. Smart Bridge is a candidate once a local partner confirms access.

The three demo plugins and local Bell archive are already available. The live adapter and team workspace are future deliverables. Set pilot dates after access is confirmed.

[Research](RND.md) · [Workflow](WORKFLOW.md) · [Country directory](../countries/README.md)

## Current issues

| Issue | Repository |
|---|---|
| [Finalize the country plugin v1 contract](https://github.com/yellow444/govapi-core/issues/1) | govapi-core |
| [Publish an end-to-end quick start](https://github.com/yellow444/govapi-core/issues/2) | govapi-core |
| [Verify the GovAPI Hub foundation in clean checkouts](https://github.com/yellow444/govapi-core/issues/3) | govapi-core |
| [Finalize the Bell feed contract and verify Core compatibility](https://github.com/yellow444/govapi-bell/issues/1) | govapi-bell |

[Core issues](https://github.com/yellow444/govapi-core/issues) · [Bell issues](https://github.com/yellow444/govapi-bell/issues)
