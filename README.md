# GovAPI Core

GovAPI Core provides the shared local interface for GovAPI Hub. It shows connected country plugins, connection guides, source links, and the result of a demo application. The HTTP server listens on loopback. Demo requests are processed locally.

```powershell
python .\serve.py --plugin .\plugins\ru.json --plugin .\plugins\kz.json --plugin .\plugins\de.json
```

Requirements: Python 3.11 or later. Open <http://127.0.0.1:8765>.

To add a country, create a manifest using the [plugin contract](PLUGIN_CONTRACT.md) and pass it as another `--plugin` argument. The manifest ID identifies the country guide, the demo form, and Bell availability.

Use `--feed` to connect a synthetic Bell feed. The public distribution is intended for one local operator. The bundled manifests provide guides and demo forms. Live adapters and access to official TEST and PROD environments are evaluated service by service.

The [country directory](docs/countries/README.md) documents government APIs, access conditions, use cases for Core and Bell, and open-source alternatives.

Core follows the approach pioneered by [EPGU](https://github.com/yellow444/epgu) and has its own code and release cycle.
