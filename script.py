from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

    def do_POST(self):
	            #Get the content length so we know how much data to read.
        content_length = int(self.headers['Content-Length'])
                #Read the post data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
                #Print the data
        print(post_data)
                #Reply with a 200.
	    self.send_response(200)

httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()