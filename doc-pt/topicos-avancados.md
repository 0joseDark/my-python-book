# Python Avançado

## 9.1 Programação Funcional

A programação funcional é um paradigma que trata a computação como a avaliação de funções matemáticas, evitando estados mutáveis e efeitos colaterais. Em Python, funções como `map()`, `filter()` e `reduce()` são comuns na programação funcional.

### Exemplo de `map()`, `filter()` e `reduce()`

```python
from functools import reduce

# Lista de números
numeros = [1, 2, 3, 4, 5]

# `map` aplica uma função a cada item da lista
dobros = list(map(lambda x: x * 2, numeros))
print("Dobros:", dobros)  # Output: [2, 4, 6, 8, 10]

# `filter` filtra itens com base numa condição
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)  # Output: [2, 4]

# `reduce` reduz a lista a um único valor, aplicando uma função cumulativa
soma = reduce(lambda x, y: x + y, numeros)
print("Soma:", soma)  # Output: 15
```

As funções de ordem superior (como `map`, `filter`, `reduce`) são essenciais para lidar com coleções de dados de forma concisa e funcional.

---

## 9.2 Geradores e Iteradores

Geradores são uma forma de criar iteradores em Python usando a palavra-chave `yield`. A vantagem dos geradores é que eles "produzem" valores sob demanda, o que permite economizar memória ao lidar com grandes volumes de dados.

### Exemplo de Gerador

```python
def contador(maximo):
    i = 1
    while i <= maximo:
        yield i
        i += 1

for numero in contador(5):
    print(numero)
# Output:
# 1
# 2
# 3
# 4
# 5
```

Neste exemplo, a função `contador` gera números até `maximo` e cada chamada do `yield` retorna um valor e pausa a função. Quando é chamado novamente, a execução continua de onde parou.

### Iteradores Customizados

Um iterador customizado é criado definindo as funções `__iter__()` e `__next__()` numa classe.

```python
class Contador:
    def __init__(self, maximo):
        self.maximo = maximo
        self.atual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual < self.maximo:
            self.atual += 1
            return self.atual
        raise StopIteration

# Usar o iterador
for numero in Contador(5):
    print(numero)
# Output:
# 1
# 2
# 3
# 4
# 5
```

---

## 9.3 Manipulação de Exceções Avançada

A manipulação de exceções avançada em Python envolve o uso de blocos `try-except`, incluindo `else` e `finally`, bem como a criação de exceções personalizadas.

### Exemplo de Manipulação Avançada de Exceções

```python
class ValorInvalidoError(Exception):
    pass

def dividir(a, b):
    try:
        if b == 0:
            raise ValorInvalidoError("Não é possível dividir por zero!")
        resultado = a / b
    except ValorInvalidoError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    else:
        print("Divisão bem-sucedida:", resultado)
    finally:
        print("Finalizando a operação")

# Teste da função
dividir(10, 0)
# Output:
# Erro: Não é possível dividir por zero!
# Finalizando a operação

dividir(10, 2)
# Output:
# Divisão bem-sucedida: 5.0
# Finalizando a operação
```

Neste exemplo, criamos uma exceção personalizada `ValorInvalidoError`. A função `dividir` verifica a possibilidade de erro e utiliza o bloco `finally` para realizar uma ação, independentemente de ocorrer ou não uma exceção.

---

## 9.4 Context Managers

Os context managers são usados para garantir que certos recursos sejam geridos corretamente, como arquivos e conexões, evitando vazamento de recursos. Em Python, são geralmente implementados usando a instrução `with`.

### Exemplo com `with` e Arquivos

```python
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Exemplo de uso de context manager com arquivos.")

# O arquivo é automaticamente fechado ao sair do bloco `with`
```

### Criando um Context Manager Customizado

Um context manager pode ser criado implementando os métodos `__enter__()` e `__exit__()` numa classe.

```python
class GerirArquivo:
    def __init__(self, nome, modo):
        self.nome = nome
        self.modo = modo
        self.arquivo = None

    def __enter__(self):
        self.arquivo = open(self.nome, self.modo)
        return self.arquivo

    def __exit__(self, tipo, valor, traceback):
        if self.arquivo:
            self.arquivo.close()

# Usando o context manager customizado
with GerirArquivo("custom.txt", "w") as arquivo:
    arquivo.write("Texto escrito com um context manager customizado.")
```

No exemplo acima, o `__enter__()` abre o arquivo e retorna-o para o bloco `with`, enquanto o `__exit__()` fecha o arquivo, garantindo que ele seja fechado mesmo se ocorrer uma exceção dentro do bloco `with`.

---
