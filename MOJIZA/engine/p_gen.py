import os

def create_project_structure(name):
    os.makedirs(f"{name}/STATIC", exist_ok=True)

    with open(f"{name}/__init__.py", "w") as f:
        f.write("from . import models\nfrom . import views\nfrom . import settings\n")

    with open(f"{name}/models.py", "w") as f:
        f.write(
            "from MOJIZA.models.base import Model, Field\n\n"
            "class User(Model):\n"
            "    username = Field('string')\n"
            "    email = Field('string')\n"
            "    password = Field('string')\n"
        )

    with open(f"{name}/settings.py", "w") as f:
        f.write(
            "from MOJIZA.static import *\n"
            "from MOJIZA.static.make_static import Static\n\n"
            "DEBUG = True\n"
            "ALLOWED_HOSTS = ['localhost', '127.0.0.1']\n"
            "STATIC = Static(\"STATIC\")\n"
            "print(STATIC)\n"
        )

    with open(f"{name}/urls.py", "w") as f:
        f.write(
            "from MOJIZA.engine.routing import PAGE\n"
            "from .views import project_view\n"
           )

    with open(f"{name}/views.py", "w") as f:
        f.write("from MOJIZA.engine.server import HTML\n")
        f.write("# Views will be written manually\n")

    print(f"✅ Project '{name}' created successfully.")

