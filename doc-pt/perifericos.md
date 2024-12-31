
# Módulos Periféricos e Portas IO em Python

Este documento fornece uma explicação dos módulos em Python que podem ser usados para interagir com periféricos e portas de entrada/saída (IO). Abaixo estão listados módulos que permitem o controlo de dispositivos como ratos, teclados, câmaras, portas USB, e muito mais.

## 1. Módulos para Rato e Teclado

### **`pynput`**
- **Descrição:** O `pynput` é utilizado para controlar e monitorizar o rato e o teclado.
- **Funcionalidades:**
  - Captura de eventos de rato (cliques, movimento, rotação da roda).
  - Captura de eventos de teclado (teclas pressionadas e libertadas).
  - Automação de cliques e movimentos do rato.
  - Simulação de pressionar teclas.
- **Exemplo:**
  ```python
  from pynput.mouse import Controller

  mouse = Controller()
  mouse.position = (100, 200)  # Move o rato para a posição (100, 200)
  ```

### **`keyboard`**
- **Descrição:** O módulo `keyboard` permite o controlo de eventos de teclado.
- **Funcionalidades:**
  - Escuta de teclas pressionadas.
  - Automação de entradas de teclado.
  - Criação de hotkeys personalizadas.
- **Exemplo:**
  ```python
  import keyboard

  keyboard.press_and_release('shift + a')  # Pressiona a combinação 'Shift+A'
  ```

## 2. Módulos para Câmaras

### **`opencv-python` (OpenCV)**
- **Descrição:** OpenCV é uma biblioteca poderosa para visão computacional, incluindo captura e manipulação de vídeo e imagem.
- **Funcionalidades:**
  - Captura de vídeo em tempo real de uma câmara USB.
  - Processamento de imagens (detecção de rostos, objetos, etc.).
  - Gravação de vídeo.
- **Exemplo:**
  ```python
  import cv2

  cap = cv2.VideoCapture(0)  # Abre a câmara
  ret, frame = cap.read()
  cv2.imshow('Imagem', frame)  # Exibe a imagem capturada
  ```

## 3. Módulos para Portas USB

### **`pyusb`**
- **Descrição:** O `pyusb` é usado para interagir com dispositivos USB de forma direta.
- **Funcionalidades:**
  - Envio e receção de dados para/dispositivos USB.
  - Controlo de dispositivos USB (como dispositivos HID).
- **Exemplo:**
  ```python
  import usb.core
  import usb.util

  dev = usb.core.find(idVendor=0x1234, idProduct=0x5678)
  if dev is None:
      raise ValueError('Dispositivo USB não encontrado')
  ```

### **`usbinfo`**
- **Descrição:** Fornece informações detalhadas sobre dispositivos USB conectados.
- **Funcionalidades:**
  - Listagem de dispositivos USB.
  - Informação detalhada sobre fabricantes, portas, e números de série.
- **Exemplo:**
  ```python
  from usbinfo import list_usb

  devices = list_usb()
  print(devices)
  ```

## 4. Módulos para Comunicação Serial

### **`pyserial`**
- **Descrição:** O `pyserial` permite a comunicação através de portas seriais (COM).
- **Funcionalidades:**
  - Leitura e escrita em portas seriais.
  - Suporte para RS-232 e outros protocolos de comunicação serial.
- **Exemplo:**
  ```python
  import serial

  ser = serial.Serial('COM3', 9600)
  ser.write(b'Hello')  # Envia dados para a porta serial
  ```

## 5. Módulos para Som

### **`pyaudio`**
- **Descrição:** O `pyaudio` é utilizado para capturar e reproduzir som.
- **Funcionalidades:**
  - Captura de som de um microfone.
  - Reprodução de ficheiros de som.
  - Processamento de áudio em tempo real.
- **Exemplo:**
  ```python
  import pyaudio

  audio = pyaudio.PyAudio()
  stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True)
  data = stream.read(1024)  # Captura som
  ```

### **`sounddevice`**
- **Descrição:** O `sounddevice` oferece funções simples para captura e reprodução de som.
- **Funcionalidades:**
  - Gravação de áudio.
  - Reprodução de som com baixa latência.
- **Exemplo:**
  ```python
  import sounddevice as sd

  fs = 44100  # Taxa de amostragem
  seconds = 3
  myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
  sd.wait()  # Espera pela conclusão da gravação
  ```

## 6. Módulos para Controlar GPIO em Raspberry Pi

### **`RPi.GPIO`**
- **Descrição:** Usado para controlar as portas GPIO no Raspberry Pi.
- **Funcionalidades:**
  - Configuração de portas GPIO como entrada ou saída.
  - Leitura e escrita em portas GPIO.
- **Exemplo:**
  ```python
  import RPi.GPIO as GPIO

  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(7, GPIO.OUT)
  GPIO.output(7, GPIO.HIGH)  # Liga o pino 7
  ```

### **`gpiozero`**
- **Descrição:** Abstração simplificada para controlar GPIO em Raspberry Pi.
- **Funcionalidades:**
  - Suporte para diversos componentes como LEDs, sensores, motores.
- **Exemplo:**
  ```python
  from gpiozero import LED

  led = LED(17)
  led.on()  # Liga o LED conectado ao pino 17
  ```

## 7. Módulos para Comunicação via Rede

### **`socket`**
- **Descrição:** O `socket` é o módulo padrão de Python para comunicação em rede.
- **Funcionalidades:**
  - Comunicação via TCP/UDP.
  - Conexões cliente-servidor.
- **Exemplo:**
  ```python
  import socket

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(('localhost', 12345))
  s.sendall(b'Hello, world')
  ```

---

Este é um resumo dos principais módulos para trabalhar com periféricos e portas IO em Python. Dependendo do tipo de dispositivo com o qual deseja interagir, poderá escolher o módulo adequado para o seu projeto.