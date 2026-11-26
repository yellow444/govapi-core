# Germany · FIT-Connect

Sources reviewed November 26, 2026. FIT-Connect is the first GovAPI pilot because its TEST environment documents self-service access, a submission interface, and a case event log. GovAPI Core currently includes a local guide and demo form. No live pilot submission has been executed.

| Environment | Access and use |
|---|---|
| TEST | Open to interested developers through the [TEST self-service portal](https://portal.auth-testing.fit-connect.fitko.dev). Sign in with an existing GitHub, GitLab, openCode, or eligible Mein Unternehmenskonto account. FITKO does not need to activate users for TEST. The environment supports self-generated test certificates and has no availability guarantee. |
| STAGE and PROD | Separate onboarding and credentials. The account guide lists Mein Unternehmenskonto for these environments. A working TEST client does not establish production access. |

[Environment guide](https://docs.fitko.de/fit-connect/docs/getting-started/environments/) · [Account and credential guide](https://docs.fitko.de/fit-connect/docs/getting-started/account/)

## 1. Run the local demo

Follow the [Core quick start](../../../README.md#quick-start). To load only Germany, run from the Core directory:

```powershell
python .\serve.py --plugin .\plugins\de.json
```

Select **Germany**, enter `ORG-DEMO` as the demo operator and `DEST-DEMO` as the sample recipient ID, then select **Get receipt**. Expect a `DEMO-` receipt. This uses a local synthetic form, without connecting to FIT-Connect.

## 2. Set up the official TEST path

1. **Choose a current contract and SDK.** Use the documented v2 submission and event endpoints for this exercise. FITKO's documentation announces the v1 shutdown on October 27, 2026. Record the API and SDK versions you use. [v2 migration guide](https://docs.fitko.de/fit-connect/docs/major-release/fit-connect_2/) · [Official SDKs](https://docs.fitko.de/fit-connect/docs/sdks/overview/)
2. **Create a TEST sender credential.** Sign in to the TEST portal with an authorized account and use the credential menu to configure a sender client. Keep the client secret outside the project and evidence. Use TEST credentials with the TEST token URL listed by FITKO. [Credential setup](https://docs.fitko.de/fit-connect/docs/getting-started/account/) · [TEST URLs](https://docs.fitko.de/fit-connect/docs/getting-started/environments/)
3. **Identify an authorized TEST destination.** Use a destination you administer or have explicit permission to use. Confirm expected schema, supported payloads, encryption requirements, and recipient role. If you need to create or operate a receiver, use separate receiver credentials assigned to that destination. [Account and destination permissions](https://docs.fitko.de/fit-connect/docs/getting-started/account/) · [Sending overview](https://docs.fitko.de/fit-connect/docs/sending/overview/)

## 3. Submit one synthetic request and read its event

1. Prepare one synthetic payload using the chosen destination schema. Use the official SDK for validation and packaging according to the sending guide. [Start a submission](https://docs.fitko.de/fit-connect/docs/sending/start-submission/) · [Submit](https://docs.fitko.de/fit-connect/docs/sending/submit/)
2. Submit once to the authorized TEST destination. Keep the returned case ID and submission ID as available. If a request times out after sending, reconcile its known ID before resubmitting.
3. Read the case event log from the sender's context. The documented v2 route is `GET /v2/cases/{caseId}/events` under the TEST Submission API. With an SDK, use its documented equivalent for the status check. Expect the event for the same synthetic submission. `submit-submission` confirms transport submission. `accept-submission` requires action by the receiving system and is optional for this pilot. Neither event establishes a substantive agency decision. [Read the event log](https://docs.fitko.de/fit-connect/docs/getting-started/event-log/get-events/) · [Event types](https://docs.fitko.de/fit-connect/docs/getting-started/event-log/events/)
4. Record the environment, SDK and API versions, redacted identifiers, event type and timestamp. Stop if the destination, role, or event access is unclear. Preserve the stage and response code to distinguish a setup error from a denied role or an unavailable destination.

**Pilot acceptance:** one synthetic submission through the real TEST service and a correlatable structured submission event. Receipt generation in GovAPI Core is only the local smoke check. The FIT-Connect event log is a transport source. Inbox access or government mailbox integration is separate.

## Source code availability

FITKO documents Java, .NET, and JavaScript SDKs and provides public SDK resources. This guide makes no claim about the availability of source for the full service. [SDK overview](https://docs.fitko.de/fit-connect/docs/sdks/overview/)

[Pilot decision and alternatives](../../project/RND.md)
