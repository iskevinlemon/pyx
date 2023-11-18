# Overview of pyx
pyx (Python eXtra) is a Python web framework that aims to make web development much simpler.

# Running locally
Clone this repo and run <code>main.py</code>.<br/>
Visit <code>localhost:3000</code>

# pyx project structure
<pre>
pyx_project
├── lib              # library for pyx
│  ├── core.py       # core functions for pyx
└── views            # folder for all your HTML pages
│   ├── index.html   # default page
│   ├── error.html   # error 404 page
├── main.py          # app controller/ logic
</pre>

# Simple pyx app
```py
# main.py

from core import start_server

port = 3000

# Specify the data as dictionary
data = {
    "fruit": "apple",
    "car": "toyota",
    "error_message": "The page you have requested cannot be found"
}

# Start the server with the specified port and pass in the data dictionary
start_server(port, data)
```

```html
<!-- error.html-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error 404</h1>
    <!-- error message from main.py -->
    <h1>{error_message}</h1>
</body>
</html>
```
