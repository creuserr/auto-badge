from http.server import BaseHTTPRequestHandler
import requests
import json

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    url = 'https://img.shields.io/badge/'
    path = self.path.split('/')
    try: 
      req = requests.get('https://creprox.vercel.app/https:/api.github.com/repos/' + '/'.join(path[1:]))
      req = json.loads(req.text)
      if path[0] == 'star':
      url += f'stargazers-{req["stargazers_count"]}-yellow'
      elif path[0] == 'watch':
        url += f'watchers-{req["watchers_count"]}-violet'
      elif path[0] == 'sub':
        url += f'subscribers-{req["subscribers_count"]}-peach'
      else:
        url += f'400 Bad Request-Invalid method-lightred'
    except:
      if len(path != 3):
        url += f'400 Bad Request-Invalid re-lightred'
      else:
        url += f'500 Internal Error-lightred'
    self.send_response(302)
    self.send_header('Location', url)
    self.end_headers()