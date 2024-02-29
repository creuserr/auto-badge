from http.server import BaseHTTPRequestHandler
from urllib.parse import quote
import requests
import json

class handler(BaseHTTPRequestHandler):
  def do_GET(self):