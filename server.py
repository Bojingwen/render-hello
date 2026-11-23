import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PAGE = """<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>jaketom0626</title></head>
<body style="font-family:sans-serif;text-align:center;margin-top:20vh">
<h1>jaketom0626</h1><p>Render 免费服务器 · 已上线</p></body></html>"""

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        body = PAGE.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *a):
        pass

HTTPServer(("0.0.0.0", int(os.environ.get("PORT", "10000"))), H).serve_forever()
