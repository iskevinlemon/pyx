# main.py

from lib.core import start_server

port = 3000

# Specify the data as dictionary
data = {
    # Custom defined data
    "page_title": "Welcome to pyx",
    "fruit": "apple",
    "car": "toyota",

    # Error pages
    "not_found_error_message": "The page you have requested cannot be found",
    "forbidden_error_message": "You do not have permission to access this page"
}

# Start the server with the specified port and pass in the data dictionary
start_server(port, data)