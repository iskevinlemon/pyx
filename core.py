import http.server
import socketserver
import os

# Default port at 3000
PORT = 8000

# Path to the 'views' folder
views_dir = os.path.join(os.path.dirname(__file__), 'views')

# Custom handler to specify the directory and handle the root path
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=views_dir, **kwargs)

    def do_GET(self):
        # Requests to the root path by serving index.html
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

# Socketserver to set up the server with the custom handler
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")

    # Start the server
    httpd.serve_forever()
