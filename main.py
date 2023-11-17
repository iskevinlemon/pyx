from lib.core import start_server

port = 4000

# Specify the data as dictionary
data = {
    "fruit": "apple",
    "car": "toyota",
    "error_message": "The page you have requested cannot be found"
}

# Start the server with the specified port and pass in the data dictionary
start_server(port, data)