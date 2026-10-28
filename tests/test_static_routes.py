import http.client
import threading
from http.server import HTTPServer
from types import SimpleNamespace

import pytest

from MOJIZA.engine.routing import Router, add_static_routes, resolve_static_path
import MOJIZA.engine.routing as routing
from MOJIZA.static.make_static import serve_static_file


@pytest.fixture
def static_server(tmp_path, monkeypatch):
    """Serve <tmp>/site/STATIC with a secret file placed outside of it."""
    site = tmp_path / "site"
    (site / "STATIC" / "css").mkdir(parents=True)
    (site / "STATIC" / "logo.png").write_bytes(b"png-bytes")
    (site / "STATIC" / "css" / "app.css").write_text("body{}")
    (tmp_path / "secret.txt").write_text("TOP-SECRET")
    monkeypatch.chdir(site)

    router = Router()
    add_static_routes(router, static_url_path="/static", static_folder="STATIC")
    monkeypatch.setattr(routing, "router", router)

    from MOJIZA.engine.server import RequestHandler

    server = HTTPServer(("127.0.0.1", 0), RequestHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    def get(path):
        conn = http.client.HTTPConnection("127.0.0.1", server.server_address[1], timeout=5)
        conn.request("GET", path)
        resp = conn.getresponse()
        return resp.status, resp.getheader("Content-Type"), resp.read()

    yield get
    server.shutdown()
    server.server_close()


def test_serves_files_inside_static(static_server):
    assert static_server("/static/logo.png") == (200, "image/png", b"png-bytes")
    status, content_type, body = static_server("/static/css/app.css")
    assert (status, content_type, body) == (200, "text/css", b"body{}")


@pytest.mark.parametrize("path", [
    "/static/../../secret.txt",
    "/static/..%2f..%2fsecret.txt",
    "/static/%2e%2e/%2e%2e/secret.txt",
    "/static/css/../../../secret.txt",
])
def test_blocks_path_traversal(static_server, path):
    status, _, body = static_server(path)
    assert status == 403
    assert b"TOP-SECRET" not in body


@pytest.mark.parametrize("path", ["/static/logo.png%00", "/static/%00logo.png"])
def test_blocks_null_byte_paths(static_server, path):
    status, _, body = static_server(path)
    assert status == 403
    assert body == b"Forbidden"


@pytest.mark.parametrize("path", ["/static/logo.png%00", "/static/%00logo.png"])
def test_legacy_static_handler_blocks_null_byte_paths(tmp_path, monkeypatch, path):
    (tmp_path / "STATIC").mkdir()
    (tmp_path / "STATIC" / "logo.png").write_bytes(b"png-bytes")
    monkeypatch.chdir(tmp_path)

    assert serve_static_file(SimpleNamespace(path=path)) == (
        403, "text/plain", b"Forbidden"
    )


def test_missing_file_and_directory(static_server):
    assert static_server("/static/nope.png")[0] == 404
    assert static_server("/static/css")[0] == 403


def test_resolve_static_path_rejects_sibling_prefix(tmp_path):
    (tmp_path / "STATIC").mkdir()
    (tmp_path / "STATIC_private").mkdir()
    root = str(tmp_path / "STATIC")
    assert resolve_static_path(root, "a.png") == str((tmp_path / "STATIC" / "a.png").resolve())
    assert resolve_static_path(root, "../STATIC_private/key") is None
