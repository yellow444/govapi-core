# Czechia · CZ

Sources verified November 25, 2026.

## Portal and interfaces

| System system | What's up | Access and source |
|---|---|---|
| Datové schránky, ISDS | Legally significant electronic correspondence, separate web services for applications | Box authorization and user role: The official help describes how to connect a third-party application via a mobile key. [Portal](https://datovka.gov.cz/) · [Third-party annexes](https://datovka.gov.cz/info/cs/help/15.3.text.html) |
| Public Technical Documentation of ISDS | Customer Integration, Technical Help and Examples | From the official certificate, a transition to the developer support center is available. [ISDS documentation](https://datovka.gov.cz/info/cs/help/15.3.text.html) |

## Written by GovAPI Core and Bell

The public part can explain the configuration and roles of ISDS. For Bell, first, compare the script of reading and exporting official correspondence with Datovka. The verifiable result is the transfer of authorized exports to the common work queue and the preservation of identifiers. The GovAPI Hub adapter is not yet available.

## Free and open-source alternatives

| Product | What works for free | Source code availability | Paid or restricted |
|---|---|---|---|
| Datovka | Reading, sending, local archive, multiple boxes, export and CLI | GPLv3 source. [Code.](https://gitlab.nic.cz/datovka/datovka) · [CLI](https://www.datovka.cz/datovka-docs/en/datovka/cli/) | Access to the box is determined by ISDS rights |
| Dokkio | One firm and user, download, archive and timing control | Publicity of the sources is not confirmed | API, webhook and command functions on tariffs. [Tariffs](https://dokkio.cz/cenik/) |

## Open questions

Test environment and acceptable action for the role of recipient: Separately, determine the legal significance of receiving and reading a message prior to automatic import.
