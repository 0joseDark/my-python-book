Decoradores em Python são funções especiais que permitem adicionar funcionalidade extra a outras funções ou métodos sem modificar o código original da função decorada. São amplamente usados para estender ou modificar o comportamento de funções de maneira clara e concisa.

### Como Funcionam os Decoradores?
Um decorador é uma função que recebe outra função como argumento, acrescenta alguma funcionalidade a ela e retorna uma nova função (ou a mesma função, com modificações). Usamos o símbolo `@` seguido do nome do decorador acima da função que queremos decorar.

### Exemplo Simples de um Decorador
Vamos criar um decorador chamado `meu_decorador` que adiciona uma mensagem antes e depois da execução de uma função.

```python
# Definindo o decorador
def meu_decorador(funcao):
    def funcao_decorada():
        print("Executando antes da função.")
        funcao()  # Chamando a função original
        print("Executando depois da função.")
    return funcao_decorada

# Usando o decorador com uma função
@meu_decorador
def saudacao():
    print("Olá!")

# Chamando a função decorada
saudacao()

# Saída:
# Executando antes da função.
# Olá!
# Executando depois da função.
```

### Explicação do Exemplo:
1. **Definindo o Decorador** (`meu_decorador`): Esta função recebe `funcao` como argumento e define uma função interna (`funcao_decorada`) que executa uma tarefa extra antes e depois de chamar `funcao`.
2. **Usando o Decorador** (`@meu_decorador`): A linha `@meu_decorador` é usada para aplicar o decorador à função `saudacao`. Isso significa que, quando chamamos `saudacao()`, ela será executada com o comportamento adicional definido em `meu_decorador`.
3. **Resultado**: Quando `saudacao()` é chamada, o decorador executa seu código antes e depois da função original.

### Decoradores com Argumentos
Muitas vezes, queremos decorar funções que aceitam argumentos. Para isso, precisamos modificar o decorador para que ele aceite e passe esses argumentos.

```python
# Decorador que aceita e passa argumentos para a função
def decorador_com_args(funcao):
    def funcao_decorada(*args, **kwargs):
        print("Argumentos recebidos:", args, kwargs)
        resultado = funcao(*args, **kwargs)  # Chamando a função original com seus argumentos
        print("Função executada com sucesso!")
        return resultado  # Retornando o resultado da função original
    return funcao_decorada

# Usando o decorador em uma função com argumentos
@decorador_com_args
def somar(a, b):
    return a + b

# Chamando a função decorada
print("Resultado da soma:", somar(3, 5))

# Saída:
# Argumentos recebidos: (3, 5) {}
# Função executada com sucesso!
# Resultado da soma: 8
```

### Explicação:
- **`*args` e `**kwargs`**: Estes permitem que o decorador aceite qualquer número de argumentos posicionais e nomeados, transmitindo-os para a função original.
- **Retornando valores**: O decorador também devolve o resultado da função original para ser usado conforme necessário.

### Aplicações Comuns dos Decoradores:
1. **Controle de acesso e autenticação**: Decoradores são usados para verificar se um usuário tem permissões para executar uma função específica.
2. **Log e debug**: Adicionar informações de log para monitorar quando e como funções são chamadas.
3. **Temporização**: Medir o tempo que uma função leva para executar.
4. **Cache**: Guardar os resultados de funções demoradas para uso posterior, economizando tempo de processamento.

Decoradores oferecem uma maneira poderosa e elegante de modificar o comportamento de funções em Python sem alterar o código original diretamente.
