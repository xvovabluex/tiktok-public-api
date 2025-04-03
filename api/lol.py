import http.server
import requests
import urllib.parse

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        url = query_params.get("video", [None])[0]

        #elf.send_response(200)
        #self.send_header("Content-type", "text/html")
        #self.end_headers()
        
        self.wfile.write(bytes(requests.post(url).text, "utf-8"))

    def do_POST(self):
        parsed_url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        url = query_params.get("video", [None])[0]

        self.wfile.write(bytes(requests.post(url).text, "utf-8"))

handler = app = RequestHandler
