- [voltar atrás](https://github.com/0joseDark/my-python-book/blob/main/index.md)
- Em Python, **parâmetros** e **argumentos** são conceitos fundamentais para o funcionamento de funções. 

### Diferença entre Parâmetros e Argumentos:
- **Parâmetros**: São os nomes usados na definição de uma função. São variáveis que "esperam" receber valores quando a função é chamada.
- **Argumentos**: São os valores reais que passamos para uma função quando a chamamos.

### Exemplo Básico:

```python
# Função com parâmetros
def saudacao(nome, idade):  # 'nome' e 'idade' são parâmetros
    print(f"Olá, {nome}! Você tem {idade} anos.")

# Chamando a função com argumentos
saudacao("Ana", 30)  # "Ana" e 30 são argumentos
```

#### Explicação do Exemplo:
- Na definição da função `saudacao`, `nome` e `idade` são **parâmetros**.
- Quando chamamos a função com `saudacao("Ana", 30)`, `"Ana"` e `30` são **argumentos** que substituem os parâmetros.

### Tipos de Argumentos em Python:

#### 1. Argumentos Posicionais:
Os argumentos são passados para a função na mesma ordem dos parâmetros.

```python
def multiplicar(a, b):
    return a * b

print(multiplicar(3, 5))  # Saída: 15
```

#### 2. Argumentos Nomeados (ou Keywords):
Esses argumentos especificam o nome do parâmetro, tornando a ordem dos argumentos irrelevante.

```python
def dividir(a, b):
    return a / b

print(dividir(b=10, a=50))  # Saída: 5.0
```

#### 3. Argumentos Padrão:
Podemos definir valores padrão para parâmetros. Assim, se um argumento não for passado, o valor padrão será usado.

```python
def apresentar(nome, saudacao="Olá"):
    print(f"{saudacao}, {nome}!")

apresentar("João")           # Saída: Olá, João!
apresentar("Ana", "Bem-vinda")  # Saída: Bem-vinda, Ana!
```

#### 4. Argumentos Arbitrários:
Usamos `*args` para aceitar múltiplos argumentos posicionais e `**kwargs` para múltiplos argumentos nomeados.

```python
# Usando *args para argumentos posicionais arbitrários
def soma(*args):
    total = sum(args)
    print("Soma:", total)

soma(1, 2, 3, 4)  # Saída: Soma: 10

# Usando **kwargs para argumentos nomeados arbitrários
def mostrar_detalhes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrar_detalhes(nome="Maria", idade=28, cidade="Lisboa")
# Saída:
# nome: Maria
# idade: 28
# cidade: Lisboa
```

### Resumo:
1. **Parâmetros**: Variáveis na definição de uma função.
2. **Argumentos**: Valores passados para a função.
3. **Tipos de Argumentos**:
   - Posicionais
   - Nomeados
   - Com valores padrão
   - Arbitrários (`*args` e `**kwargs`)
