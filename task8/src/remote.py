from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # def __init__(self):
    mode = 'play'

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')
        self.wfile.write(bytes(SimpleHTTPRequestHandler.mode, 'utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')

        cmd = json.loads(body.decode('utf-8'))

        response.write(bytes(cmd["mode"], 'utf-8'))

        if cmd["mode"] == 'play' or cmd["mode"] == 'pause':
            SimpleHTTPRequestHandler.mode = cmd["mode"]

        # print(response.getvalue())
        print("got POST req")
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)

httpd.serve_forever()

# print("server init")
# res = bytes(test_string, 'utf-8')
# string = bytesObj.decode('utf-8')