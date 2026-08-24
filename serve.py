#!/usr/bin/env python3
"""Serve the studio tools locally.

The tools are single-file HTML and mostly run straight from the filesystem,
but a few use fetch() for their presets, which browsers block on file:// URLs.
Serving over http fixes that.

    python3 serve.py        then open http://localhost:4602
"""
import http.server, socketserver, webbrowser, os

PORT = 4602  # change if taken
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Studio tools → http://localhost:{PORT}  (ctrl-c to stop)")
    webbrowser.open(f"http://localhost:{PORT}")
    httpd.serve_forever()
