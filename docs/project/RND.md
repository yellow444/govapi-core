# GovAPI Hub research and pilot decision

Decision recorded November 26, 2026. **First pilot: FIT-Connect TEST in Germany.** Submit one synthetic application to an authorized TEST destination, then retrieve a structured event for the same case. Start with an official SDK and record the result before designing an adapter. The local GovAPI form is a separate smoke check.

## Compare the application interfaces

| Candidate | Documented TEST and access | Decision |
|---|---|---|
| **Germany · FIT-Connect** | TEST self-service accepts an existing supported account without FITKO provisioning the user. The documentation covers sender credentials, destination setup, v2 submissions and the case event log. An anonymous request from the review runner returned HTTP 401. No authenticated session, destination or submission was tested. | **First technical pilot.** Confirm sign-in and a usable TEST destination before sending a synthetic request. [Environments](https://docs.fitko.de/fit-connect/docs/getting-started/environments/) · [Account and credentials](https://docs.fitko.de/fit-connect/docs/getting-started/account/) · [Germany guide](../countries/de/README.md) |
| **Kazakhstan · Smart Bridge** | TEST follows an authorized organization's application, approval by the service owner, and network setup by the operator. Service-specific schemas and response routing depend on the selected service. | **First partner-dependent candidate.** Find a participating organization and one service owner who can confirm TEST access and a correlatable structured response. [Official connection guide](https://new-sb.egov.kz/docs/ru/guides/kak-podklyuchitsya-k-servisu-na-smartbridge) · [Kazakhstan guide](../countries/kz/README.md) |
| **Russia · EPGU** | Public catalog and protocol specification are reachable. A registered information system and service authorization still govern the actual TEST operation. The upstream project provides a local FSSP mock. | **Defer a live pilot.** Confirm one service-specific grant and a supported synthetic payload. [Partner catalog](https://partners.gosuslugi.ru/catalog/api_for_gu) · [Russia guide](../countries/ru/README.md) |
| **Bangladesh · Nothi** | The manual describes submission, status polling and informing the applicant system. It describes integration by government offices. An external developer sandbox and independent access were not confirmed. | **Keep as a reference.** Revisit if an eligible government office offers a test route. [Nothi API manual](https://nothi.gov.bd/API) |

## Pilot exit criteria

1. Identify a TEST account, sender role, authorized destination and matching schema. Record the SDK and API versions.
2. Submit exactly one synthetic application. Preserve the returned case and submission identifiers as applicable.
3. Retrieve a structured event for the same case. A transport submission event is sufficient. Accepting it at the receiving system is optional and requires that role.
4. Record the environment, redacted identifiers, event type and timestamp, and the command or SDK steps needed to repeat the result. If sign-in, permissions or destination setup fail, stop and identify the blocker. Do not switch to STAGE or PROD.

The pilot tests official submission and event retrieval. It gives no proof of a substantive agency decision or inbox access. [FIT-Connect event log](https://docs.fitko.de/fit-connect/docs/getting-started/event-log/get-events/)

## Compare notification channels for Bell

| Candidate | What the official material supports | TEST and constraints |
|---|---|---|
| **Austria · Mein Postkorb** | Businesses can collect incoming messages through a web service. An authorized recipient enables collection, and the USP administrator configures certificates. | A demo environment is documented. **Leading Bell follow-on** once a business partner confirms access and the effects of collection and acknowledgement. Full service code was not verified. [Business collection](https://www.usp.gv.at/en/mein-postkorb/einstellungen/automatische-abholung.html) · [Technical guide](https://www.usp.gv.at/dam/jcr%3A0909b669-4372-438f-b3fd-c42a37ffc5f4/Mein_Postkorb_AutomatischeAbholung_HowTo.pdf) |
| **Spain · DEHú / LEMA** | Web services are designed for high-volume legal entities receiving administrative communications. The portal is a separate channel. | **Backup** if a qualifying partner confirms the integration route and rules for retrieval, acknowledgement, and effects on deadlines. Full service code was not verified. [DEHú and LEMA](https://administracionelectronica.gob.es/ctt/lema/infoadicional) |
| **Sweden · Mina Meddelanden** | Separate technical contracts cover senders, intermediaries and mailbox operators. | Vendor testing and access are role-specific. Confirm which test environment applies to the proposed actor. Full service code was not verified. [Technical contracts](https://www.digg.se/digitala-tjanster/digital-post/digital-post-for-dig-som-offentlig-aktor/teknisk-beskrivning-av-digital-post/tekniskt-tjanstekontrakt---api-specifikationer) |
| **Italy · App IO** | A connected public service can send messages and inspect delivery status. PagoPA publishes mobile and backend source. | A service can be tried in test mode. This is a sender-side reference. It does not confirm an external application can collect a recipient's mailbox. [Testing a service](https://developer.pagopa.it/en/app-io/guides/io-technical-guide/v6.0/function/publish-a-service/try-a-service-being-tested) · [IO app](https://github.com/pagopa/io-app) · [IO backend](https://github.com/pagopa/io-backend) |
| **Iceland · Digital Mailbox** | The documented REST contract connects document providers to the mailbox. The provider publishes a reference and supplies the document on recipient request. Source components are public. | Provider access follows onboarding. Treat the provider demo as a reference for the document side. Recipient-side collection for Bell remains unconfirmed. [Provider contract](https://docs.devland.is/products/postholf/postholf-01-intro-and-overview) · [Demo](https://github.com/digitaliceland/postholf-demo) · [Source](https://github.com/island-is/island.is) |

Bell itself can already be verified offline using an authorized synthetic export for one organization. Keep a future operator test out of the pilot until the recipient role and effects of retrieval are known. [Bell guide](https://github.com/yellow444/govapi-bell/blob/main/SINGLE_ORGANIZATION.md)

[Roadmap](ROADMAP.md) · [Source review method](SOURCE_REVIEW.md) · [Country directory](../countries/README.md)
