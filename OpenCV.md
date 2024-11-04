O OpenCV (Open Source Computer Vision Library) é uma biblioteca de código aberto para processamento de imagem e visão computacional. Ela oferece uma vasta gama de funcionalidades para manipular, analisar e transformar imagens. Vamos passar por alguns exemplos básicos usando OpenCV em Python para ilustrar como funciona.

### Passos para Instalar e Importar OpenCV

Antes de começarmos, instale a biblioteca OpenCV no seu ambiente Python, caso ainda não tenha feito isso:

```bash
pip install opencv-python
```

Depois de instalar, você pode importar o OpenCV como:

```python
import cv2
```

### 1. Leitura e Exibição de Imagens

Para começar, vamos carregar uma imagem e exibi-la numa janela.

```python
import cv2

# Carregar uma imagem
imagem = cv2.imread('exemplo.jpg')  # Substitua pelo caminho da sua imagem

# Exibir a imagem
cv2.imshow('Imagem Original', imagem)

# Aguardar até que uma tecla seja pressionada e fechar a janela
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 2. Redimensionamento de Imagem

Você pode redimensionar imagens para ajustá-las a tamanhos específicos.

```python
import cv2

imagem = cv2.imread('exemplo.jpg')
imagem_redimensionada = cv2.resize(imagem, (300, 300))  # Redimensiona para 300x300 pixels

cv2.imshow('Imagem Redimensionada', imagem_redimensionada)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 3. Conversão de Cores

Um dos processos mais comuns é converter uma imagem colorida para tons de cinza ou outras representações de cor.

```python
import cv2

imagem = cv2.imread('exemplo.jpg')

# Converter para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

cv2.imshow('Imagem em Tons de Cinza', imagem_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 4. Aplicar Filtro Gaussiano

Filtros são usados para suavizar imagens e remover ruído. Um dos filtros mais comuns é o filtro Gaussiano.

```python
import cv2

imagem = cv2.imread('exemplo.jpg')

# Aplicar o filtro Gaussiano
imagem_suavizada = cv2.GaussianBlur(imagem, (15, 15), 0)

cv2.imshow('Imagem Suavizada', imagem_suavizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 5. Detecção de Bordas com Canny

O algoritmo Canny é usado para detectar bordas em imagens, o que é muito útil em análises de contornos.

```python
import cv2

imagem = cv2.imread('exemplo.jpg')
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplicar o detector de bordas de Canny
bordas = cv2.Canny(imagem_cinza, 100, 200)

cv2.imshow('Bordas Detectadas', bordas)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 6. Desenho de Formas na Imagem

Você pode adicionar formas geométricas, como retângulos, círculos e linhas, diretamente em imagens.

```python
import cv2

imagem = cv2.imread('exemplo.jpg')

# Desenhar um retângulo na imagem
cv2.rectangle(imagem, (50, 50), (200, 200), (0, 255, 0), 3)

# Desenhar um círculo na imagem
cv2.circle(imagem, (300, 300), 50, (255, 0, 0), -1)

cv2.imshow('Imagem com Formas', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 7. Transformação de Perspectiva (Warping)

Às vezes, você precisa ajustar a perspectiva de uma imagem, como "dobrar" ou "esticar" uma área específica.

```python
import cv2
import numpy as np

imagem = cv2.imread('exemplo.jpg')

# Coordenadas dos pontos de origem (o que queremos transformar)
pontos_originais = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])

# Coordenadas dos pontos de destino (para onde queremos mapear)
pontos_destino = np.float32([[10, 100], [200, 50], [100, 250], [300, 200]])

# Matriz de transformação
matriz = cv2.getPerspectiveTransform(pontos_originais, pontos_destino)

# Aplicar a transformação de perspectiva
imagem_transformada = cv2.warpPerspective(imagem, matriz, (imagem.shape[1], imagem.shape[0]))

cv2.imshow('Imagem Transformada', imagem_transformada)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 8. Segmentação de Cor

Segmentação de cor é útil para identificar e extrair regiões de uma imagem com base na cor.

```python
import cv2
import numpy as np

imagem = cv2.imread('exemplo.jpg')

# Converter a imagem para o espaço de cores HSV
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Definir intervalos de cor para a máscara (aqui, para uma cor azul)
limite_inferior = np.array([110, 50, 50])
limite_superior = np.array([130, 255, 255])

# Criar uma máscara
mascara = cv2.inRange(imagem_hsv, limite_inferior, limite_superior)

# Aplicar a máscara na imagem original
imagem_segmentada = cv2.bitwise_and(imagem, imagem, mask=mascara)

cv2.imshow('Imagem Segmentada', imagem_segmentada)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

Estes são exemplos introdutórios de processamento de imagem usando OpenCV em Python.
