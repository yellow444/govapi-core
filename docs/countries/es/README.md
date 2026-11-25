# Spain · ES

Sources verified November 25, 2026.

## Portal and interfaces

| System system | Confirmed operation | Conditions and official source |
|---|---|---|
| DEHú / LEMA | Automatic receipt of administrative notifications and communications | Web services for businesses with a large number of inbounds, and a connected recipient can distribute correspondence between their departments. [Description of DEHú and LEMA](https://administracionelectronica.gob.es/ctt/lema/infoadicional) |
| Notifica | Sending administrative notices | Common platform for participating sending bodies. [Overview of administration notices](https://administracionelectronica.gob.es/estrategias/racionaliza-comparte/elementos-comunes/notificaciones-en-la-administracion) |
| FACe | Filing an invoice to the state customer, receipt and request for status | Departmental outline of electronic invoices: For web services, the provider registers the integrator and specifies the certificate. [Integration of FACe](https://administracionelectronica.gob.es/ctt/face/infoadicional) · [API documentation for suppliers](https://api.face.gob.es/providers/doc) |
| FACe, bill notifications | Proactive transfer of status changes described for SOAP | The historical description relates to the 2017 announcement, and the support for this contract for new integrations needs to be checked with the operator. [History of FACE](https://administracionelectronica.gob.es/ctt/face) |

## Core and Bell use cases

**Core:** Checking the TEST FACe for invoice filing, receipt and status by its ID, is an example of an industry process for a government supplier. **Bell:** Check the qualified recipient's connection to LEMA and understand what can be picked up without changing the legal status of the message. DEHú already provides an integration channel. The value of the individual application should be searched in the local archive, transfer to EDMS and assigning the message to the responsible person.

## Free and open-source alternatives

DEHú has a public web interface for recipients. LEMA has published an integration description. The publicity of the full platform code and the availability of a free third-party client for organizations are not confirmed by this card.

## Open questions

The order of connection of LEMA, support for the necessary operations in the test circuit, the legal effect of receiving or confirming, the active version of the FACe interface and the presence of push notifications in it.
