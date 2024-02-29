from http.server import BaseHTTPRequestHandler
from urllib.parse import quote
import requests, json

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    path = '/'.join(self.path[1:].split('/')[1:])
    req = requests.get('https://lyrist.vercel.app/api/' + path)
    res = json.loads(req.text)
    title = res['title']
    artist = res['artist']
    image = res['image']
    a = f'https://m.youtube.com/results?search_query={quote(title + " " + artist)}'
    st = '{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
    svg = f'<a href="{a}"><svg xmlns="http://www.w3.org/2000/svg" width="400" height="100"><style>@import url("https://fonts.googleapis.com/css2?family=Inter");.text{st}</style><defs><clipPath id="rounded-corner"><rect x="10" y="10" width="80" height="80" rx="3" ry="3"/></clipPath></defs><image href="{image}" x="10" y="10" width="80" height="80" clip-path="url(#rounded-corner)" /><text x="105" y="25" font-size="14" fill="lightgray" font-family="Inter" class="text">Listening to</text><text x="105" y="50" font-size="20" fill="black" font-family="Inter" class="text">{title}</text><text x="105" y="75" font-size="16" fill="gray" font-family="Inter" class="text">{artist}</text></svg></a>'
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Content-Type', 'image/svg+xml')
    self.end_headers()
    self.wfile.write(svg.encode('utf-8'))