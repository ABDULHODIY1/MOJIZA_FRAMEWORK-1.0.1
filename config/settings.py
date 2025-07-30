from MOJIZA.static import *
from MOJIZA.static.make_static import Static

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
STATIC = Static("STATIC")
print(STATIC)
