- [voltar atrás](https://github.com/0joseDark/my-python-book/blob/main/index.md)
# Classes e Objetos em Python

## Classes
Uma classe é como uma "planta" ou "modelo" que define as características e comportamentos que um objeto terá. Pense nela como um molde para criar objetos.

### Estrutura Básica de uma Classe
```python
class NomeDaClasse:
    def __init__(self, parametros):  # Construtor
        self.atributos = parametros
    
    def metodos(self):  # Métodos
        # Ações que o objeto pode realizar
        pass
```

## Objetos
Um objeto é uma instância de uma classe. Se uma classe é o molde, o objeto é o produto final criado a partir desse molde.

### Exemplos Práticos

#### 1. Exemplo com Pessoa
```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Olá, eu sou {self.nome} e tenho {self.idade} anos!"
    
    def fazer_aniversario(self):
        self.idade += 1

# Criando objetos da classe Pessoa
pessoa1 = Pessoa("Maria", 25)
pessoa2 = Pessoa("João", 30)

print(pessoa1.apresentar())  # Saída: Olá, eu sou Maria e tenho 25 anos!
pessoa1.fazer_aniversario()
print(pessoa1.idade)  # Saída: 26
```

#### 2. Exemplo com Carro
```python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        self.ligado = False
    
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            return "Carro ligado!"
        return "O carro já está ligado!"
    
    def acelerar(self, valor):
        if self.ligado:
            self.velocidade += valor
            return f"Velocidade atual: {self.velocidade} km/h"
        return "Primeiro ligue o carro!"

# Criando objetos da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020)
carro_amigo = Carro("Honda", "Civic", 2021)

print(meu_carro.ligar())      # Saída: Carro ligado!
print(meu_carro.acelerar(20)) # Saída: Velocidade atual: 20 km/h
```

#### 3. Exemplo com Conta Bancária
```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor}")
            return f"Depósito de R${valor} realizado com sucesso!"
        return "Valor inválido para depósito!"
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R${valor}")
            return f"Saque de R${valor} realizado com sucesso!"
        return "Saldo insuficiente!"
    
    def ver_saldo(self):
        return f"Saldo atual: R${self.saldo}"

# Criando objetos da classe ContaBancaria
conta_maria = ContaBancaria("Maria", 1000)
conta_joao = ContaBancaria("João")

print(conta_maria.ver_saldo())     # Saída: Saldo atual: R$1000
print(conta_maria.sacar(500))      # Saída: Saque de R$500 realizado com sucesso!
print(conta_maria.depositar(200))  # Saída: Depósito de R$200 realizado com sucesso!
print(conta_maria.ver_saldo())     # Saída: Saldo atual: R$700
```

## Pontos Importantes sobre Classes e Objetos:

1. **Atributos**: São as características/propriedades do objeto
   - Definidos no método `__init__`
   - Acessados usando `self.nome_do_atributo`

2. **Métodos**: São as ações que o objeto pode realizar
   - São funções dentro da classe
   - Sempre recebem `self` como primeiro parâmetro

3. **Construtor**: O método `__init__`
   - Executado automaticamente ao criar um objeto
   - Inicializa os atributos do objeto

4. **Instanciação**: Processo de criar um objeto
   - Usa-se o nome da classe seguido de parênteses
   - Exemplo: `objeto = MinhaClasse()`

5. **self**: Referência ao próprio objeto
   - Usado para acessar atributos e métodos dentro da classe
   - Sempre é o primeiro parâmetro dos métodos

Cada objeto criado é independente dos outros, mesmo sendo da mesma classe. Isso significa que alterações em um objeto não afetam os outros objetos da mesma classe.
