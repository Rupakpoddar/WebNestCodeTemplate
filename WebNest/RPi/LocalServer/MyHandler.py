# MyHandler.py

from http.server import SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from WebNestDevice import deviceList

class MyHandler(SimpleHTTPRequestHandler):
    """
    Custom request handler to manage HTTP requests for controlling WebNest devices.
    """

    def end_headers(self):
        """
        Override end_headers to set CORS headers.
        """
        self.send_header('Access-Control-Allow-Origin', '*')  # Consider restricting in production
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        SimpleHTTPRequestHandler.end_headers(self)

    def do_OPTIONS(self):
        """
        Handle HTTP OPTIONS requests for CORS preflight.
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')  # Consider restricting in production
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        """
        Handle HTTP GET requests.
        Respond with either the status of all devices or modify the state of a specific device.
        """
        # Parse the query parameters from the URL
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        
        # If no parameters are passed, return the status of all devices
        if not query_params:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # Create a string with the status of all devices
            deviceListString = [str(instance) for instance in deviceList]
            self.wfile.write("{{{}}}".format(','.join(deviceListString)).encode('utf-8'))
            return

        # Access individual parameters from the query
        deviceName = query_params.get('deviceName', [''])[0]
        paramType = query_params.get('paramType', [''])[0]
        paramValue = query_params.get('paramValue', [''])[0]
        
        # Find the specified device and update its parameters
        currentDevice = [x for x in deviceList if x.name == deviceName]
        
        if currentDevice:
            if paramType == 'Color':
                currentDevice[0].color = int(paramValue, 16)
            elif paramType == 'State':
                paramValue = int(paramValue)
                currentDevice[0].state = 1 - currentDevice[0].state if paramValue < 0 else paramValue
            elif paramType == 'PWM':
                currentDevice[0].pwm = int(paramValue)
            elif paramType == 'Temperature':
                currentDevice[0].temperature = int(paramValue)

        # Send a response with the updated parameter values
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        response_message = f"Received parameters: deviceName={deviceName}, paramType={paramType}, paramValue={paramValue}"
        self.wfile.write(response_message.encode('utf-8'))
