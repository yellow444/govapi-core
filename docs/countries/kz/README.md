# Kazakhstan · Smart Bridge

Sources reviewed November 26, 2026. Smart Bridge connects an organization's information system to a service published by another organization. This guide covers the GovAPI demo and the approval path for one service. GovAPI Core currently has no live Smart Bridge adapter.

| Channel | Role in the flow |
|---|---|
| eGov and eGov Business | User-facing channels. A visible application status does not grant an external system access to it. [eGov Business](https://nitec.kz/index.php/ru/news/egov-business-gosudarstvennye-uslugi-dlya-predprinimateley-v-paru-klikov) |
| Smart Bridge service catalog | Identifies the owner and requirements for a specific integration service. [Connection guide](https://new-sb.egov.kz/docs/ru/guides/kak-podklyuchitsya-k-servisu-na-smartbridge) |
| eLicense | User-facing licensing and permit procedures. Select a Smart Bridge service and verify its own contract when a corresponding integration exists. [Example procedure](https://egov.kz/cms/ru/services/business_registration/reg_ip) · [Smart Bridge public services](https://new-sb.egov.kz/docs/ru/guides/kak-rabotat-s-gosuslugami) |

## 1. Run the local demo

Follow the [Core quick start](../../../README.md#quick-start). To load only Kazakhstan, run from the Core directory:

```powershell
python .\serve.py --plugin .\plugins\kz.json
```

Select **Kazakhstan**, enter `ORG-DEMO` and `demo-001`, then select **Get receipt**. Expect a `DEMO-` receipt. It shows that the local form and plugin work. It does not represent a Smart Bridge request or approval.

## 2. Apply for access to one TEST service

1. **Identify the service and owner.** Open the service passport in the catalog. Record the identifier, version, response mode, eligible client roles, and the owner who can confirm access. Verify the selected service is available to your type of organization.
2. **Prepare the application.** The first head of the organization or an employee with signing authority submits it. Prepare the basis for connection, responsible contact, information-system details and network scheme. Ask the service owner and operator which certificate and authentication modes apply. The guide requires organization certificates tied to the organization's BIN when the corresponding certificate check applies. [Official connection checklist](https://new-sb.egov.kz/docs/ru/guides/kak-podklyuchitsya-k-servisu-na-smartbridge)
3. **Agree on response delivery.** For synchronous services, confirm the response schema. For asynchronous services, agree on the TEST delivery URL, request correlation field and expected acknowledgement. The operator guide requires HTTPS for the production delivery address. Keep any TEST and PROD settings separate.
4. **Wait for approval and network setup.** The service owner approves the request and the operator configures network access. Confirm the TEST endpoint, supported schemas and permitted synthetic data. The production move follows testing and its own documentation.

## 3. Verify the authorized result

1. Validate one synthetic request using the owner-supplied contract. Run it once in the authorized TEST environment.
2. For a synchronous service, save the structured result and correlation field. For an asynchronous service, retain the dispatch receipt and verify the response at the agreed receiver. Match it to the original request using the documented field.
3. Record service version, response or error code, date, and redacted identifiers. Stop and contact the owner if the network settings, rights or correlation contract are missing.

**Decision:** keep Smart Bridge as the first partner-dependent candidate. Start a live pilot only after a participating organization and the owner of a specific service confirm the TEST path. Smart Bridge can deliver a service response. General eGov Business notifications require a separately verified source and access grant.

## Source code availability

[Documentolog](https://documentolog.com/en/tariffs) offers basic free document workflows and lists government exchange and CRM APIs in its Business plan. The source code for the full product was not verified. [SIGEX's NCALayer client](https://github.com/sigex-kz/ncalayer-js-client) is a public signing component.
