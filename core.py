import http.server
import socketserver
import os
import webbrowser

# Function to bind values to HTML
def bind_to_html(html_content, **kwargs):
    for key, value in kwargs.items():

        # templating with {variable}
        html_content = html_content.replace(f"{{{key}}}", str(value))

        # templating with @{variable}
        # html_content = html_content.replace(f"@{{{key}}}", str(value))

    return html_content

def start_server(port, data):
    # Path to the 'views' folder
    views_dir = os.path.join(os.path.dirname(__file__), 'views')

    # Create a custom handler to specify the directory and handle the root path
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=views_dir, **kwargs)

        def do_GET(self):
            # If it's a request for a file, serve it using the default handler
            if '.' in self.path:
                return super().do_GET()

            # Handle requests to the root path by serving index.html
            if self.path == '/':
                self.path = '/index.html'

                # Read the content of index.html
                with open(os.path.join(views_dir, 'index.html'), 'r') as file:
                    html_content = file.read()

                # Replace placeholders with data values
                content = bind_to_html(html_content, **data)

                # Override the default do_GET to include dynamic content
                self.send_response(200)
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))

            # TODO: implement custom routing
            
            # TODO: implement forbidden pages and etc... 
            
            # Error page
            else:

                # Read the content of error.html
                with open(os.path.join(views_dir, 'error.html'), 'r') as file:
                    html_content = file.read()

                # Replace placeholders with data values (if needed for custom error message)
                content = bind_to_html(html_content, **data)
            
                self.send_response(404)
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))

    # Use socketserver to set up the server with the custom handler
    with socketserver.TCPServer(("", port), CustomHandler) as httpd:
        # Logging message
        print(f"Server running on port {port}")

        # Start the server
        httpd.serve_forever()

        # No need for this as default view is / route (views/index.html)
        # webbrowser.open_new('views/index.index.html')
