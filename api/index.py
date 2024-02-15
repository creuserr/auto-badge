from http.server import BaseHTTPRequestHandler
import requests
import json

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    url = 'https://img.shields.io/badge/'
    path = self.path[1:].split('/')
    try: 
      req = requests.get('https://creprox.vercel.app/https:/api.github.com/repos/' + '/'.join(path[1:]))
      req = json.loads(req.text)
      if path[0] == 'star':
        url += f'stargazers-{req["stargazers_count"]}-D8BA00'
      elif path[0] == 'watch':
        url += f'watchers-{req["watchers_count"]}-00A4FF'
      elif path[0] == 'sub':
        url += f'subscribers-{req["subscribers_count"]}-DF6EFF'
      else:
        url += f'400 Bad Request-Invalid method-FF5353'
    except:
      if len(path) != 3:
        url += f'400 Bad Request-FF5353'
      else:
        url += f'500 Internal Error-FF2D2D'
    self.send_response(302)
    self.send_header('Location', url)
    self.end_headers()