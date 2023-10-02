import http.server as ws
class istekisleyici(ws.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_handler("content-type","html")
        self.end_handlers()
        self.write("Pytgon ile deneme web".encode())
def main():
    PORT=7000
    httpd = ws.HTTPServer(('',PORT),istekisleyici)
    httpd.serve_forever()
if __name__=="__main__":
    main()
