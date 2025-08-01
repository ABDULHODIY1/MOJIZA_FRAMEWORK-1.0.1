import os
import logging
from functools import partial


logger = logging.getLogger(__name__)

import os
import mimetypes
from urllib.parse import unquote

def serve_static_file(request):
    """
    Static fayllar (rasm, video, pdf, css, js va hokazo) uchun universal view.
    """
    # URL’dan /static/ ni olib tashlaymiz va fayl yo‘lini olamiz
    rel_path = unquote(request.path[len("/static/"):])
    # Fayl tizimidagi haqiqiy joyga qo‘shamiz
    base = os.path.abspath("STATIC")
    file_path = os.path.abspath(os.path.join(base, rel_path))

    # Xavfsizlik: STATIC papkasi tashqarisiga chiqmasin
    if not file_path.startswith(base):
        return 403, "text/plain", b"Forbidden"

    # Papkalar roʻyxatini bermaymiz
    if os.path.isdir(file_path):
        return 403, "text/plain", b"Directory listing forbidden"

    if not os.path.exists(file_path):
        return 404, "text/plain", b"File not found"

    # MIME turini aniqlaymiz
    content_type, _ = mimetypes.guess_type(file_path)
    if content_type is None:
        content_type = "application/octet-stream"

    # Faylni o‘qiymiz
    with open(file_path, "rb") as f:
        data = f.read()

    return 200, content_type, data
# server.py ga tepadan import qiling
import threading

# Thread-local storage
_request_ctx = threading.local()

def get_current_request():
    return getattr(_request_ctx, "request", None)

def Static(filename: str) -> str:
    """
    To'liq static URL hosil qiluvchi helper.
    Foydalanish: Static("mojiza.png") -> "http://site.com/static/mojiza.png"
    """
    req = get_current_request()
    if req:
        # Host header olamiz
        host = req.headers.get("Host", "localhost")
        # Schema: oddiy qilib http, kerak bo'lsa https qo'shing
        return f"http://{host}/static/{filename}"
    # Fallback: faqat relative yo‘l
    return f"/static/{filename}"


def load_static_routes(router, static_root="STATIC"):
    print(f"[DEBUG] Static root: {static_root}")
    for dirpath, _, filenames in os.walk(static_root):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            print(f"[DEBUG] Found static file: {full_path}")

            rel_path = os.path.relpath(full_path, static_root)
            route_path = "/static/" + rel_path.replace("\\", "/")

            print(f"[DEBUG] Adding route: {route_path}")
            handler = partial(serve_static_file, rel_path)
            router.add_route(route_path, handler)



