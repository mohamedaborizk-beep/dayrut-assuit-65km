import os, sys, json, subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler

sys.stdout.reconfigure(encoding='utf-8')
PORT = 8080
APP_DIR = os.path.dirname(os.path.abspath(__file__))

class ProjectAppHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=APP_DIR, **kwargs)

    def do_POST(self):
        if self.path == '/api/refresh-data':
            try:
                # Run extraction script
                scratch_script = os.path.join(APP_DIR, '..', '..', '..', '..', '..', '..', 'Users', 'user', '.gemini', 'antigravity', 'brain', '5dc9d524-e02e-44cc-9ba3-083f32e7ff79', 'scratch', 'extract_all_dashboard_data.py')
                if os.path.exists(scratch_script):
                    subprocess.run([sys.executable, scratch_script], check=True)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'success'}).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'error', 'message': str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server_address = ('0.0.0.0', PORT)
    httpd = HTTPServer(server_address, ProjectAppHandler)
    print(f"Server started at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")
