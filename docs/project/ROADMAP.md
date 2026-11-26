# GovAPI Hub roadmap

November 26, 2026

GovAPI Hub brings country plugins and Bell together in one interface. The public distribution supports one operator and organization. The team edition adds roles, multiple organizations, scheduling, routing, and an audit trail.

| Phase | Deliverables | Exit criteria |
|---|---|---|
| **01 · Foundation** | Plugin and feed contracts, quick start, and reproducible local demo | A clean checkout runs without government credentials. Verify country switching, a demo receipt, and reimport without duplicates. |
| **02 · Guides and R&D** | Step-by-step guides for Russia, Kazakhstan, and Germany, a single-organization Bell guide, and research on access and source availability | Another developer can reproduce the guide. The pilot has a current official contract, an eligible role, a TEST environment, and an observable result. |
| **03 · Platform pilots** | One end-to-end operation in an official test environment, then one authorized notification source | Verify structured case status and notifications separately. Record permissions, identifiers, retries, and error handling. Evaluate the second adapter and team features afterward. |

## Current focus

The public foundation has passed smoke checks from clean Core and Bell clones. The country guides and single-organization Bell guide describe the local workflow, official access requirements, and acceptance evidence.

The first technical pilot uses FIT-Connect TEST. Before implementation, verify sign-in and an authorized TEST destination. The pilot must produce one synthetic submission and a structured event for the same case. Kazakhstan remains the first candidate that needs a partner. See the [pilot decision](RND.md).

[Research](RND.md) · [Workflow](WORKFLOW.md) · [Country directory](../countries/README.md)

## Foundation verification record

| Issue | Repository |
|---|---|
| [Finalize the country plugin v1 contract](https://github.com/yellow444/govapi-core/issues/1) | govapi-core |
| [Publish an end-to-end quick start](https://github.com/yellow444/govapi-core/issues/2) | govapi-core |
| [Verify the GovAPI Hub foundation in clean checkouts](https://github.com/yellow444/govapi-core/issues/3) | govapi-core |
| [Finalize the Bell feed contract and verify Core compatibility](https://github.com/yellow444/govapi-bell/issues/1) | govapi-bell |

[Core issues](https://github.com/yellow444/govapi-core/issues) · [Bell issues](https://github.com/yellow444/govapi-bell/issues)
