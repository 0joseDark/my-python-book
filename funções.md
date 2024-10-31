Em Python, funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas permitem organizar o código em partes que podem ser chamadas várias vezes, tornando o programa mais modular e fácil de entender. Funções podem receber parâmetros (dados de entrada) e retornar valores como resultado.

### Como Definir uma Função:
1. Usamos a palavra-chave `def` seguida pelo nome da função.
2. Parênteses `()` são usados para listar os parâmetros (ou deixados vazios se não houver parâmetros).
3. Após o nome da função e os parênteses, usamos `:` e indentamos o bloco de código.
4. `return` pode ser usado para devolver um valor (opcional).

### Exemplo de Definição e Uso de Funções:

```python
# Definindo uma função que não recebe parâmetros e apenas imprime uma mensagem
def saudacao():
    print("Olá! Bem-vindo!")

# Chamando a função
saudacao()  # Saída: Olá! Bem-vindo!


# Definindo uma função que recebe parâmetros e calcula a soma
def soma(a, b):
    resultado = a + b
    return resultado  # Retorna o resultado da soma

# Chamando a função com argumentos
resultado_soma = soma(5, 3)
print("Resultado da soma:", resultado_soma)  # Saída: Resultado da soma: 8


# Definindo uma função que verifica se um número é par ou ímpar
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# Chamando a função e imprimindo o resultado
print("O número 4 é:", par_ou_impar(4))  # Saída: O número 4 é: Par
print("O número 7 é:", par_ou_impar(7))  # Saída: O número 7 é: Ímpar
```

### Explicação dos principais conceitos:
1. **Definição de função**: Usamos `def nome_da_funcao():` para definir a função.
2. **Parâmetros e argumentos**:
   - **Parâmetros** são variáveis dentro da definição da função (ex: `a`, `b`).
   - **Argumentos** são os valores passados quando chamamos a função (ex: `5`, `3`).
3. **Bloco de código**: O código da função é indentado para indicar que faz parte da função.
4. **Retorno de valor**: Usamos `return` para devolver um valor, que pode ser armazenado em uma variável.
5. **Chamando a função**: Para executar uma função, usamos seu nome seguido de `()` com os argumentos necessários.

### Vantagens das Funções:
- **Reutilização**: Podemos chamar a função quantas vezes quisermos.
- **Organização**: Deixam o código mais organizado e modular.
- **Facilidade de manutenção**: Alterações no código da função se aplicam a todas as suas chamadas.
