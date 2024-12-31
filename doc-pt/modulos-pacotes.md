Em Python, **módulos** e **pacotes** são ferramentas de organização de código que permitem estruturar programas de forma modular, facilitando a manutenção, a reutilização e o compartilhamento de código.

### Módulos

Um módulo é um ficheiro que contém código Python. Pode incluir variáveis, funções, classes e declarações que podem ser reutilizadas em diferentes partes de um programa. Para criar um módulo, basta salvar o código num ficheiro com extensão `.py`. 

#### Exemplo de módulo

Vamos criar um módulo chamado `meu_modulo.py` com algumas funções:

```python
# meu_modulo.py

def saudacao(nome):
    return f"Olá, {nome}!"

def soma(a, b):
    return a + b
```

Para utilizar este módulo noutro ficheiro Python, usamos o comando `import`:

```python
# principal.py
import meu_modulo

print(meu_modulo.saudacao("Ana"))  # Saída: Olá, Ana!
print(meu_modulo.soma(5, 3))       # Saída: 8
```

Podemos também usar `from` para importar funções específicas:

```python
from meu_modulo import saudacao

print(saudacao("João"))  # Saída: Olá, João!
```

### Pacotes

Um pacote é uma coleção de módulos organizados numa pasta. A pasta que contém o pacote deve incluir um ficheiro especial chamado `__init__.py` (pode estar vazio), que indica ao Python que aquela pasta é um pacote.

#### Exemplo de pacote

Vamos criar um pacote chamado `meu_pacote` com o seguinte estrutura de ficheiros:

```
meu_pacote/
│
├── __init__.py
├── saudacoes.py
└── operacoes.py
```

- `saudacoes.py`

```python
def saudacao(nome):
    return f"Olá, {nome}!"
```

- `operacoes.py`

```python
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b
```

Podemos agora importar os módulos deste pacote noutro ficheiro Python:

```python
# principal.py
from meu_pacote import saudacoes, operacoes

print(saudacoes.saudacao("Maria"))  # Saída: Olá, Maria!
print(operacoes.soma(10, 5))        # Saída: 15
print(operacoes.subtracao(10, 5))   # Saída: 5
```

#### Importações Relativas e Absolutas

Num pacote, podemos fazer importações absolutas ou relativas:

- **Importação Absoluta**: Usamos o nome completo do pacote, como `from meu_pacote import saudacoes`.
- **Importação Relativa**: Usamos `.` para se referir ao módulo atual ou `..` para o módulo pai. Exemplo: `from . import saudacoes` (usado dentro do próprio pacote).

### Vantagens de Módulos e Pacotes

1. **Organização**: Separar o código em módulos e pacotes torna o projeto mais legível e organizado.
2. **Reutilização**: Funções e classes em módulos e pacotes podem ser usadas em diferentes projetos.
3. **Manutenção**: É mais fácil fazer atualizações e correções num módulo do que num código grande.

### Exemplo Completo

Suponha que estamos a desenvolver uma aplicação para uma calculadora e temos vários pacotes:

```
calculadora/
│
├── __init__.py
├── basico/
│   ├── __init__.py
│   ├── adicao.py
│   ├── subtracao.py
│
├── avancado/
│   ├── __init__.py
│   ├── raiz_quadrada.py
│   └── potencia.py
```

- `basico/adicao.py`

```python
def adicao(a, b):
    return a + b
```

- `basico/subtracao.py`

```python
def subtracao(a, b):
    return a - b
```

- `avancado/raiz_quadrada.py`

```python
import math

def raiz_quadrada(x):
    return math.sqrt(x)
```

- `avancado/potencia.py`

```python
def potencia(base, expoente):
    return base ** expoente
```

No ficheiro principal:

```python
# principal.py
from calculadora.basico import adicao, subtracao
from calculadora.avancado import raiz_quadrada, potencia

print(adicao.adicao(10, 5))            # Saída: 15
print(subtracao.subtracao(10, 5))      # Saída: 5
print(raiz_quadrada.raiz_quadrada(16)) # Saída: 4.0
print(potencia.potencia(2, 3))         # Saída: 8
```

Desta forma, a aplicação calculadora está organizada em módulos e pacotes, facilitando o entendimento e a expansão da aplicação.

Esses exemplos mostram como módulos e pacotes estruturam o código em Python, promovendo reutilização e organização.