from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json

def controller(data):
    print(data)


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
    
    def do_GET(self):
        self._set_headers()
        print("GET REQUEST PERFORMED")

    def do_POST(self):
        #doesn't do anything with posted data
        self._set_headers()
        #Get the content length so we know how much data to read.
        content_length = int(self.headers['Content-Length'])
        #Read the post data
        post_data = self.rfile.read(content_length).decode("utf-8")
        controller(post_data)

def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()