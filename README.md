# 🕸️ WebNest

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)
![Platform Support](https://img.shields.io/badge/platform-MCU/MPU-9cf)

**WebNest** is a rapid, straightforward solution for implementing home automation or remote device control using Firebase or a local server. It allows for quick prototyping and real-time updates without extensive setup or configuration.

## 🚀 Features

- **Universal Compatibility**: Use with any MCU or MPU of your choice.
- **Flexible Backend**: Supports both Firebase and local servers for seamless data handling.
- **Real-time Control**: Instantly update and control your devices without delays.
- **Easy Setup**: Simply plug in your Firebase Project Reference URL or local server IP, configure permissions, and start controlling your devices.

## 🛠️ Getting Started

### 🔗 Supported Platforms

WebNest can be used with **any MCU or MPU**, including but not limited to:

- **Raspberry Pi**:
  - [Local Server Setup](https://github.com/Rupakpoddar/WebNestCodeTemplate/tree/main/RPi/LocalServer)
  - [Firebase Setup](https://github.com/Rupakpoddar/WebNestCodeTemplate/tree/main/RPi/Firebase)
  
- **Raspberry Pi Pico W**:
  - [Firebase Setup](https://github.com/Rupakpoddar/WebNestCodeTemplate/tree/main/RPico/Firebase)

- **ESP8266, ESP32, Arduino UNO R4 WiFi**:
  - Use with the [Arduino Firebase Library](https://github.com/Rupakpoddar/FirebaseArduino). Check out the WebNest example in the library.

### 📝 Firebase Rules Setup

To get started with Firebase, ensure your Firebase rules are set to allow public access. Set your Firebase rules as follows:

```json
{
    "rules": {
        ".read": "true",
        ".write": "true"
    }
}
