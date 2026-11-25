# Country plugin contract v1

A plugin manifest is a JSON file passed explicitly on the command line. It contains `schema: 1`, a unique two-letter lowercase `id`, the country and platform names, a summary, connection steps with HTTPS source links, and labels for the demo form fields. The boolean `bell` enables the notifications section. See the examples in [plugins/](plugins/).

`GET /api/plugins` returns the connected manifests. `POST /api/mock` accepts a country ID in `country` and form values in `fields`. It returns a local receipt with `mode: demo`. Equivalent requests for a country produce the same demo receipt. The receipt does not represent the status of a live application.

`GET /api/feed?country=ru` reads a connected Bell JSON export. The version 1 envelope contains `country`, `organization`, `environment: demo`, and `items`. Each item has a message ID, subject, and source timestamp. Use a documented structured identifier or status from an official adapter to associate a notification with an application.

For a future official integration, the effective context is the country, organization, environment, and employee role. Keep credentials and account data in the adapter and the organization's authorized environment. Store only public reference material in the manifest.
