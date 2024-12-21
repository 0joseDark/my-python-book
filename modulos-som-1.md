Aqui está uma lista de **módulos de som para Python**, explicados em português europeu, incluindo instruções para a instalação no Windows 10 e no Ubuntu Linux.  

---

### 1. **PyDub**
- **Descrição**:  
  PyDub é uma biblioteca para manipular ficheiros de áudio. Permite cortar, juntar, alterar volume, exportar em diferentes formatos e muito mais.
- **Instalação**:  
  - **Windows 10**:  
    ```bash
    pip install pydub
    ```
    Além disso, é necessário instalar o **FFmpeg**:
    1. Faça download do FFmpeg [aqui](https://ffmpeg.org/download.html).  
    2. Adicione a pasta `bin` do FFmpeg ao PATH do sistema.
  - **Ubuntu Linux**:  
    ```bash
    sudo apt update
    sudo apt install ffmpeg
    pip install pydub
    ```

---

### 2. **Sounddevice**
- **Descrição**:  
  Sounddevice permite gravar e reproduzir áudio diretamente com baixa latência. É útil para criar aplicações de gravação de som ou reprodução em tempo real.  
- **Instalação**:  
  - **Windows 10 e Ubuntu Linux**:  
    ```bash
    pip install sounddevice
    ```
    Para suporte de áudio adicional, instale o **PortAudio**:
    - **Ubuntu Linux**:  
      ```bash
      sudo apt install portaudio19-dev
      ```

---

### 3. **Wave**
- **Descrição**:  
  Wave é um módulo nativo do Python para leitura e escrita de ficheiros WAV. É ideal para trabalhar com som em formato não comprimido.  
- **Instalação**:  
  Este módulo já vem com o Python, não sendo necessário instalar.

---

### 4. **PyAudio**
- **Descrição**:  
  PyAudio fornece uma interface para trabalhar com o sistema de áudio em tempo real e ficheiros WAV, permitindo gravação e reprodução.
- **Instalação**:  
  - **Windows 10**:  
    Instale a versão precompilada:
    1. Faça download do ficheiro `.whl` correspondente à sua versão Python [aqui](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).  
    2. Instale-o com:  
       ```bash
       pip install <nome_do_ficheiro.whl>
       ```
  - **Ubuntu Linux**:  
    ```bash
    sudo apt update
    sudo apt install python3-pyaudio
    pip install pyaudio
    ```

---

### 5. **Audioread**
- **Descrição**:  
  Audioread é uma biblioteca que suporta a leitura de ficheiros de áudio em vários formatos, como MP3, WAV, AAC, entre outros.  
- **Instalação**:  
  - **Windows 10 e Ubuntu Linux**:  
    ```bash
    pip install audioread
    ```

---

### 6. **Librosa**
- **Descrição**:  
  Librosa é usada para análise e manipulação de áudio, incluindo processamento de sinais e extração de características como espectrogramas.  
- **Instalação**:  
  - **Windows 10 e Ubuntu Linux**:  
    ```bash
    pip install librosa
    ```
    Para garantir dependências completas, instale também o **FFmpeg** (veja as instruções no **PyDub**).

---

### 7. **Simpleaudio**
- **Descrição**:  
  Simpleaudio é uma biblioteca leve para reproduzir áudio, suportando ficheiros WAV.  
- **Instalação**:  
  - **Windows 10 e Ubuntu Linux**:  
    ```bash
    pip install simpleaudio
    ```

---

### 8. **Scipy (Signal)**  
- **Descrição**:  
  O módulo `scipy.signal` oferece ferramentas para processamento de sinais, incluindo sinais de áudio, como filtros e transformadas.  
- **Instalação**:  
  - **Windows 10 e Ubuntu Linux**:  
    ```bash
    pip install scipy
    ```

---

### 9. **Mutagen**
- **Descrição**:  
  Mutagen é uma biblioteca para manipular metadados de ficheiros de áudio, como etiquetas ID3 em MP3.  
- **Instalação**:  
  - **Windows 10 e Ubuntu Linux**:  
    ```bash
    pip install mutagen
    ```

---

### 10. **Midiutil**
- **Descrição**:  
  Midiutil é usado para criar e manipular ficheiros MIDI, ideal para música programática.  
- **Instalação**:  
  - **Windows 10 e Ubuntu Linux**:  
    ```bash
    pip install midiutil
    ```

---

### Resumo das Instalações no Ubuntu Linux  
```bash
sudo apt update
sudo apt install ffmpeg portaudio19-dev python3-pyaudio
pip install pydub sounddevice audioread librosa simpleaudio scipy mutagen midiutil
```

### Ferramentas Adicionais  
- **FFmpeg** (obrigatório para alguns módulos como PyDub e Librosa).  
- **PortAudio** (necessário para Sounddevice e PyAudio).

Estas bibliotecas cobrem uma ampla gama de funcionalidades, desde manipulação de áudio até processamento de sinais e criação de ficheiros MIDI.