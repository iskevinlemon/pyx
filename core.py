import http.server
import socketserver
import os

def pyx_start_server(port):
    
    # Path to the 'views' folder
    views_dir = os.path.join(os.path.dirname(__file__), 'views')

    # Create a custom handler to specify the directory and handle the root path
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=views_dir, **kwargs)

        def do_GET(self):
            # Handle requests to the root path by serving index.html
            if self.path == '/':
                self.path = '/index.html'
            return super().do_GET()

    # Use socketserver to set up the server with the custom handler
    with socketserver.TCPServer(("", port), CustomHandler) as httpd:

        # Logging message
        print(f"Server running on port {port}")

        # Start the server
        httpd.serve_forever()
