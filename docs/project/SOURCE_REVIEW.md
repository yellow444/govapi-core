# Review government API sources and public code

Add evidence directly to the [country profile template](../countries/TEMPLATE.md). Summarize verified facts and access limits in the [global directory](../countries/GLOBAL_INDEX.md).

1. **Identify the operation.** Keep submission, case status, message retrieval, and notification delivery status separate. Record the jurisdiction, service, official owner, and integration role.
2. **Check the primary source.** Prefer the operator's service or API documentation, published contract, or onboarding guide. Record the exact link, review date, and published version when available. Cite the document that supports the stated operation. Describe a portal, data catalog, or exchange bus by its actual role.
3. **Record access evidence.** State what the documentation says about the authorized roles, credentials, TEST, and PROD. Use **documented** for a published contract, **verified in TEST** only after an authorized run, and **unconfirmed** when the necessary evidence is missing. Report public page checks separately from API execution.
4. **Identify the code.** Link to the source repository and license. Describe what it covers, such as the full service, a client, SDK, or sample. A published API specification, user app, or free tier alone does not establish open-source availability for the underlying service.
5. **State the acceptance gate.** Record the expected observable result and what would block the pilot. For an actual test, retain the environment, role, date, API version, and redacted receipt or event. Keep organization data and credentials out of the public index.

## Examples

| Country | What to record | Limit |
|---|---|---|
| Germany | FIT-Connect documents v2 case events and self-service TEST credentials. Published SDK resources support integrations. [Events](https://docs.fitko.de/fit-connect/docs/getting-started/event-log/get-events/) · [Accounts](https://docs.fitko.de/fit-connect/docs/getting-started/account/) · [SDKs](https://docs.fitko.de/fit-connect/docs/sdks/overview/) | An authorized sender and destination still need a live TEST run. The SDK evidence does not establish the license of the full service. |
| Italy | App IO documents a message API. The mobile and backend repositories publish code under EUPL-1.2. [Message API](https://developer.pagopa.it/en/app-io/api) · [Mobile code](https://github.com/pagopa/io-app) · [Backend code](https://github.com/pagopa/io-backend) | Message delivery status is not an administrative case status. Recipient mailbox collection is a separate question. |
