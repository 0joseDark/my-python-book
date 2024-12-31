As variáveis e tipos de dados são elementos fundamentais em Python, pois permitem armazenar e manipular informações no programa. Vamos ver como declarar variáveis, os principais tipos de dados e alguns exemplos de uso.

### 1. O Que São Variáveis?

Uma variável é um espaço na memória onde armazenamos dados. Em Python, para criar uma variável, basta atribuir um valor a um nome. Python usa tipagem dinâmica, o que significa que o tipo da variável é automaticamente definido pelo valor atribuído a ela.

### Exemplo de Declaração de Variáveis

```python
nome = "Maria"  # Variável do tipo string
idade = 25      # Variável do tipo inteiro
altura = 1.68   # Variável do tipo float
ativo = True    # Variável do tipo booleano
```

### 2. Tipos de Dados Básicos

Aqui estão os tipos de dados mais comuns em Python:

- **String (`str`)**: representa texto.
- **Inteiro (`int`)**: representa números inteiros.
- **Ponto Flutuante (`float`)**: representa números decimais.
- **Booleano (`bool`)**: representa valores lógicos (`True` ou `False`).

#### Exemplo de Cada Tipo

```python
nome = "Python"         # String
idade = 30              # Inteiro
altura = 1.75           # Float
ativo = True            # Booleano
```

### 3. Tipos de Dados Compostos

Python também tem tipos de dados compostos, como listas, tuplas, e dicionários.

- **Lista (`list`)**: coleção ordenada e mutável de elementos.
- **Tupla (`tuple`)**: coleção ordenada e imutável de elementos.
- **Dicionário (`dict`)**: coleção de pares chave-valor.

#### Exemplo de Lista, Tupla e Dicionário

```python
# Lista
frutas = ["maçã", "banana", "laranja"]

# Tupla
cores = ("vermelho", "azul", "verde")

# Dicionário
aluno = {
    "nome": "Ana",
    "idade": 20,
    "curso": "Engenharia"
}
```

### 4. Trabalhando com Variáveis e Tipos de Dados

#### Operações Básicas

Você pode realizar operações matemáticas em variáveis inteiras e de ponto flutuante.

```python
a = 10
b = 3

soma = a + b           # 13
subtracao = a - b      # 7
multiplicacao = a * b  # 30
divisao = a / b        # 3.333...
divisao_inteira = a // b  # 3
resto = a % b          # 1
exponenciacao = a ** b # 1000
```

#### Concatenando Strings

Com strings, é possível concatenar (juntar) textos usando o operador `+`.

```python
saudacao = "Olá"
nome = "Maria"
mensagem = saudacao + ", " + nome + "!"
print(mensagem)  # Saída: "Olá, Maria!"
```

#### Conversão Entre Tipos

Você pode converter variáveis entre tipos usando funções como `int()`, `float()`, `str()` e `bool()`.

```python
numero_str = "123"
numero_int = int(numero_str)  # Converte de string para inteiro
altura = 1.75
altura_str = str(altura)      # Converte de float para string
```

### 5. Exemplo Completo: Calculando a Área de um Retângulo

Vamos juntar esses conceitos para criar um programa que calcula a área de um retângulo.

```python
# Entrada de dados
largura = float(input("Digite a largura do retângulo (em metros): "))
altura = float(input("Digite a altura do retângulo (em metros): "))

# Cálculo da área
area = largura * altura

# Exibição do resultado
print("A área do retângulo é:", area, "metros quadrados.")
```

### 6. Exemplo com Variáveis e Dicionários: Cadastro de Aluno

Aqui vamos criar um programa que coleta dados de um aluno e armazena em um dicionário.

```python
# Coletando dados
nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
curso = input("Digite o curso do aluno: ")

# Armazenando os dados em um dicionário
aluno = {
    "nome": nome,
    "idade": idade,
    "curso": curso
}

# Exibindo os dados
print("\nCadastro do Aluno:")
print("Nome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Curso:", aluno["curso"])
```

### 7. Exemplo com Tipos de Dados Compostos: Lista de Notas

Neste exemplo, criamos uma lista para armazenar as notas de um aluno e calculamos a média.

```python
# Lista de notas
notas = [7.5, 8.0, 6.5, 9.0, 8.5]

# Cálculo da média
media = sum(notas) / len(notas)

# Exibindo a média
print("As notas do aluno são:", notas)
print("A média das notas é:", media)
```

Esses exemplos demonstram como utilizar variáveis e tipos de dados em Python para armazenar, manipular e exibir informações de maneira prática. Com esses conceitos, você já consegue criar programas básicos e funcionais.
