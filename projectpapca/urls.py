from MOJIZA.engine.routing import PAGE
from MOJIZA.engine.server import HTML
from projectpapca.views import fullpage, newpage, login_view, guess_number_page,project_home, mojiza_mtml_documentation

base_urls = "/"  # localhost:8000/papca
space_name = "home"


@PAGE('/')
def home_view(method, params):
    return fullpage()

@PAGE('/forpage')
def new_page_view(method, params):
    return newpage()

@PAGE('/home')
def login(method, params):
    return login_view()

@PAGE('/GAME')
def guess_number(method, params):
    return guess_number_page(method, params)

@PAGE("/fullpage")
def hame_s(method, params):
    return project_home()

@PAGE('/doc')
def doc(method, params):
    return mojiza_mtml_documentation()


