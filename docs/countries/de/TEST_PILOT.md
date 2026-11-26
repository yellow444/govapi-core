# FIT-Connect v2 TEST pilot

## November 27, 2026 — preflight

The first run is waiting for access to an authorized TEST sender and recipient. Zero submissions were sent and zero case events were retrieved.

| Check | Observed result |
| --- | --- |
| TEST portal | The direct sign-in page returned HTTP 200. The portal root returned HTTP 401 in the same unauthenticated check. No signed-in portal session or API authentication was verified. |
| Sender and recipient | Awaiting a TEST online-service client, its type C sender destination, and a type A/B recipient we administer or have permission to use. Recipient compatibility is still unverified. |
| Local preparation | A local client using FITKO's .NET SDK 4.0.0 built successfully and generated a synthetic fixture based on the official first-submission tutorial. The client was exercised in fixture mode. |

[TEST sign-in](https://portal.auth-testing.fit-connect.fitko.dev/login) · [FITKO account and credentials guide](https://docs.fitko.de/fit-connect/docs/getting-started/account/) · [FITKO first-submission tutorial](https://docs.fitko.de/fit-connect/docs/sdks/lernen/erste-submission/)

## Resume and record the result

1. Sign in to the TEST portal. Provision a TEST sender client and verify its association with the type C sender destination. Store credentials outside the repository.
2. Verify the authorized recipient's TEST destination ID, supported service and payload schema, and active encryption key. Use the tutorial fixture when the recipient is configured for that service and schema.
3. Send one synthetic submission. Retain the returned case and submission IDs locally. If the send outcome is uncertain, reconcile it before any further write.
4. Read the v2 event log for that case and submission using the same sender. Record the event type and timestamp after SDK verification. The pilot passes when the transport submission event is correlated with the sent case and submission. Keep raw identifiers and credentials out of the published report.

[Destination setup](https://docs.fitko.de/fit-connect/docs/receiving/destination/) · [v2 event log](https://docs.fitko.de/fit-connect/docs/getting-started/event-log/get-events/) · [SDK event verification](https://docs.fitko.de/fit-connect/docs/sdks/rezepte/status/) · [Pilot issue](https://github.com/yellow444/govapi-core/issues/7)
