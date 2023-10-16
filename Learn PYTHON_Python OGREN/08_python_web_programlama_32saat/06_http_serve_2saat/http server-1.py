"""
# https://docs.python.org/3.4/library/http.server.html
# https://www.mshowto.org/python-web-server-nasil-olusturulur.html
def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
"""

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
"""
python -m http.server 8000
python -m http.server 8000 --bind 127.0.0.1
python -m http.server --cgi 8000
"""
