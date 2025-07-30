from MOJIZA.engine.routing import PAGE
from .views import homepage

base_urls = "/papca"  # localhost:8000/papca
space_name = "pic"



@PAGE('/test')
def project_url(method, params):
       return homepage()
