Funções recursivas são funções que **se chamam a si mesmas** para resolver um problema. A recursão é usada quando um problema pode ser dividido em subproblemas menores, de forma que cada um seja uma versão reduzida do original. É importante que uma função recursiva tenha uma **condição de parada** para evitar um loop infinito.

### Características das Funções Recursivas:
1. **Chamam a si mesmas**: Uma função recursiva usa o próprio nome dentro de sua definição.
2. **Condição de parada**: Define quando a função deve parar de chamar a si mesma.
3. **Dividir para conquistar**: Cada chamada trabalha em uma versão reduzida do problema.

### Exemplo Clássico: Cálculo do Fatorial
O fatorial de um número `n` (escrito como `n!`) é o produto de todos os inteiros positivos até `n`. Por exemplo, `5! = 5 * 4 * 3 * 2 * 1 = 120`. Podemos definir o fatorial recursivamente como:
- Base: `0! = 1`
- Passo recursivo: `n! = n * (n - 1)!`

### Exemplo de Função Recursiva para Calcular Fatorial:

```python
# Função recursiva para calcular o fatorial de um número
def fatorial(n):
    # Condição de parada: quando n é 0 ou 1, o fatorial é 1
    if n == 0 or n == 1:
        return 1
    else:
        # Passo recursivo: n * fatorial de (n - 1)
        return n * fatorial(n - 1)

# Chamando a função com um exemplo
numero = 5
resultado = fatorial(numero)
print(f"Fatorial de {numero} é: {resultado}")  # Saída: Fatorial de 5 é: 120
```

### Explicação do Código:
1. **Condição de Parada** (`if n == 0 or n == 1`): Quando `n` é 0 ou 1, a função retorna 1 sem fazer uma nova chamada.
2. **Passo Recursivo** (`n * fatorial(n - 1)`): A função chama a si mesma com um valor menor de `n`, acumulando o resultado até alcançar a condição de parada.
3. **Chamada Recursiva**: A cada chamada, a função calcula o fatorial para um número menor, até atingir 1.

### Outro Exemplo: Sequência de Fibonacci
A sequência de Fibonacci é definida recursivamente como:
- `fibonacci(0) = 0`
- `fibonacci(1) = 1`
- `fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)` para `n > 1`

```python
# Função recursiva para calcular o n-ésimo número de Fibonacci
def fibonacci(n):
    # Condições de parada
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Passo recursivo
        return fibonacci(n - 1) + fibonacci(n - 2)

# Chamando a função com um exemplo
termo = 6
resultado_fibonacci = fibonacci(termo)
print(f"O {termo}º número de Fibonacci é: {resultado_fibonacci}")  # Saída: O 6º número de Fibonacci é: 8
```

### Explicação do Código:
1. **Condições de Parada** (`if n == 0` e `elif n == 1`): A função retorna 0 ou 1 diretamente para os primeiros termos da sequência.
2. **Passo Recursivo**: A função chama a si mesma para `n - 1` e `n - 2`, somando os resultados até alcançar a condição de parada.
3. **Empilhamento das chamadas**: Cada chamada recursiva depende do resultado de outra, empilhando chamadas até que as condições de parada sejam atendidas.

### Cuidados ao Usar Funções Recursivas:
- **Condição de Parada**: Garantir que sempre haja uma condição de parada.
- **Desempenho**: Funções recursivas podem consumir mais memória e serem lentas para problemas grandes, por isso otimize com técnicas como memoização, quando necessário.
