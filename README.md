# GovAPI Core

GovAPI Core is the shared local interface for GovAPI Hub. It shows connected country plugins, connection guides, and demo application receipts. It can also display a synthetic feed exported by GovAPI Bell.

## Quick start

Use Git and Python 3.11 or later. The demo uses the Python standard library. Run the commands from a directory where you want to keep the clone.

```powershell
git clone https://github.com/yellow444/govapi-core.git
Set-Location govapi-core
python .\serve.py --plugin .\plugins\ru.json --plugin .\plugins\kz.json --plugin .\plugins\de.json
```

Open <http://127.0.0.1:8765>. Select **Russia**, **Kazakhstan**, or **Germany** to see its connection guide. In **Demo application**, enter sample values and select **Get receipt**. A successful result starts with `DEMO-`. The receipt is generated locally and does not submit an application to a government service.

To verify the API from a second PowerShell terminal:

```powershell
$base = 'http://127.0.0.1:8765'
(Invoke-RestMethod "$base/api/plugins").id
$body = '{"country":"ru","fields":{"organization":"ORG-DEMO","service":"demo-001"}}'
Invoke-RestMethod "$base/api/mock" -Method Post -ContentType 'application/json' -Body $body
```

The first command lists `ru`, `kz`, and `de`. The second returns `mode: demo`, `country: ru`, and a receipt ID. Stop the server with Ctrl+C. If the port is already in use, pass `--port 8766` and use that port in the URL.

## Add the Bell demo feed

Follow the [Bell quick start](https://github.com/yellow444/govapi-bell#quick-start) to clone Bell next to Core and create `feed.json`. Stop Core if it is already running, then restart it from the Core directory:

```powershell
python .\serve.py --plugin .\plugins\ru.json --plugin .\plugins\kz.json --plugin .\plugins\de.json --feed ..\govapi-bell\feed.json
```

Select **Russia** and look for two entries under **Notifications**. The bundled Kazakhstan and Germany plugins do not enable that section. Core reads demo feeds only, and it listens on loopback.

## Add a country plugin

Create a JSON manifest using the [country plugin contract](PLUGIN_CONTRACT.md). Pass it as a separate `--plugin` argument on startup. The manifest provides guide content and a demo form. Access to official environments and live adapters is evaluated per service.

[Country directory](docs/countries/README.md) · [Roadmap](docs/project/ROADMAP.md) · [Research](docs/project/RND.md) · [Workflow](docs/project/WORKFLOW.md)

Core follows the approach pioneered by [EPGU](https://github.com/yellow444/epgu) and has its own code and release cycle.
