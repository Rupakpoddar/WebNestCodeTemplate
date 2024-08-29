# WebNestDevice.py

# A list to hold all instances of WebNestDevice
deviceList = []

class WebNestDevice:
    """
    Class to represent a web-controlled device (like a smart light or fan).
    """
    def __init__(self, name: str):
        """
        Initialize a new WebNestDevice with default parameters.
        Args:
            name (str): The name of the device.
        """
        self.name = name
        self.color = 0xFFE0B2  # Default color (hex value)
        self.state = 0         # Device state (on/off)
        self.pwm = 50          # Pulse Width Modulation percentage
        self.temperature = 50  # Temperature setting

        # Add this device instance to the global deviceList
        deviceList.append(self)
    
    def __str__(self):
        """
        String representation of the device in JSON-like format.
        """
        return '"%s":{"Color":"%s","PWM":%s,"State":%s,"Temperature":%s}' % (
            self.name, hex(self.color)[2:].upper(), self.pwm, self.state, self.temperature)
    
    def __del__(self):
        """
        Cleanup method called when the object is destroyed.
        Removes the device from the global list.
        """
        deviceList.remove(self)
