"""
Instructions to run the WebNest server locally and connect it with the WebNest interface:

1. Run this script (main.py) to start the local server.
2. Once the server is running, copy the URL shown in the terminal (http://localhost:{port}).
3. Go to the following link in your web browser: https://rupakpoddar.github.io/WebNest/
4. In the WebNest interface, click the gear icon on the top right to open the setup tab.
5. Paste the copied URL (http://localhost:{port}) into the "Service URL/IP" field and click "Update."
6. Click the add button (+) on the top right to create a new device. For this example:
    - Create a device with the name "BedroomLight" (without quotes).
    - Choose the button style (ON/OFF or Toggle).
    - Select the desired parameters like color, temperature, and pwm.
    - Click "Finish" to create the new WebNest device.
7. Repeat the same process to create additional devices like "TableFan" and "DeskLamp."

Now you should be able to control the devices locally through the WebNest interface.

"""

from http.server import HTTPServer
from webnest_device import WebNestDevice
from my_handler import MyHandler

if __name__ == '__main__':
    # Create WebNest devices
    WebNestDevice("BedroomLight")
    WebNestDevice("TableFan")
    WebNestDevice("DeskLamp")
    
    # Define the port for the HTTP server
    port = 8080

    # Create the server instance with custom handler
    server = HTTPServer(('localhost', port), MyHandler)

    # Print server status
    print(f"Server running on http://localhost:{port}")

    # Start the server
    server.serve_forever()
