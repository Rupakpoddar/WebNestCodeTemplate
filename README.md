# 🕸️ WebNest

<a href="https://github.com/Rupakpoddar/WebNestCodeTemplate/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge" alt="License">
</a>
<img src="https://img.shields.io/badge/contributions-welcome-purple.svg?style=for-the-badge" alt="Contributions Welcome">

**[WebNest](https://rupakpoddar.github.io/WebNest/)** is a rapid, straightforward solution for implementing home automation or remote device control using Firebase or a local server. It allows for quick prototyping and real-time updates without extensive setup or configuration.

## 🚀 Features

- **Universal Compatibility**: Use with any MCU or MPU of your choice.
- **Flexible Backend**: Supports both Firebase and local servers for seamless data handling.
- **Real-time Control**: Instantly update and control your devices without delays.
- **Easy Setup**: Simply plug in your Firebase Project Reference URL or local server IP, configure permissions, and start controlling your devices.
- **Persistent Storage**: WebNest stores device configurations directly in your browser for quick and easy access.
- **Import/Export Configurations**: Save and share your setup with a single click using the import/export feature.

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

### 🔐 Firebase Rules Setup

To get started with Firebase, ensure your Firebase rules are set to allow public access. Set your Firebase rules as follows:

```json
{
    "rules": {
        ".read": "true",
        ".write": "true"
    }
}
```

## 🌟 Contributions
We welcome contributions! Feel free to open issues or submit pull requests to enhance WebNest.
