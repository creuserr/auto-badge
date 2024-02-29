from http.server import BaseHTTPRequestHandler
from urllib.parse import quote
import requests
import json

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    path = '/'.join(self.path[1:].split('/')[1:])
    req = requests.get('https://lyrist.vercel.app/api/' + path)
    res = json.loads(req.text)
    title = res['title']
    artist = res['artist']
    image = res['image']