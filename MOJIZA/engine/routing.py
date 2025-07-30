import logging
import importlib.util
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MOJIZA.engine.routing")


class Route:
    def __init__(self, route, view):
        self.route = route
        self.view = view


class Router:
    def __init__(self):
        self.routes = []

    def add_route(self, route, view):
        self.routes.append(Route(route, view))
        logger.info(f"Route added: {route} -> {view.__name__}")

    def get_view(self, path):
        for route in self.routes:
            if route.route == path:
                return route.view
        return None


# Router instance
router = Router()


def PAGE(route):
    """
    PAGE dekoratori routing tizimiga sahifa qo'shish uchun.
    """
    def decorator(view_func):
        # __route__ markerini qo‘yamiz (load_app_routes uchun)
        view_func.__route__ = route
        return view_func
    return decorator

def load_app_routes(project_root):
    routes = []

    exclude_dirs = {'.venv', '__pycache__', 'site-packages', '.git'}

    for root, dirs, files in os.walk(project_root):
        # 🔥 .venv yoki site-packages ni o'tkazib yuboramiz
        if any(exclude in root for exclude in exclude_dirs):
            continue

        if 'urls.py' in files:
            app_urls_path = os.path.join(root, 'urls.py')
            app_name = os.path.basename(root)

            try:
                spec = importlib.util.spec_from_file_location(f"{app_name}.urls", app_urls_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                base_url = getattr(module, "base_urls", "")
                space_name = getattr(module, "space_name", "")

                if hasattr(module, "register_routes"):
                    module.register_routes()

                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if callable(attr) and hasattr(attr, "__route__"):
                        route_path = attr.__route__

                        if base_url.endswith("/") and route_path.startswith("/"):
                            full_path = base_url[:-1] + route_path
                        elif not base_url.endswith("/") and not route_path.startswith("/"):
                            full_path = base_url + "/" + route_path
                        else:
                            full_path = base_url + route_path

                        full_path = full_path.replace("\\", "/")
                        router.add_route(full_path, attr)

                routes.append({
                    "app_name": app_name,
                    "base_url": base_url,
                    "space_name": space_name or ""
                })
            except Exception as e:
                logger.warning(f"❌ Failed to load {app_urls_path}: {e}")

    return routes
