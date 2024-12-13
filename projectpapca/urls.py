# projectpapca/urls.py

from MOJIZA.engine.routing import PAGE
from projectpapca.views import fullpage

def register_routes():
    @PAGE('/')
    def home_view():
        return fullpage()

    # Yana boshqa sahifalarni shu yerga qo'shing
