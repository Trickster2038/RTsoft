from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    mode = 'play'

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        msg_json = json.dumps({"mode": SimpleHTTPRequestHandler.mode})
        msg_bytes = bytes(msg_json, 'utf-8')
        self.wfile.write(msg_bytes)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'Post requests received')

        cmd = json.loads(body.decode('utf-8'))

        if cmd["mode"] == 'play' or cmd["mode"] == 'pause':
            SimpleHTTPRequestHandler.mode = cmd["mode"]

        print("got POST request")


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)

httpd.serve_forever()

# res = bytes(test_string, 'utf-8')
# string = bytesObj.decode('utf-8')