# Russia · EPGU

Sources reviewed November 26, 2026. This guide covers the local GovAPI demo and preparation for an authorized Gosuslugi TEST integration. GovAPI Core currently ships a navigator and demo, without a live EPGU adapter.

| Interface | Purpose | Access |
|---|---|---|
| EPGU / GUSMEV | Submit and track requests supported by a specific service contract | Requires a registered information system and authorization for that service. [Partner catalog](https://partners.gosuslugi.ru/catalog/api_for_gu) |
| ESIA | System identity and authorization | Use the organization and system registered for the target environment. The public EPGU connection guide describes the sequence. [Connection guide](https://github.com/yellow444/epgu/blob/main/project/epgu/PUBLIC_RELEASE_2026-11-07.md) |
| Government mailbox and portal notifications | Separate sources of communication and alerts | Verify the recipient role and permitted source separately. A notification should not be used to infer case status. [EPGU](https://github.com/yellow444/epgu) · [EPGU Bell readiness](https://github.com/yellow444/epgu-bell/blob/v0.2.0-rc.4/docs/READINESS.md) |

## 1. Run the local demo

Follow the [Core quick start](../../../README.md#quick-start). To start only this plugin, run from the Core directory:

```powershell
python .\serve.py --plugin .\plugins\ru.json
```

Select **Russia**. Enter `ORG-DEMO` as the organization and `demo-001` as the service code, then select **Get receipt**. Expect a receipt beginning with `DEMO-`. The [Bell quick start](https://github.com/yellow444/govapi-bell#quick-start) can add a two-message synthetic feed to this view. A separate [FSSP mock cycle](https://github.com/yellow444/epgu/blob/main/project/epgu/FSSP_MOCK_CYCLE.md) in the upstream EPGU project exercises more of the request lifecycle on local data.

## 2. Confirm who can use TEST

1. **Choose one service.** Record its catalog entry, service code, current version of the base API specification, and service-specific schema. The official v1.15 document is a reference for the base protocol. Recheck the catalog for superseding contracts before implementing. [Partner catalog](https://partners.gosuslugi.ru/catalog/api_for_gu) · [EPGU v1.15](https://gu-st.ru/content/partners/api_for_gu/Specifikaciya_API_EPGU_v1_15.docx)
2. **Confirm your tenant and system.** Identify the organization and its registered information system in TEST ESIA. Confirm the relevant authority and service permission with the operator. Keep TEST and PROD certificates, settings, and approval records separate. The local connection card tracks reported steps. It does not verify an account or grant access. [Public connection walkthrough](https://github.com/yellow444/epgu/blob/main/project/epgu/PUBLIC_RELEASE_2026-11-07.md)
3. **Check permissions before sending.** Obtain written confirmation of the role, allowed operation, test credentials, sample data rules, and any callback or signature requirements. If authentication works but the service returns `403` or `access_denied_system`, record the service and environment and ask the operator to confirm the grant. A successful token or read does not establish submission permission.

## 3. Accept one service end to end

1. Prepare the service's approved synthetic request. Validate the schema and any required package or signature locally.
2. Submit once through the authorized TEST interface. Record the returned transaction or application ID according to the service contract.
3. Query a documented structured status or receive the authorized callback. Match it to the same application ID. Record the status and the source of the response separately from any mailbox message.
4. Retain a redacted receipt, status or error code, specification version, and evidence that the environment was TEST. Stop if the service response has no documented correlation key, the role is denied, or the result is observable only in the consumer portal.

**Decision:** defer a live GovAPI pilot until one service-specific grant and an approved test request are confirmed. The local demo is available now. Core does not claim a complete live FSSP submission cycle.

## Source code availability

The public [EPGU project](https://github.com/yellow444/epgu) publishes a Python SDK and interface source. [go-api-epgu](https://github.com/ofstudio/go-api-epgu) is a separate public client. [EPGU Bell Free](https://github.com/yellow444/epgu-bell) is distributed free of charge. Its application source is closed.
