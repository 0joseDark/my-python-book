Em Python, os números são um dos tipos de dados mais comuns e são divididos em três categorias principais:

1. **Inteiros (`int`)**: Números inteiros, sem parte decimal (exemplo: 1, -3, 100).
2. **Flutuantes (`float`)**: Números com ponto decimal (exemplo: 3.14, -0.5, 7.0).
3. **Complexos (`complex`)**: Números que possuem uma parte real e uma parte imaginária (exemplo: 2 + 3j, onde `j` representa a unidade imaginária).

### 1. Números Inteiros (`int`)

Os números inteiros são usados para representar valores inteiros, como 0, 5, -100, e são úteis para contagens, índices e muitas operações matemáticas básicas.

#### Exemplo de Declaração e Operações com Inteiros

```python
a = 10        # Número inteiro positivo
b = -3        # Número inteiro negativo
c = 0         # Zero é também considerado um inteiro

# Operações com inteiros
soma = a + b        # 10 + (-3) = 7
subtracao = a - b   # 10 - (-3) = 13
multiplicacao = a * b  # 10 * (-3) = -30
divisao_inteira = a // b  # 10 // -3 = -4 (divisão inteira)
resto = a % b         # 10 % -3 = -2 (módulo)
exponenciacao = a ** 2  # 10^2 = 100

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão Inteira:", divisao_inteira)
print("Resto:", resto)
print("Exponenciação:", exponenciacao)
```

### 2. Números Flutuantes (`float`)

Números flutuantes (ou "ponto flutuante") representam valores com parte decimal, sendo úteis para operações que precisam de precisão decimal, como cálculos financeiros e científicos.

#### Exemplo de Declaração e Operações com Flutuantes

```python
x = 3.14       # Número flutuante positivo
y = -0.5       # Número flutuante negativo
z = 5.0        # Float com valor inteiro (5.0 é um float)

# Operações com floats
soma = x + y           # 3.14 + (-0.5) = 2.64
subtracao = x - y      # 3.14 - (-0.5) = 3.64
multiplicacao = x * y  # 3.14 * (-0.5) = -1.57
divisao = x / y        # 3.14 / (-0.5) = -6.28

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
```

Python lida com números flutuantes usando a precisão dupla, o que permite armazenar decimais com boa precisão. No entanto, como em outras linguagens, as operações com `float` podem ter pequenas imprecisões devido ao modo como os números são armazenados internamente.

### 3. Números Complexos (`complex`)

Os números complexos em Python são representados como uma combinação de parte real e parte imaginária. A unidade imaginária é indicada pela letra `j`, então um número complexo `a + bj` é representado em Python como `complex(a, b)` ou diretamente com `a + bj`.

#### Exemplo de Declaração e Operações com Complexos

```python
num1 = 2 + 3j         # Número complexo (parte real: 2, parte imaginária: 3j)
num2 = 1 - 1.5j       # Outro número complexo

# Operações com números complexos
soma = num1 + num2    # (2 + 3j) + (1 - 1.5j) = 3 + 1.5j
subtracao = num1 - num2  # (2 + 3j) - (1 - 1.5j) = 1 + 4.5j
multiplicacao = num1 * num2  # Multiplicação complexa
divisao = num1 / num2        # Divisão complexa

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)

# Acessando a parte real e imaginária
print("Parte real de num1:", num1.real)
print("Parte imaginária de num1:", num1.imag)
```

### Convertendo entre Tipos de Dados Numéricos

Python permite converter entre `int`, `float`, e `complex` usando funções de conversão, mas com algumas restrições:

- Inteiros e floats podem ser convertidos livremente entre si.
- Inteiros e floats podem ser convertidos para complexos, mas complexos não podem ser convertidos diretamente para inteiros ou floats.

#### Exemplo de Conversão entre Tipos

```python
a = 10           # Inteiro
b = 3.5          # Float

# Convertendo de int para float
float_a = float(a)     # 10 -> 10.0

# Convertendo de float para int (perde a parte decimal)
int_b = int(b)         # 3.5 -> 3

# Convertendo para complex
complex_a = complex(a)     # 10 -> 10+0j
complex_b = complex(b)     # 3.5 -> 3.5+0j

print("Float de a:", float_a)
print("Int de b:", int_b)
print("Complexo de a:", complex_a)
print("Complexo de b:", complex_b)
```

### Resumo

| Tipo      | Descrição                            | Exemplo         |
|-----------|--------------------------------------|-----------------|
| **int**   | Número inteiro                       | `10`, `-3`, `0`|
| **float** | Número decimal                       | `3.14`, `-0.5` |
| **complex** | Número complexo com parte real e imaginária | `2 + 3j` |

Esses tipos de dados numéricos cobrem a maioria das necessidades em cálculos matemáticos em Python, desde operações simples até manipulação de números complexos em aplicações científicas.
