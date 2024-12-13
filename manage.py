# manage.py

import argparse
from MOJIZA.engine.server import run_server
from projectpapca.urls import register_routes

def main():
    parser = argparse.ArgumentParser(description='MOJIZA Framework Management')
    parser.add_argument('command', help='Command to run (runserver)')
    parser.add_argument('--port', type=int, default=8000, help='Port number to run the server on')

    args = parser.parse_args()

    if args.command == 'runserver':
        # Routing yo'nalishlarini ro'yxatdan o'tkazish
        register_routes()
        run_server(port=args.port)
    else:
        print(f"Unknown command: {args.command}")

if __name__ == "__main__":
    main()
