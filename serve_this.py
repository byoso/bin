#! /usr/bin/env python3

import os
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler
import argparse

parser = argparse.ArgumentParser(description='Serve the current directory.')
parser.add_argument('-p', '--port', type=int, default=8000,
                    help='port to serve on (default: 8000)')

DIR = os.getcwd()
PORT = parser.parse_args().port

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


if __name__ == "__main__":
    IP = get_ip()
    print(f"Serving at http://{IP}:{PORT}")
    try:
        HTTPServer((IP, PORT), SimpleHTTPRequestHandler).serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
