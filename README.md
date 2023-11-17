# Overview of pyx
pyx (Python eXtra) is a Python web framework that aims to make web development much simpler.

# Running locally
Clone this repo and run <code>core.py</code>.<br/>
Visit <code>localhost:3000</code>

# pyx project structure
.<b>views</b><br/>
..index.html<br/>
.<b>lib</b><br/>
..core.py<br/>
.main.py<br/>

# Simple pyx app
```py
# main.py

from core import start_server

port = 3000
start_server(port)
```