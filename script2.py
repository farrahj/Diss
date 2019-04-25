from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json
import sys

USERNAME = "james"
PASSWORD = "testingPassword"

def capitalLetter(password):
    #Do checks for capital
    #if there is a capital, return False
    
    #return True (if it doesnt satisfy this function)

def bruteforce(password, main):
    flag = 0
    print("ENTERED PASSWORD: " + password)
    if (capitalLetter(password) == True):
        flag += 1
    if ....
        flag += 1

    





def controller(data, main):
    # try:
    data = json.loads(data)
    if ("username" in data and "password" in data):
        if (data["username"] == USERNAME):
            if (data["password"] == PASSWORD):
                main._set_response(200, "correct information")
            else:
                print("BRUTEFORCE CHECK")
                bruteforce(data["password"], main)
        else:
            main._set_response(403, "invalid credentials")
    else:
        main._set_response(400, "JSON must include a username and password")
    # except:
    #     main._set_response(400, "invalid data")

class S(BaseHTTPRequestHandler):
    def _set_response(self, code = 200, message = ""):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        json_message = json.dumps({'message': message}).encode()
        self.wfile.write(json_message)
    
    def do_GET(self):
        self._set_response(404, "route not found")

    def do_POST(self):
        if (self.headers['Content-Length'] != None):
            content_length = int(self.headers['Content-Length'])
        else:
            self._set_response(400, "JSON must include a username and password")
        #Read the post data
        post_data = self.rfile.read(content_length).decode("utf-8")
        controller(post_data, self)

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


# curl -i -X POST 127.0.0.1:8080 -d '{"username": "james", "password": "testingPasord"}'