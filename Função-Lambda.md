- [voltar atrás](https://github.com/0joseDark/my-python-book/blob/main/index.md)
- Funções Lambda em Python são funções anônimas, ou seja, funções que não têm um nome específico. Elas são definidas usando a palavra-chave `lambda`, e são normalmente usadas para criar funções curtas e simples que realizam uma operação rápida. Diferente de uma função normal, uma função lambda é composta de apenas uma expressão, e o valor dessa expressão é automaticamente retornado.

### Características das Funções Lambda:
1. **Sintaxe compacta**: São escritas em uma única linha.
2. **Sem nome**: São funções anônimas, geralmente usadas em situações onde funções pequenas são necessárias.
3. **Uso comum**: São frequentemente usadas com funções como `map()`, `filter()`, e `sorted()`, que aplicam a função a uma sequência de elementos.

### Estrutura de uma Função Lambda:
A estrutura básica de uma função lambda é:
```python
lambda argumentos: expressão
```
- **`argumentos`**: Os parâmetros que a função recebe.
- **`expressão`**: A operação ou cálculo que a função realiza e retorna.

### Exemplo de Função Lambda:

```python
# Definindo uma função lambda que soma dois números
soma = lambda a, b: a + b

# Chamando a função lambda
resultado = soma(3, 5)
print("Resultado da soma:", resultado)  # Saída: Resultado da soma: 8
```

### Exemplos de Uso Comum das Funções Lambda

#### 1. Usando Lambda com `map()`:
`map()` aplica uma função a cada item em uma lista.

```python
# Lista de números
numeros = [1, 2, 3, 4]

# Usando lambda para elevar cada número ao quadrado
quadrados = list(map(lambda x: x ** 2, numeros))
print("Quadrados:", quadrados)  # Saída: Quadrados: [1, 4, 9, 16]
```

#### 2. Usando Lambda com `filter()`:
`filter()` usa uma função para filtrar uma lista com base em uma condição.

```python
# Filtrando números pares de uma lista
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)  # Saída: Números pares: [2, 4, 6]
```

#### 3. Usando Lambda para Ordenar com `sorted()`:
Usando uma função lambda como chave para ordenar uma lista.

```python
# Lista de tuplas com nome e idade
pessoas = [("João", 30), ("Ana", 25), ("Carlos", 20)]

# Ordenando pela idade
pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa[1])
print("Pessoas ordenadas por idade:", pessoas_ordenadas)
# Saída: Pessoas ordenadas por idade: [('Carlos', 20), ('Ana', 25), ('João', 30)]
```

### Explicação dos Conceitos:
1. **Função Lambda**: Definida em uma linha, com `lambda argumentos: expressão`.
2. **Aplicações Comuns**:
   - **`map()`**: Aplica a função a cada elemento de uma lista.
   - **`filter()`**: Retorna apenas os elementos que atendem à condição da função.
   - **`sorted()`**: Usa a função como critério de ordenação.
3. **Leve e eficiente**: Lambdas são úteis para operações rápidas e simples, sem a necessidade de definir uma função completa.
