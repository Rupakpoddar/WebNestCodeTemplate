"""
---------------------------------
IMPORTANT: Configuration Reminder
---------------------------------

Before running this code, make sure to update the 'config.py' file
for important configuration details such as Wi-Fi credentials and
Firebase settings.

The 'config.py' file should include:
- Your Wi-Fi SSID and Password
- Your Firebase Realtime Database URL

Ensure that 'config.py' is properly configured and includes the correct
information for your project. Failure to do so may result in connection
errors or incorrect behavior of your application.

Note: The 'config.py' file should be located in the same directory as
this script.
"""

"""
---------------------------------
INFO: WebNest Setup & Usage Guide  
---------------------------------

WebNest is a rapid, straightforward solution for implementing home automation
or remote device control using Firebase or a local server. It allows for quick
prototyping and real-time updates without extensive setup or configuration.

To get started with WebNest, follow these steps to set up and configure
your devices and connect them with Firebase for real-time control and monitoring.

1. Visit the official WebNest site:
   Go to https://rupakpoddar.github.io/WebNest/

2. Configure the Service URL:
   - Click the gear icon in the top right corner to open the setup dialog.
   - In the "Service URL/IP" field, paste your Firebase Realtime Database Reference URL.
   - Select "Update" to apply the settings.

3. Add Devices:
   - Click the "+" button on the top right corner to add a new device.
   - For this example, enter the device name as "Ambience Light" (case-sensitive, without quotes).
     Ensure the name matches exactly, including spaces and capitalization.
   - Choose the style for the controls (ON/OFF, Toggle, etc.) and select additional features like 
     Color Picker, Temperature, and PWM as needed.

4. Add Another Device:
   - Repeat the process above to add another device, and name it "Pedestal Fan".
   - Again, ensure that the device name matches exactly as provided.

5. Firebase Configuration:
   - Ensure that your Firebase Realtime Database is in "Test Mode" for proper read/write access
     during development. This allows unrestricted access without requiring authentication.

6. Upload to Board:
   - Once you've completed the setup, configure your code properly (see config.py for Firebase 
     and Wi-Fi credentials) and upload this script to your Raspberry Pi Pico.
   - Once the board is running, you will see the device states getting updated in real-time on the WebNest interface.
"""

import urequests
import ujson
import network
import time
import gc
from machine import Pin

# Import Wi-Fi and Firebase configuration
import config
from webnest_device import WebNestDevice

# Initialize Firebase URL
FIREBASE_URL = config.REFERENCE_URL

# Create WebNest devices
ambience_light = WebNestDevice("Ambience Light")
pedestal_fan = WebNestDevice("Pedestal Fan")

# Set up Wi-Fi connection
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(config.WIFI_SSID, config.WIFI_PASSWORD)

    print("\nConnecting to Wi-Fi...")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(0.5)

    print("\nWi-Fi Connected\n")
    print("Network config:", wlan.ifconfig())

# Main loop to update and display device states
def main():
    connect_to_wifi()

    while True:
        # Fetch data from Firebase
        response = urequests.get(FIREBASE_URL + ".json")
        if response.status_code == 200:
            json_data = response.text
            response.close()
            WebNestDevice.poll(json_data)
            gc.collect()
        else:
            print("Error fetching data from Firebase")

        # Display device states
        print("Device Name\t\tState\tTemp\tPWM\tColor")
        print(f"{ambience_light.get_name()}\t\t{ambience_light.get_state()}\t{ambience_light.get_temperature()}\t{ambience_light.get_pwm()}\t{ambience_light.get_color():06X}")
        print(f"{pedestal_fan.get_name()}\t\t{pedestal_fan.get_state()}\t{pedestal_fan.get_temperature()}\t{pedestal_fan.get_pwm()}\t{pedestal_fan.get_color():06X}")
        print()

        time.sleep(1)

# Run the main function
if __name__ == "__main__":
    main()
