import os
from http.server import HTTPServer, CGIHTTPRequestHandler
# Ensure that the server is created in a directory that we know is safe to expose
os.chdir('/home/brian/test-server')
# Create server object listening the port 80
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
# Start the web server
server_object.serve_forever()
