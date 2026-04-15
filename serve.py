"""
Start a local HTTP server to view the project website.
Run from the project root: python serve.py
Then open: http://localhost:8000/website/
"""
import http.server, socketserver, webbrowser, os, threading

PORT = 8000
URL = f"http://localhost:{PORT}/website/"

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def open_browser():
 import time; time.sleep(1)
 webbrowser.open(URL)

threading.Thread(target=open_browser, daemon=True).start()

print(f"Serving at {URL}")
print("Press Ctrl+C to stop.\n")

# Allow reuse of the address to avoid "Address already in use" errors
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
 httpd.serve_forever()
