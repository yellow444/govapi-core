"""Serve the GovAPI Hub public workspace on loopback."""
import argparse
import hashlib
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
from urllib.parse import parse_qs, urlsplit

WEB = Path(__file__).resolve().parent / "web"
ASSETS = {
    "/": ("index.html", "text/html"),
    "/style.css": ("style.css", "text/css"),
    "/app.js": ("app.js", "text/javascript"),
}


def require(valid):
    if not valid:
        raise ValueError('Invalid manifest fields.')


def load_plugins(paths):
    plugins = {}
    for path in paths:
        try:
            profile = json.loads(path.read_text(encoding="utf-8-sig"))
            country = profile["id"]
            require(type(profile["schema"]) is int and profile["schema"] == 1)
            require(re.fullmatch(r"[a-z]{2}", country) and country not in plugins)
            require(all(isinstance(profile[key], str) and profile[key].strip()
                       for key in ("country", "platform", "summary")))
            require(type(profile["bell"]) is bool and profile["steps"] and profile["fields"])
            require(isinstance(profile["steps"], list) and isinstance(profile["fields"], dict))
            require(all(re.fullmatch(r"[a-z][a-z_]{0,39}", field) and
                       isinstance(label, str) and label.strip()
                       for field, label in profile["fields"].items()))
            for step in profile["steps"]:
                require(all(isinstance(step[key], str) and step[key].strip()
                           for key in ("title", "detail", "source", "url")))
                url = urlsplit(step["url"])
                require(url.scheme == "https" and url.hostname and not url.username)
        except (KeyError, TypeError, ValueError, OSError) as error:
            raise ValueError(f"Invalid or duplicate plugin: {path}") from error
        plugins[country] = profile
    return plugins


def demo_receipt(profile, fields):
    if not isinstance(fields, dict) or fields.keys() != profile["fields"].keys():
        raise ValueError("Fill in the demo scenario fields.")
    if any(not isinstance(value, str) or not 1 <= len(value.strip()) <= 120
           for value in fields.values()):
        raise ValueError("Each field must contain 1 to 120 characters.")
    canonical = json.dumps({key: value.strip() for key, value in fields.items()}, sort_keys=True)
    digest = hashlib.sha256(f"{profile['id']}:{canonical}".encode()).hexdigest()
    return {"mode": "demo", "country": profile["id"], "receipt": f"DEMO-{digest[:12].upper()}"}


class Handler(BaseHTTPRequestHandler):
    def respond(self, status, body, content_type):
        self.send_response(status)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'; object-src 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(body)

    def json_response(self, status, value):
        self.respond(status, json.dumps(value, ensure_ascii=False).encode(), "application/json")

    def check_host(self):
        port = self.server.server_port
        if self.headers.get("Host") not in {f"127.0.0.1:{port}", f"localhost:{port}"}:
            self.json_response(HTTPStatus.FORBIDDEN, {"error": "Open the local application address."})
            return False
        return True

    def do_GET(self):
        if not self.check_host():
            return
        url = urlsplit(self.path)
        if url.path in ASSETS:
            name, content_type = ASSETS[url.path]
            self.respond(HTTPStatus.OK, (WEB / name).read_bytes(), content_type)
        elif url.path == "/api/plugins":
            self.json_response(HTTPStatus.OK, list(self.server.plugins.values()))
        elif url.path == "/api/feed":
            country = parse_qs(url.query).get("country", [""])[0]
            profile = self.server.plugins.get(country)
            if not profile or not profile["bell"]:
                self.json_response(HTTPStatus.NOT_FOUND, {"error": "Notifications are unavailable for this country."})
                return
            path = self.server.feeds.get(country)
            try:
                feed = read_feed(path, country) if path else None
            except (OSError, ValueError, TypeError):
                self.json_response(HTTPStatus.SERVICE_UNAVAILABLE, {"error": "The demo feed is unavailable."})
                return
            self.json_response(HTTPStatus.OK, feed)
        else:
            self.json_response(HTTPStatus.NOT_FOUND, {"error": "Endpoint not found."})

    def do_POST(self):
        if not self.check_host():
            return
        if self.path != "/api/mock":
            self.json_response(HTTPStatus.NOT_FOUND, {"error": "Endpoint not found."})
            return
        origin = self.headers.get("Origin")
        if origin and origin != "http://" + self.headers["Host"]:
            self.json_response(HTTPStatus.FORBIDDEN, {"error": "The request came from a different origin."})
            return
        if self.headers.get_content_type() != "application/json":
            self.json_response(HTTPStatus.UNSUPPORTED_MEDIA_TYPE, {"error": "Expected JSON."})
            return
        try:
            size = int(self.headers.get("Content-Length", 0))
            if not 1 <= size <= 8192:
                raise ValueError("The request size must be 1 to 8192 bytes.")
            request = json.loads(self.rfile.read(size))
            profile = self.server.plugins[request["country"]]
            receipt = demo_receipt(profile, request.get("fields"))
        except (json.JSONDecodeError, UnicodeDecodeError, TypeError, KeyError, AttributeError):
            self.json_response(HTTPStatus.BAD_REQUEST, {"error": "Check the country and request structure."})
            return
        except ValueError as error:
            self.json_response(HTTPStatus.BAD_REQUEST, {"error": str(error)})
            return
        self.json_response(HTTPStatus.OK, receipt)


def read_feed(path, country):
    feed = json.loads(path.read_text(encoding="utf-8-sig"))
    if (not isinstance(feed, dict) or feed.get("country") != country or
            type(feed.get("schema")) is not int or feed["schema"] != 1 or
            feed.get("environment") != "demo" or
            not isinstance(feed.get("organization"), str) or
            not isinstance(feed.get("items"), list) or
            any(not isinstance(item, dict) or
                any(not isinstance(item.get(key), str) for key in ("id", "subject", "received_at"))
                for item in feed["items"])):
        raise ValueError(f"Invalid demo feed: {path}")
    return feed


def load_feeds(paths, plugins):
    feeds = {}
    for path in paths:
        # The file is configured by the operator and checked again on refresh.
        country = json.loads(path.read_text(encoding="utf-8-sig"))["country"]
        if country in feeds or not plugins.get(country, {}).get("bell"):
            raise ValueError(f"Unexpected or duplicate country in demo feed: {path}")
        read_feed(path, country)
        feeds[country] = path
    return feeds


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plugin", type=Path, action="append", default=[])
    parser.add_argument("--feed", type=Path, action="append", default=[])
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    try:
        plugins = load_plugins(args.plugin)
        feeds = load_feeds(args.feed, plugins)
        server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    except (OSError, TypeError, ValueError, KeyError) as error:
        parser.error(str(error))
    with server:
        server.plugins = plugins
        server.feeds = feeds
        print(f"GovAPI Hub · http://127.0.0.1:{server.server_port}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
