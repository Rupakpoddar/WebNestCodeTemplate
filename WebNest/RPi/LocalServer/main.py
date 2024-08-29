from http.server import HTTPServer
from WebNestDevice import WebNestDevice, deviceList
from MyHandler import MyHandler

if __name__ == '__main__':
    # Create WebNest devices
    WebNestDevice("BedroomLight")
    WebNestDevice("HallLight")
    WebNestDevice("DeskLamp")
    
    # Define the port for the HTTP server
    port = 8080

    # Create the server instance with custom handler
    server = HTTPServer(('localhost', port), MyHandler)

    # Print server status
    print(f"Server running on http://localhost:{port}")

    # Start the server
    server.serve_forever()
