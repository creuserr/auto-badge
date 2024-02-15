from http.server import BaseHTTPRequestHandler
import requests
import json

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    url = 'https://img.shields.io/badge/'
    path = self.path[1:].split('/')
    try: 
      req = requests.get('https://creprox.vercel.app/https:/api.github.com/repos/' + '/'.join(path[1:]))
      if 'Not Found' in req.text:
        url += f'404-{"%2F".join(path[1:])} not found-FF5353'
      else:
        req = json.loads(req.text)
        # stargazers
        if path[0] == 'star':
          url += f'Stargazers-{req["stargazers_count"]}-D8BA00'
        # watchers
        elif path[0] == 'watch':
          url += f'Watchers-{req["watchers_count"]}-00A4FF'
        # forks
        elif path[0] == 'fork':
          url += f'Forks-{req["forks_count"]}-4131FF'
        # issue
        elif path[0] == 'issue':
          url += f'Open Issues-{req["forks_count"]}-008A3D'
        # subscribers
        elif path[0] == 'sub':
          url += f'Subscribers-{req["subscribers_count"]}-DF6EFF'
        else:
          url += '400 Bad Request-Invalid method-FF5353'
    except:
      if len(path) != 3:
        url += '400 Bad Request-FF5353'
      else:
        url += '500 Internal Error-FF2D2D'
    self.send_response(302)
    self.send_header('Location', url)
    self.end_headers()