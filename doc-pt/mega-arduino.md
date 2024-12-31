Para este projeto, vamos dividir a solução em três partes:

1. **Servidor Web no Arduino Mega**: Configuração do Arduino como servidor web com uma página HTML que contém botões para enviar comandos de movimento.
2. **Script Python no PC**: Interface gráfica em Python para controlar os movimentos do Arduino via USB.
3. **Script Arduino em C++**: Código para o Arduino interpretar os comandos recebidos e controlar três servomotores e dois motores DC.

### 1. Código do Servidor Web no Arduino Mega

Aqui está o código em C++ para o Arduino Mega, configurando um servidor web simples. Este código cria uma página HTML com botões que enviam comandos de movimento para o Arduino. Certifique-se de ter a biblioteca **Ethernet** ou **WiFi** adequada se usar um módulo de rede. Aqui, consideramos a Ethernet.

#### Código em C++ para o Arduino

```cpp
#include <Ethernet.h>
#include <Servo.h>

// Definir pinos dos motores e servos
Servo servo1, servo2, servo3;
int motor1Pin = 9;
int motor2Pin = 10;

EthernetServer server(80);

void setup() {
  // Iniciar comunicação Serial
  Serial.begin(9600);
  
  // Iniciar servos e definir posição inicial
  servo1.attach(3);
  servo2.attach(4);
  servo3.attach(5);
  servo1.write(90);
  servo2.write(90);
  servo3.write(90);
  
  // Configurar pinos dos motores como saída
  pinMode(motor1Pin, OUTPUT);
  pinMode(motor2Pin, OUTPUT);

  // Iniciar o servidor Ethernet
  Ethernet.begin(mac, ip);
  server.begin();
  Serial.println("Servidor iniciado");
}

void loop() {
  EthernetClient client = server.available();
  
  if (client) {
    String request = client.readStringUntil('\r');
    Serial.println(request);
    client.flush();

    // Comandos para mover motores e servos
    if (request.indexOf("/UP") != -1) {
      moverFrente();
    }
    if (request.indexOf("/DOWN") != -1) {
      moverTras();
    }
    if (request.indexOf("/LEFT") != -1) {
      virarEsquerda();
    }
    if (request.indexOf("/RIGHT") != -1) {
      virarDireita();
    }
    if (request.indexOf("/STOP") != -1) {
      parar();
    }

    // Enviar página HTML de controle ao cliente
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");
    client.println("Connection: close");
    client.println();
    client.println("<!DOCTYPE HTML>");
    client.println("<html>");
    client.println("<h1>Controle de Movimento</h1>");
    client.println("<button onclick=\"location.href='/UP'\">Frente</button>");
    client.println("<button onclick=\"location.href='/DOWN'\">Trás</button>");
    client.println("<button onclick=\"location.href='/LEFT'\">Esquerda</button>");
    client.println("<button onclick=\"location.href='/RIGHT'\">Direita</button>");
    client.println("<button onclick=\"location.href='/STOP'\">Parar</button>");
    client.println("</html>");
    
    delay(1);
    client.stop();
  }
}

void moverFrente() {
  digitalWrite(motor1Pin, HIGH);
  digitalWrite(motor2Pin, HIGH);
}

void moverTras() {
  digitalWrite(motor1Pin, LOW);
  digitalWrite(motor2Pin, LOW);
}

void virarEsquerda() {
  servo1.write(60);
}

void virarDireita() {
  servo1.write(120);
}

void parar() {
  digitalWrite(motor1Pin, LOW);
  digitalWrite(motor2Pin, LOW);
  servo1.write(90);
  servo2.write(90);
  servo3.write(90);
}
```

### 2. Interface Gráfica em Python para o PC

Este código cria uma janela com botões para cada movimento, enviando comandos para o Arduino Mega via USB.

```python
import tkinter as tk
import serial

# Configurar a porta USB e taxa de transmissão
ser = serial.Serial('COM3', 9600)  # Certifique-se de usar a porta correta

def enviar_comando(comando):
    ser.write(comando.encode())

def frente():
    enviar_comando("UP")

def tras():
    enviar_comando("DOWN")

def esquerda():
    enviar_comando("LEFT")

def direita():
    enviar_comando("RIGHT")

def parar():
    enviar_comando("STOP")

# Criar janela
janela = tk.Tk()
janela.title("Controle do Arduino")

# Botões de movimento
tk.Button(janela, text="Frente", command=frente).pack()
tk.Button(janela, text="Trás", command=tras).pack()
tk.Button(janela, text="Esquerda", command=esquerda).pack()
tk.Button(janela, text="Direita", command=direita).pack()
tk.Button(janela, text="Parar", command=parar).pack()

janela.mainloop()
```

### 3. Ligações dos Motores e Servos ao Arduino Mega

Para conectar os servos e motores ao Arduino Mega, siga estas instruções:

- Conecte os fios de sinal dos servos aos pinos 3, 4 e 5.
- Conecte o motor1 ao pino 9 e o motor2 ao pino 10.
- Alimente o Arduino através da porta USB e os servos/motores com uma fonte externa, se necessário, para evitar sobrecarga.

### Explicação e Comentários

1. **Arduino (C++):**
   - Configura um servidor web que responde a pedidos HTTP simples.
   - Os comandos na página HTML ativam funções como `moverFrente()` e `virarEsquerda()`.
   - Cada comando controla os motores e servos.

2. **Python (Tkinter)**:
   - Interface gráfica com botões para enviar comandos seriais.
   - Funções como `frente()` e `direita()` enviam dados ao Arduino, que os interpreta e move os motores.

Essa estrutura permite controlar o Arduino via web e localmente com a interface em Python.
