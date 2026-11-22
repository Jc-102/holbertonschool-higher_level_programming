#!/usr/bin/python3
"""A simple API built with Python's http.server module."""
import http.server
import json

PORT = 8000


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Handle GET requests for a few simple endpoints."""

    def _send(self, status, body, content_type="text/plain"):
        """Send a response with a status code, content type and body."""
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def do_GET(self):
        """Route GET requests to the matching endpoint."""
        if self.path == "/":
            self._send(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send(200, json.dumps(data), "application/json")
        elif self.path == "/status":
            self._send(200, "OK")
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._send(200, json.dumps(info), "application/json")
        else:
            self._send(404, "Endpoint not found")


if __name__ == "__main__":
    server = http.server.HTTPServer(("", PORT), SimpleAPIHandler)
    print("Serving on port {}".format(PORT))
    server.serve_forever()
