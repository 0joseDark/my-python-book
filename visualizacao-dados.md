A visualização de dados é uma técnica essencial para entender e comunicar insights de dados de maneira clara e eficaz. Em Python, o **Matplotlib** e o **Seaborn** são duas das bibliotecas mais populares para visualização de dados. Vamos ver alguns exemplos básicos usando ambas as bibliotecas.

### 1. Matplotlib

O **Matplotlib** é uma biblioteca versátil que oferece controle detalhado sobre gráficos. Ele é frequentemente usado para gráficos de linhas, barras, histogramas, entre outros.

#### Exemplo: Gráfico de Linhas com Matplotlib

```python
import matplotlib.pyplot as plt
import numpy as np

# Dados para o gráfico
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Criar o gráfico de linha
plt.plot(x, y, label='Seno')
plt.title('Gráfico de Linha com Matplotlib')
plt.xlabel('X')
plt.ylabel('Seno(X)')
plt.legend()
plt.grid(True)
plt.show()
```

#### Exemplo: Gráfico de Barras com Matplotlib

```python
import matplotlib.pyplot as plt

# Dados
categorias = ['A', 'B', 'C', 'D']
valores = [4, 7, 1, 8]

# Criar o gráfico de barras
plt.bar(categorias, valores, color='skyblue')
plt.title('Gráfico de Barras com Matplotlib')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.show()
```

### 2. Seaborn

O **Seaborn** é construído em cima do Matplotlib e facilita a criação de visualizações estatísticas. Ele é especialmente útil para gráficos mais complexos e analíticos.

#### Exemplo: Gráfico de Dispersão com Seaborn

O gráfico de dispersão é útil para visualizar a relação entre duas variáveis.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Gerar dados
np.random.seed(0)
x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.1, 100)

# Criar o gráfico de dispersão
sns.scatterplot(x=x, y=y)
plt.title('Gráfico de Dispersão com Seaborn')
plt.xlabel('Variável X')
plt.ylabel('Variável Y')
plt.show()
```

#### Exemplo: Histograma com Seaborn

Os histogramas são úteis para visualizar a distribuição de uma variável.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Gerar dados
dados = np.random.normal(loc=0, scale=1, size=1000)

# Criar o histograma
sns.histplot(dados, kde=True, color='purple')
plt.title('Histograma com Seaborn')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.show()
```

### 3. Comparando Gráficos com Seaborn e Matplotlib

Seaborn também pode ser combinado com Matplotlib para ajustar detalhes específicos do gráfico.

#### Exemplo: Gráfico de Linha com Estilização Seaborn e Ajuste Matplotlib

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configuração do estilo
sns.set(style="whitegrid")

# Dados
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Gráfico com Matplotlib e estilização Seaborn
plt.plot(x, y1, label='Seno', color='blue')
plt.plot(x, y2, label='Cosseno', color='orange')
plt.title('Gráfico de Linha com Seaborn e Matplotlib')
plt.xlabel('X')
plt.ylabel('Função')
plt.legend()
plt.show()
```

### Resumo

- **Matplotlib** é ótimo para gráficos básicos e oferece mais controle sobre detalhes.
- **Seaborn** facilita gráficos estatísticos e traz uma estética aprimorada.
- **Combinação dos dois** permite criar visualizações customizadas e elegantes.
