from http.server import BaseHTTPRequestHandler
#import requests
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
          url += f'Stargazers-{req["stargazers_count"]}-B8B800'
        # watchers
        elif path[0] == 'watch':
          url += f'Watchers-{req["watchers_count"]}-00A4FF'
        # subscribers
        elif path[0] == 'sub':
          url += f'Subscribers-{req["subscribers_count"]}-DF6EFF'
        # forks
        elif path[0] == 'fork':
          url += f'Forks-{req["forks_count"]}-979797'
        # open issues
        elif path[0] == 'issue':
          url += f'Open Issues-{req["forks_count"]}-008A3D'
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
    
  def format_count(i):
    i = str(i)
    s = ""
    c = 0
    p = len(i) - 1
    for x in range(len(i)):
      px = p - x
      if c == 3:
        c = 1
        s = i[px] + ',' + s
      else:
        c += 1
        s = i[px] + s
    return s[:len(s) - 1] if s.endswith(',') else s

print(handler.format_count(827372))


277_277_232 - 277m
1_262 - 1k
82 - 82
123_456_789_123 - 123b