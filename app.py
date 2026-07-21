from http.server import BaseHTTPRequestHandler, HTTPServer

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        result = factorial(10)
        self.wfile.write(f"<h1>Factorial of 5 is {result}</h1>".encode())

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    print("Server running on port 8000")
    server.serve_forever()