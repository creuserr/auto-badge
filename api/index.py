from http.server import BaseHTTPRequestHandler
import requests
import json

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    req = requests.get('https://creprox.vercel.app/https:/api.github.com/repos/' + self.path[1:])
    req = json.loads(req.text)
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(req.encode('utf-8'))