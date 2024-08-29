"""
---------------------------------
INFO: WebNestDevice Class for Pi Pico
---------------------------------

Handles individual device configuration and updates using JSON data
from Firebase.
"""

import ujson

MAX_DEVICES = 16

class WebNestDevice:
    # Static list to store all devices
    device_list = []

    def __init__(self, name):
        self.name = name
        self.color = 0xFFE0B2
        self.state = 0
        self.pwm = 50
        self.temperature = 50

        # Add this device to the device list
        WebNestDevice.device_list.append(self)

    # Getters
    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def get_state(self):
        return self.state

    def get_pwm(self):
        return self.pwm

    def get_temperature(self):
        return self.temperature

    # Setters
    def set_color(self, color):
        self.color = color

    def set_state(self, state):
        self.state = state

    def set_pwm(self, pwm):
        self.pwm = pwm

    def set_temperature(self, temperature):
        self.temperature = temperature

    # Static method to poll and update device states from Firebase JSON data
    @staticmethod
    def poll(json_string):
        try:
            data = ujson.loads(json_string)
            for device in WebNestDevice.device_list:
                device_data = data.get(device.get_name())
                if device_data:
                    if "Color" in device_data:
                        device.set_color(int(device_data["Color"], 16))  # Convert hex string to int
                    if "State" in device_data:
                        device.set_state(device_data["State"])
                    if "PWM" in device_data:
                        device.set_pwm(device_data["PWM"])
                    if "Temperature" in device_data:
                        device.set_temperature(device_data["Temperature"])
        except ValueError as e:
            print("JSON parse error:", e)
