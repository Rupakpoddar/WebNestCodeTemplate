'''
Written by Rupak Poddar
https://rupakpoddar.github.io/
'''

from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

deviceList = []

class WebNestDevice():
    def __init__ (self, name:str):
        # Device initalization parameters
        self.name = name
        self.color = 0xFFE0B2
        self.state = 0
        self.pwm = 50
        self.temperature = 50
        
        # Add the instance to a list
        deviceList.append(self)
    
    def __str__ (self):
        return '"%s":{"Color":"%s","PWM":%s,"State":%s,"Temperature":%s}' %(self.name, hex(self.color)[2:].upper(), self.pwm, self.state, self.temperature)
    
    def __del__ (self):
        deviceList.remove(self)

class MyHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')  # You might want to restrict this to specific origins in production
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        SimpleHTTPRequestHandler.end_headers(self)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')  # You might want to restrict this to specific origins in production
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
    def do_GET(self):
        # Parse the query parameters from the URL
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        
        # Check if no parameters are passed
        if not query_params:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            deviceListString = [str(instance) for instance in deviceList]
            self.wfile.write("{{{}}}".format(','.join(deviceListString)).encode('utf-8'))
            return

        # Access individual parameters
        deviceName = query_params.get('deviceName', [''])[0]
        paramType = query_params.get('paramType', [''])[0]
        paramValue = query_params.get('paramValue', [''])[0]
        
        # Update the WebNest device
        currentDevice = [x for x in deviceList if x.name == deviceName]
        
        if currentDevice:
            if paramType == 'Color':
                currentDevice[0].color = int(paramValue, 16)
            if paramType == 'State':
                paramValue = int(paramValue)
                if (paramValue < 0):
                    currentDevice[0].state = 1 - currentDevice[0].state
                else:
                    currentDevice[0].state = paramValue
            if paramType == 'PWM':
                currentDevice[0].pwm = int(paramValue)
            if paramType == 'Temperature':
                currentDevice[0].temperature = int(paramValue)

        # Send a response with the parameter values
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        response_message = f"Received parameters: deviceName={deviceName}, paramType={paramType}, paramValue={paramValue}"
        self.wfile.write(response_message.encode('utf-8'))

if __name__ == '__main__':
    # Make some WebNest devices
    WebNestDevice("BedroomLight")
    WebNestDevice("HallLight")
    WebNestDevice("DeskLamp")
    
    # Define the port on which you want to run the server
    port = 8080

    # Create the server instance with your custom handler
    server = HTTPServer(('localhost', port), MyHandler)

    print(f"Server running on http://localhost:{port}")

    # Start the server
    server.serve_forever()

    