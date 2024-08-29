 # This module defines the WebNestDevice class and manages a global list of devices.

# Global device list to store all instances of WebNestDevice
deviceList = []

class WebNestDevice:
    def __init__(self, name: str):
        """Initialize a WebNest device with default parameters."""
        self.name = name
        self.color = 0xFFE0B2   # Default color
        self.state = 0          # Default state (off)
        self.pwm = 50           # Default PWM value
        self.temperature = 50   # Default temperature
        
        # Add the newly created device to the global device list
        deviceList.append(self)
    
    def __str__(self):
        """Return a string representation of the device in JSON-like format."""
        return '"%s":{"Color":"%s","PWM":%s,"State":%s,"Temperature":%s}' % (
            self.name, hex(self.color)[2:].upper(), self.pwm, self.state, self.temperature)
    
    def __del__(self):
        """Remove the device from the device list when it is deleted."""
        deviceList.remove(self)
