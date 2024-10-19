# Peripheral Modules and IO Ports in Python

This document provides an explanation of modules in Python that can be used to interact with peripherals and input/output (IO) ports. Listed below are modules that allow control of devices such as mice, keyboards, cameras, USB ports, and more.

## 1. Mouse and Keyboard Modules

### **`pynput`**
- **Description:** `pynput` is used to control and monitor the mouse and keyboard.
- **Features:**
 - Capture of mouse events (clicks, movement, wheel rotation).
 - Capture of keyboard events (keys pressed and released).
 - Automation of mouse clicks and movements.
 - Key press simulation.
- **Example:**
 ```python
 from pynput.mouse import Controller

 mouse = Controller()
 mouse.position = (100, 200) # Move the mouse to position (100, 200)
 ```

### **`keyboard`**
- **Description:** The `keyboard` module allows control of keyboard events.
- **Features:**
 - Listening to pressed keys.
 - Automation of keyboard inputs.
 - Creation of personalized hotkeys.
- **Example:**
 ```python
 import keyboard

 keyboard.press_and_release('shift + a') # Press the combination 'Shift+A'
 ```

## 2. Camera Modules

### **`opencv-python` (OpenCV)**
- **Description:** OpenCV is a powerful library for computer vision, including video and image capture and manipulation.
- **Features:**
 - Real-time video capture from a USB camera.
 - Image processing (detection of faces, objects, etc.).
 - Video recording.
- **Example:**
 ```python
 import cv2

 cap = cv2.VideoCapture(0) # Open the camera
 ret, frame = cap.read()
 cv2.imshow('Image', frame) # Display the captured image
 ```

## 3. Modules for USB Ports

### **`pyusb`**
- **Description:** `pyusb` is used to interact with USB devices directly.
- **Features:**
 - Sending and receiving data to/USB devices.
 - Control of USB devices (such as HID devices).
- **Example:**
 ```python
 import usb.core
 import usb.util

 dev = usb.core.find(idVendor=0x1234, idProduct=0x5678)
 if dev is None:
 raise ValueError('USB device not found')
 ```

### **`usbinfo`**
- **Description:** Provides detailed information about connected USB devices.
- **Features:**
 - Listing of USB devices.
 - Detailed information about manufacturers, ports, and serial numbers.
- **Example:**
 ```python
 from usbinfo import list_usb

 devices = list_usb()
 print(devices)
 ```

## 4. Modules for Serial Communication

### **`pyserial`**
- **Description:** `pyserial` allows communication through serial (COM) ports.
- **Features:**
 - Reading and writing on serial ports.
 - Support for RS-232 and other serial communication protocols.
- **Example:**
 ```python
 import series

 ser = serial.Serial('COM3', 9600)
 ser.write(b'Hello') # Send data to serial port
 ```

## 5. Modules for Sound

### **`pyaudio`**
- **Description:** `pyaudio` is used to capture and play sound.
- **Features:**
 - Capture sound from a microphone.
 - Playback of sound files.
 - Real-time audio processing.
- **Example:**
 ```python
 import pyaudio

 audio = pyaudio.PyAudio()
 stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True)
 data = stream.read(1024) # Capture sound
 ```

### **`sounddevice`**
- **Description:** `sounddevice` offers simple functions for capturing and playing sound.
- **Features:**
 - Audio recording.
 - Low latency sound reproduction.
- **Example:**
 ```python
 import sounddevice as sd

 fs = 44100 # Sampling rate
 seconds = 3
 myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
 sd.wait() # Wait for recording to complete
 ```

## 6. Modules to Control GPIO on Raspberry Pi

### **`RPi.GPIO`**
- **Description:** Used to control GPIO ports on Raspberry Pi.
- **Features:**
 - Configuration of GPIO ports as input or output.
 - Reading and writing on GPIO ports.
- **Example:**
 ```python
 import RPi.GPIO as GPIO

 GPIO.setmode(GPIO.BOARD)
 GPIO.setup(7, GPIO.OUT)
 GPIO.output(7, GPIO.HIGH) # Connect pin 7
 ```

### **`gpiozero`**
- **Description:** Simplified abstraction to control GPIO on Raspberry Pi.
- **Features:**
 - Support for various components such as LEDs, sensors, motors.
- **Example:**
 ```python
 do gpiozero import LED

 led = LED(17)
 led.on() # Connects the LED connected to pin 17
 ```

## 7. Modules for Network Communication

### **`socket`**
- **Description:** `socket` is the standard Python module for network communication.
- **Features:**
 - Communication via TCP/UDP.
 - Client-server connections.
- **Example:**
 ```python
 import socket

 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect(('localhost', 12345))
 s.sendall(b'Hello, world')
 ```

---
This is a summary of the main modules for working with peripherals and IO ports in Python. Depending on the type of device you want to interact with, you can choose the appropriate module for your project.