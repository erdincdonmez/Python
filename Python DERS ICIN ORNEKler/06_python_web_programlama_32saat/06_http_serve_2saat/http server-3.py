def handler_from(directory):
    def _init(self, *args, **kwargs):
        return http.server.SimpleHTTPRequestHandler.__init__(self, *args, directory=self.directory, **kwargs)
    return type(f'HandlerFrom<{directory}>',
                (http.server.SimpleHTTPRequestHandler,),
                {'__init__': _init, 'directory': directory})


with socketserver.TCPServer(("", PORT), handler_from("web")) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
