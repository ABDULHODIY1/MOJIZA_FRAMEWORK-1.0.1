# MOJIZA/engine/routing.py

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Route:
    def __init__(self, route, view):
        """
        Route obyektini yaratish.
        :param route: URL yo'nalishi (masalan, '/', '/hello')
        :param view: View funksiyasi
        """
        self.route = route
        self.view = view

class Router:
    def __init__(self):
        self.routes = []

    def add_route(self, route, view):
        """
        Route qo'shish.
        :param route: URL yo'nalishi
        :param view: View funksiyasi
        """
        self.routes.append(Route(route, view))
        logger.info(f"Route added: {route} -> {view.__name__}")

    def get_view(self, path):
        """
        URL yo'nalishiga mos view funksiyasini topish.
        :param path: URL yo'nalishi
        :return: View funksiyasi yoki None
        """
        for route in self.routes:
            if route.route == path:
                return route.view
        return None

# Router obyektini yaratish
router = Router()

def PAGE(route):
    """
    PAGE dekoratori routing tizimiga sahifa qo'shish uchun.
    :param route: URL yo'nalishi (masalan, '/', '/hello')
    """
    def decorator(view_func):
        router.add_route(route, view_func)
        return view_func
    return decorator
