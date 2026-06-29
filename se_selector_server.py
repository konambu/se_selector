from __future__ import annotations

import argparse
import contextlib
import os
import socket
import threading
import webbrowser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


APP_DIR = Path(__file__).resolve().parent
DEFAULT_PORT = 8765


def find_open_port(host: str, start_port: int) -> int:
    port = start_port
    while port < start_port + 100:
        with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            if sock.connect_ex((host, port)) != 0:
                return port
        port += 1
    raise RuntimeError("No open port found in scan range.")


def build_server(host: str, port: int) -> ThreadingHTTPServer:
    handler = partial(SimpleHTTPRequestHandler, directory=str(APP_DIR))
    return ThreadingHTTPServer((host, port), handler)


def main() -> int:
    parser = argparse.ArgumentParser(description="Local server for the SE Selector tool.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()

    port = find_open_port(args.host, args.port)
    server = build_server(args.host, port)
    url = f"http://{args.host}:{port}/se_selector.html"

    print(f"[se_selector] Serving {APP_DIR}")
    print(f"[se_selector] Open {url}")
    print("[se_selector] Press Ctrl+C to stop.")

    if not args.no_browser:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[se_selector] Stopping...")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
