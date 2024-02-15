from http.server import BaseHTTPRequestHandler
import requests
import json

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    path = self.path.split('/')
    req = requests.get('https://creprox.vercel.app/https:/api.github.com/repos/' + '/'.join(path[1:]))
    req = json.loads(req.text)
    url = 'https://img.shields.io/badge/'
    if path[0] == 'stars':
      url += f'stars-{req["stargazers_count"]}-yellow'
    elif path[0] == 'watchers':
      url += f'stars-{req["starga_count"]}-yellow'
    self.send_response(302)
    self.send_header('Location', '')
    self.end_headers()
    self.wfile.write(req.encode('utf-8'))