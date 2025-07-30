# runer.py
import argparse
from MOJIZA.engine.server import run_server
from MOJIZA.engine.routing import load_app_routes, router
from MOJIZA.engine.p_gen import create_project_structure
from MOJIZA.engine.server import get_generated_apps
from version import __VERSION__

DEFAULT_NAME = "config"


def main():
    parser = argparse.ArgumentParser(description="MOJIZA Framework Boshqaruv Paneli")

    parser.add_argument("command", nargs="?", help="commands: run_script | generate")
    parser.add_argument("--port", type=int, default=8000, help="Server qaysi portda ishlasin? Default=8000")
    parser.add_argument("--v", action="store_true", help="Show framework version")
    parser.add_argument("-n", "--name", type=str, default=DEFAULT_NAME, help="Yangi loyiha nomi (generate bilan)")

    args = parser.parse_args()

    # Versiyani ko‘rsatish
    if args.v:
        print(f"🌟 MOJIZA Framework version: {__VERSION__}")
        return

    # Komandani bajarish
    if args.command == "run_script":
        # 🔍 Avtomatik app topish
        apps = get_generated_apps()
        if apps:
            print(f"INFO:MOJIZA: apps: {', '.join(apps)}")
        else:
            print("INFO:MOJIZA: apps: No generated apps found.")

        # 🔁 Routingni avtomatik yuklash
        routes = load_app_routes(".")
        for route in routes:
            print(f"Route added: {route['base_url']} -> {route['app_name']} (namespace: {route['space_name']})")

        print("Server started on http://localhost:8000")
        print("Available routes:")
        for r in router.routes:
            print(f" -> {r.route}")
        run_server(port=args.port)

    elif args.command == "generate":
        create_project_structure(args.name)

    elif args.command:
        print(f"⚠️ Noma'lum komanda: '{args.command}'")
        print("✅ Foydalanish:\n  python3 runer.py run_script\n  python3 runer.py generate -n yourproject")

    else:
        print("ℹ️ Komanda kiriting. Masalan: `--v`, `run_script`, yoki `generate`")


if __name__ == "__main__":
    main()
