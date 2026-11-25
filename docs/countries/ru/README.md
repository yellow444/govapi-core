# Russia · RU

Sources verified November 25, 2026.

## Portal and interfaces

| System system | What's up | Access and source |
|---|---|---|
| EPSU and GUSMEV | Partnership integration under individual service contracts | Verify the published contract and IP admission for the service. [Catalogue of the API of EPSU](https://partners.gosuslugi.ru/catalog/api_for_gu) |
| ESIA | Identification and context of IP for integration | The EPGU guide describes registration, test outline and preparation of props. [EPGU](https://github.com/yellow444/epgu) |
| Municipal post and notifications | Channels of communication with differentiation by role | The portal notification collector is documented separately. [EPGU](https://github.com/yellow444/epgu) · [EPGU Bell](https://github.com/yellow444/epgu-bell) |

## GovAPI Core use case

Select one service and run it by specification: organization, IP clearance, package schema and signature, transaction logging, structured output. The original EPGU has SDKs, instructions and local mock cycle of the FSSP. The GovAPI Hub is now a training route. The full live FSSP cycle is not accepted.

## Bell use case

Use authorized events of one organization: Save ID, time stamp, and origin. Application status is derived from a structured response. The original Bell published a free local delivery with JSON and API. Acceptance of live TEST tape was performed on the previous candidate. [Bell Readiness](https://github.com/yellow444/epgu-bell/blob/v0.2.0-rc.4/docs/READINESS.md)

## Free and open-source alternatives

The public Go SDK contains examples of working with EPGU. EPGU publishes the Python SDK and the source of the public interface. EPGU Bell Free is distributed free of charge, the application has closed source. [Go SDK](https://github.com/ofstudio/go-api-epgu) · [EPGU](https://github.com/yellow444/epgu) · [Bell Free](https://github.com/yellow444/epgu-bell)

## Open questions

Agreed TEST-admission to one profile, number and result of the operation, access to a specific role of the notification recipient.
