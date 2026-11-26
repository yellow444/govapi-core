# Country plugin contract v1

A country plugin is a UTF-8 JSON manifest passed explicitly to `serve.py --plugin <file>`. Core accepts multiple plugin arguments and presents them in argument order. Restart Core to change the manifest set. Plugin IDs must be unique across the loaded files. A rejected manifest or duplicate ID stops startup and reports the file.

## Manifest fields

| Field | Type | Requirement |
|---|---|---|
| `schema` | Integer | Exactly `1`. JSON booleans, decimal values, strings, and other versions are rejected. |
| `id` | String | Matches `[a-z]{2}`. Use the same ID in requests and any Bell feed for the country. |
| `country`, `platform`, `summary` | Strings | Non-blank display text. |
| `steps` | Array | One or more objects. Each has non-blank `title`, `detail`, `source`, and `url` strings. Use HTTPS links to public sources and omit credentials from URLs. |
| `fields` | Object | One or more entries. Keys match `[a-z][a-z_]{0,39}`. Values are non-blank form labels. |
| `bell` | Boolean | Enables the notifications section for this country. You can load the plugin before connecting a feed. |

Use [the bundled examples](plugins/) as a starting point. Copy an example, give it a new ID and appropriate guide text, and load it in a clean start with `--plugin path\to\country.json`. Check that the country appears and the demo form shows the declared fields. Keep credentials and account data outside the manifest. A manifest provides reference content and demo inputs. Official adapters and permissions are separate.

## Local HTTP endpoints

| Endpoint | Result |
|---|---|
| `GET /api/plugins` | JSON array of connected manifests. With no plugins configured, the array is empty. |
| `POST /api/mock` | Send `application/json` with `country` and a `fields` object. Field keys must match the manifest exactly. Each value must be a string of 1 to 120 characters after trimming. Unknown countries and invalid fields return HTTP 400. |
| `GET /api/feed?country=ru` | Demo Bell envelope for the requested country. Returns HTTP 200 with JSON `null` when the plugin enables Bell but no feed is connected, HTTP 404 for an unknown country or a plugin with Bell disabled, and HTTP 503 when a configured feed cannot be read or validated. |

For example, the Russia plugin accepts:

```json
{"country":"ru","fields":{"organization":"ORG-DEMO","service":"demo-001"}}
```

The response contains `mode: "demo"`, `country: "ru"`, and `receipt: "DEMO-…"`. Equivalent requests with the same country and trimmed values return the same receipt regardless of field order. Demo receipts are local and carry no official application status.

## Bell feed

Pass each feed as `--feed <file>`. Core accepts at most one feed for each loaded country plugin with `bell: true`. The JSON envelope contains integer `schema: 1`, a matching `country`, string `organization`, `environment: "demo"`, and an `items` array. Each item has string `id`, `subject`, and `received_at`. Core reads the configured file on each feed request. The [Bell importer](https://github.com/yellow444/govapi-bell#feed-contract) creates this format and checks the archive context.

Use a structured ID or status from an official adapter to associate a notification with an application in a future integration. Country, organization, environment, and employee role determine the effective context for live operations.

[Quick start](README.md#quick-start)
