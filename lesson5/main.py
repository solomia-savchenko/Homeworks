from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/': # http://localhost:8080/
            self.send_response(200) #
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as html:
                self.wfile.write(html.read())
        elif self.path == '/about':
            self.send_response(200)  #
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('about.html', 'rb') as html:
                self.wfile.write(html.read())
        elif self.path.startswith('/assets/css/'):
            css_file_path = self.path[1:]

            if os.path.exists(css_file_path):
                self.send_response(200)
                self.send_header('Content-type', 'text/css')
                self.end_headers()
                with open(css_file_path, 'rb') as css_file:
                    self.wfile.write(css_file.read())
            else:
                self.send_response(404)
                self.end_headers()
        elif self.path.startswith('/assets/js/'):
            js_file_path = self.path[1:]

            if os.path.exists(js_file_path):
                self.send_response(200)
                self.send_header('Content-type', 'text/javascript')
                self.end_headers()
                with open(js_file_path, 'rb') as js_file:
                    self.wfile.write(js_file.read())
            else:
                self.send_response(404)
                self.end_headers()
        elif self.path.startswith('/assets/images/'):
            image_file_path = self.path[1:]

            if os.path.exists(image_file_path):
                self.send_response(200)
                self.send_header('Content-type', 'image/webp')
                self.end_headers()
                with open(image_file_path, 'rb') as image_file:
                    self.wfile.write(image_file.read())
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def do_POST(self):
        print(f'POST: {self.path}')
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            print(f'POST: {body}')

            data = json.loads(
                body.decode()
            )

            print(f'POST: {data}')

            name = data['name']
            comment = data['comment']
            print(f'POST: {name}, {comment}')

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'approved'}).encode())

server = HTTPServer(
    ('localhost', 8080),
    Handler
)

print('Server started http://localhost:8080')

server.serve_forever()