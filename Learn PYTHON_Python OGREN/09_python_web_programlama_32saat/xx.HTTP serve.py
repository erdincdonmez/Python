import http.server
import socketserver

PORT = 8000
DIRECTORY = "E:\aErdinc\IS\Projeler\CALISILANDenemeDersOrnek\Python\PYTHON Projects\PythonWebYayin"

def handler_from(directory):
    def _init(self, *args, **kwargs):
        return http.server.SimpleHTTPRequestHandler.__init__(self, *args, directory=self.directory, **kwargs)
    return type(f'HandlerFrom<{directory}>',
                (http.server.SimpleHTTPRequestHandler,),
                {'__init__': _init, 'directory': directory})


with socketserver.TCPServer(("", PORT), handler_from("web")) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()