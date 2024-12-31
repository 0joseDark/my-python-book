# Módulos de Som em Python

## 1. Manipulação e Processamento de Áudio

- **pydub**: Biblioteca poderosa para manipulação de áudio, suporta operações como cortar, juntar e aplicar efeitos em ficheiros de áudio. Compatível com formatos como MP3, WAV, entre outros.
- **librosa**: Focada na análise e extração de características do áudio, muito usada para tarefas de processamento de áudio, como análise de espectro e extração de recursos musicais.
- **wave**: Biblioteca nativa para ler e gravar ficheiros de áudio no formato WAV, útil para manipulação de áudio em baixa complexidade.
- **audioread**: Interface para várias bibliotecas de backend, permite leitura de múltiplos formatos de áudio.
- **soundfile**: Utilizado para ler e gravar ficheiros de áudio no formato WAV e FLAC, oferece leitura e escrita de alta qualidade.
- **scipy.io.wavfile**: Parte do SciPy, permite leitura e gravação de ficheiros WAV, especialmente para projetos que já utilizam a biblioteca SciPy.
- **madmom**: Biblioteca voltada para tarefas de processamento de música e reconhecimento de batidas.

## 2. Reprodutores de Áudio

- **pygame.mixer**: Módulo de áudio do Pygame, permite reprodução simples e manipulação de ficheiros de som em jogos e outras aplicações interativas.
- **playsound**: Reproduz ficheiros de áudio com uma única linha de código. Funciona com ficheiros WAV e MP3.
- **python-vlc**: Interface Python para o VLC media player, permite reprodução avançada de áudio e vídeo com controle completo do fluxo de mídia.
- **simpleaudio**: Oferece reprodução síncrona e assíncrona de ficheiros de áudio WAV.
- **sounddevice**: Usado para reprodução e gravação de áudio diretamente pelo dispositivo de áudio, com suporte a gravações multi-canal e baixa latência.

## 3. Gravação e Captura de Áudio

- **sounddevice**: Além de reprodução, permite captura de áudio de dispositivos de entrada, sendo útil para gravação em tempo real.
- **pyaudio**: Interface para a biblioteca PortAudio, permite gravação e reprodução de áudio multi-plataforma.
- **microphone**: Parte do pacote `speech_recognition`, permite captura de áudio pelo microfone para posterior reconhecimento de fala.
- **audiomath**: Combina funcionalidades de análise e gravação de áudio, com um foco em medições de som.

## 4. Análise e Síntese de Áudio

- **scipy.signal**: Inclui ferramentas para análise e manipulação de sinais de áudio, como filtros e transformadas.
- **noisereduce**: Biblioteca para reduzir ruído de áudio, útil para pré-processamento de gravações.
- **spleeter**: Modelo baseado em aprendizado de máquina para separação de fontes musicais, como voz e instrumentos em uma faixa de áudio.
- **aubio**: Oferece algoritmos de análise de áudio, como detecção de batidas, tons e pitch tracking.
- **wavebender**: Ferramenta para síntese de áudio e geração de ondas sonoras com formas de onda customizadas.
- **rtmixer**: Reproduz e mistura áudio em tempo real, usando bibliotecas de backend como PortAudio e RtAudio.

## 5. Conversão e Manipulação de Formatos de Áudio

- **ffmpeg-python**: Interface para a ferramenta FFmpeg, permite conversão entre formatos de áudio, manipulação de streams e edição avançada.
- **soundconverter**: Facilita a conversão de formatos de áudio, compatível com uma variedade de codecs de áudio.
- **sox**: Interface para o programa SoX (Sound eXchange), permite manipulação avançada de áudio e conversão de formatos.
