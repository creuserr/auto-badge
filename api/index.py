from http.server import BaseHTTPRequestHandler
from urllib.parse import quote
import requests
import json

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    version = 3
    count = None
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
          count = req['stargazers_count']
          url += f'Stargazers-{self.fmtcount(count)}-B8B800'
        # watchers
        elif path[0] == 'watch':
          count = req['watchers_count']
          url += f'Watchers-{self.fmtcount(count)}-00A4FF'
        # subscribers
        elif path[0] == 'sub':
          count = req['subscribers_count']
          url += f'Subscribers-{self.fmtcount(count)}-DF6EFF'
        # forks
        elif path[0] == 'fork':
          count = req['forks_count']
          url += f'Forks-{self.fmtcount(count)}-979797'
        # open issues
        elif path[0] == 'issue':
          count = req['open_issues_count']
          url += f'Open Issues-{self.fmtcount(count)}-008A3D'
        else:
          url += '400 Bad Request-Invalid method-FF5353'
    except BaseException as e:
      if len(path) != 3:
        url += '400 Bad Request-FF5353'
      else:
        # for diagnosis
        if 'x-autobadge-diagnosis-dev' in self.path:
          url += f'{quote(str(e))}-FF2D2D'
        else:
          url += '500 Internal Error-FF2D2D'
    self.send_response(302)
    if count != None:
      self.send_header('X-Autobadge-Version', version)
      self.send_header('X-Autobadge-Method', path[0])
      self.send_header('X-Autobadge-User', path[1])
      self.send_header('X-Autobadge-Repo', path[2])
      self.send_header('X-Autobadge-Value', count)
    self.send_header('Location', url)
    self.end_headers()
    
  def fmtcount(self, i):
    i = str(i)
    if int(i) >= 1000000000:
      i = i[0:len(i) - 9]
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
      return (s[:len(s) - 1] if s.endswith(',') else s) + 'b'
    elif int(i) >= 1000000:
      return i[0:len(i) - 6] + 'm'
    elif int(i) >= 1000:
      return i[0:len(i) - 3] + 'k'
