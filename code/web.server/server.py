import http.server
import socketserver

# Define the handler to use for incoming requests
handler = http.server.SimpleHTTPRequestHandler

# Define the port number for the server to listen on
port = 8080

# Create the server and bind it to the specified port
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Serving on port {port}")

    # Run the server forever
    httpd.serve_forever()
