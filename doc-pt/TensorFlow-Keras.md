Redes Neurais são modelos computacionais inspirados no cérebro humano, que aprendem padrões a partir de dados para realizar tarefas como classificação, regressão, reconhecimento de imagens e previsão de séries temporais. A combinação de TensorFlow e Keras permite criar redes neurais de maneira simples e flexível.

### O que são TensorFlow e Keras?

- **TensorFlow**: uma biblioteca de código aberto da Google para criar modelos de aprendizado de máquina e redes neurais. É conhecida por sua eficiência e capacidade de executar modelos em CPUs, GPUs, e TPUs.
- **Keras**: uma API de alto nível integrada ao TensorFlow, projetada para ser amigável e fácil de usar, facilitando a criação e treino de modelos de redes neurais com menos linhas de código.

### Estrutura de uma Rede Neural Básica

Uma rede neural básica é composta de:
1. **Camada de Entrada**: recebe os dados de entrada (ex.: imagem, texto, número).
2. **Camadas Ocultas**: processam os dados usando neurônios e funções de ativação.
3. **Camada de Saída**: gera o resultado final (ex.: classe de uma imagem, valor de regressão).

### Exemplo 1: Classificação de Dígitos com MNIST

Vamos criar uma rede neural simples para classificar imagens de dígitos usando o dataset MNIST. Esse conjunto contém imagens de dígitos manuscritos (0 a 9) em escala de cinza com 28x28 pixels.

#### Passo a Passo

1. **Importe as bibliotecas**:
```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
```

2. **Carregar e preparar os dados**:
```python
# Carregue o dataset MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize as imagens (valores entre 0 e 1)
x_train, x_test = x_train / 255.0, x_test / 255.0

# Converta as etiquetas para o formato "one-hot"
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
```

3. **Definir a estrutura da rede neural**:
```python
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Transforma a imagem 28x28 em um vetor 784
    Dense(128, activation='relu'),  # Primeira camada oculta com 128 neurônios
    Dense(64, activation='relu'),   # Segunda camada oculta com 64 neurônios
    Dense(10, activation='softmax') # Camada de saída para 10 classes (0 a 9)
])
```

4. **Compilar o modelo**:
```python
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])
```

5. **Treinar o modelo**:
```python
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2)
```

6. **Avaliar o modelo**:
```python
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Loss: {loss}, Accuracy: {accuracy}")
```

Esse código cria uma rede neural totalmente conectada (rede densa) para classificar dígitos de 0 a 9 com cerca de 98% de precisão.

### Exemplo 2: Regressão Linear com TensorFlow e Keras

Vamos agora ver um exemplo de regressão linear, que usa uma rede neural com uma única saída para prever valores contínuos.

#### Passo a Passo

1. **Importar bibliotecas e gerar dados**:
```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Gera dados fictícios para regressão
x_train = np.linspace(0, 10, 100)
y_train = 3 * x_train + 7 + np.random.normal(0, 1, 100)  # y = 3x + 7 + ruído
```

2. **Definir o modelo de regressão linear**:
```python
model = Sequential([
    Dense(1, input_shape=(1,))  # Camada com um neurônio para saída contínua
])
```

3. **Compilar o modelo**:
```python
model.compile(optimizer='adam', loss='mse')  # mse: erro quadrático médio
```

4. **Treinar o modelo**:
```python
model.fit(x_train, y_train, epochs=100)
```

5. **Testar o modelo com novos dados**:
```python
x_test = np.array([11, 12, 13])
y_pred = model.predict(x_test)
print(f"Previsões para {x_test}: {y_pred}")
```

### Exemplo 3: Rede Neural Convolucional (CNN) para Reconhecimento de Imagens

Redes neurais convolucionais (CNNs) são ideais para reconhecimento de imagens, pois extraem características espaciais dos dados.

#### Passo a Passo

1. **Importe as bibliotecas**:
```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
```

2. **Carregar e preparar os dados**:
```python
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
```

3. **Definir a estrutura da CNN**:
```python
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),  # 32 filtros 3x3
    MaxPooling2D((2, 2)),                                              # Pooling 2x2
    Conv2D(64, (3, 3), activation='relu'),                            # 64 filtros 3x3
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])
```

4. **Compilar e treinar o modelo**:
```python
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2)
```

5. **Avaliar o modelo**:
```python
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Loss: {loss}, Accuracy: {accuracy}")
```

Este exemplo usa uma CNN para reconhecer dígitos, aproveitando a arquitetura de camadas convolucionais e de pooling para processar as características da imagem.

Esses exemplos mostram redes neurais para diferentes tarefas. Experimente com parâmetros, número de neurônios e camadas para ver como isso afeta o desempenho dos modelos!
