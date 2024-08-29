from http.server import SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from webnest_device import device_list

class MyHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        """Add CORS headers to the HTTP response."""
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow all origins
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # Allow GET, POST, and OPTIONS methods
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')  # Allow Content-Type header
        super().end_headers()  # Call the parent class's end_headers method

    def do_OPTIONS(self):
        """Handle OPTIONS requests (CORS preflight)."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow all origins
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # Allow GET, POST, and OPTIONS methods
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')  # Allow Content-Type header
        self.end_headers()  # Finalize headers

    def do_GET(self):
        """Handle GET requests by parsing query parameters and responding accordingly."""
        # Parse the URL query parameters
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        
        # If no query parameters, return the list of devices as a JSON-like string
        if not query_params:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Join all devices' string representations and send as response
            device_list_string = [str(device) for device in device_list]
            self.wfile.write("{{{}}}".format(','.join(device_list_string)).encode('utf-8'))
            return

        # Extract individual query parameters
        device_name = query_params.get('deviceName', [''])[0]
        param_type = query_params.get('paramType', [''])[0]
        param_value = query_params.get('paramValue', [''])[0]
        
        # Find the device by name
        current_device = next((device for device in device_list if device.name == device_name), None)

        if current_device:
            # Update the device parameters based on the paramType
            if param_type == 'Color':
                current_device.color = int(param_value, 16)
            elif param_type == 'State':
                param_value = int(param_value)
                if param_value < 0:
                    current_device.state = 1 - current_device.state  # Toggle state if value is negative
                else:
                    current_device.state = param_value
            elif param_type == 'PWM':
                current_device.pwm = int(param_value)
            elif param_type == 'Temperature':
                current_device.temperature = int(param_value)

        # Respond with a confirmation message
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response_message = f"Received parameters: deviceName={device_name}, paramType={param_type}, paramValue={param_value}"
        self.wfile.write(response_message.encode('utf-8'))
