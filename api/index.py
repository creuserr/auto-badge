from http.server import BaseHTTPRequestHandler
import requests
import json

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    path = self.path.split('/')
    req = requests.get('https://creprox.vercel.app/https:/api.github.com/repos/' + '/'.join(path[1:]))
    req = json.loads(req.text)
    url = 'https://img.shields.io/badge/'
    if path[0] == 'star':
      url += f'stargazers-{req["stargazers_count"]}-yellow'
    elif path[0] == 'watch':
      url += f'watchers-{req["watchers_count"]}-violet'
    elif path[0] == 'sub':
      url += f'subscribers-{req["subscribers_count"]}-peach'
    else:
      url += f'400 Bad Request-Invalid method-lightred'
    self.send_response(302)
    self.send_header('Location', url)
    self.end_headers()
    self.wfile.write(req.encode('utf-8'))