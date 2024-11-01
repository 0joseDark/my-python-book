- [voltar atrás](https://github.com/0joseDark/my-python-book/blob/main/index.md)
# Herança em POO (Python)

Herança é um conceito que permite criar uma nova classe baseada em uma classe existente. A nova classe (subclasse) herda atributos e métodos da classe original (superclasse), permitindo reutilização de código e estabelecendo uma relação "é um" entre classes.

## Tipos de Herança

### 1. Herança Simples
Uma classe herda de uma única classe base.

```python
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def emitir_som(self):
        return "Som genérico de animal"
    
    def apresentar(self):
        return f"Eu sou {self.nome} e tenho {self.idade} anos"

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)  # Chama o construtor da classe pai
        self.raca = raca
    
    def emitir_som(self):  # Sobrescrevendo o método da classe pai
        return "Au au!"
    
    def abanar_rabo(self):  # Método específico de Cachorro
        return "Abanando o rabo!"

# Usando as classes
rex = Cachorro("Rex", 3, "Pastor Alemão")
print(rex.apresentar())     # Método herdado
print(rex.emitir_som())     # Método sobrescrito
print(rex.abanar_rabo())    # Método específico
```

### 2. Herança Múltipla
Uma classe herda de várias classes base.

```python
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def calcular_pagamento(self):
        return self.salario

class Artista:
    def __init__(self, especialidade):
        self.especialidade = especialidade
    
    def performar(self):
        return f"Realizando performance de {self.especialidade}"

class ArtistaFuncionario(Funcionario, Artista):
    def __init__(self, nome, salario, especialidade):
        Funcionario.__init__(self, nome, salario)
        Artista.__init__(self, especialidade)
    
    def calcular_pagamento(self):
        # Sobrescrevendo para adicionar bônus
        return self.salario + 1000

# Usando a classe
artista1 = ArtistaFuncionario("João", 3000, "música")
print(artista1.calcular_pagamento())  # Método sobrescrito
print(artista1.performar())           # Método herdado de Artista
```

### 3. Exemplo com Hierarquia de Veículos

```python
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
    
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            return "Veículo ligado"
        return "Veículo já está ligado"
    
    def desligar(self):
        if self.ligado:
            self.ligado = False
            return "Veículo desligado"
        return "Veículo já está desligado"

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self.num_portas = num_portas
        self.marcha = 0
    
    def trocar_marcha(self, marcha):
        if 0 <= marcha <= 5:
            self.marcha = marcha
            return f"Marcha alterada para {marcha}"
        return "Marcha inválida"

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada
    
    def empinar(self):
        if self.ligado:
            return "Empinando a moto! (Cuidado!)"
        return "Primeiro ligue a moto!"

# Usando as classes
carro = Carro("Toyota", "Corolla", 2020, 4)
moto = Moto("Honda", "CB500", 2021, 500)

print(carro.ligar())          # Método herdado
print(carro.trocar_marcha(3)) # Método específico
print(moto.ligar())           # Método herdado
print(moto.empinar())         # Método específico
```

### 4. Exemplo com Sistema Bancário

```python
class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo  # Protected
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return f"Depósito de R${valor} realizado"
    
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            return f"Saque de R${valor} realizado"
        return "Saldo insuficiente"
    
    def ver_saldo(self):
        return f"Saldo: R${self._saldo}"

class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0, taxa_juros=0.005):
        super().__init__(numero, titular, saldo)
        self.taxa_juros = taxa_juros
    
    def aplicar_juros(self):
        juros = self._saldo * self.taxa_juros
        self._saldo += juros
        return f"Juros de R${juros:.2f} aplicados"

class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000):
        super().__init__(numero, titular, saldo)
        self.limite = limite
    
    def sacar(self, valor):  # Sobrescrevendo o método sacar
        if valor <= (self._saldo + self.limite):
            self._saldo -= valor
            return f"Saque de R${valor} realizado"
        return "Limite insuficiente"

# Usando as classes
poupanca = ContaPoupanca("001", "Maria", 1000)
corrente = ContaCorrente("002", "João", 500)

print(poupanca.depositar(500))    # Método herdado
print(poupanca.aplicar_juros())   # Método específico
print(corrente.sacar(1000))       # Método sobrescrito
print(corrente.ver_saldo())       # Método herdado
```

## Pontos Importantes sobre Herança:

1. **super()**
   - Usado para chamar métodos da classe pai
   - Importante em construtores para inicialização correta

2. **Sobrescrita de Métodos**
   - Permite modificar comportamento herdado
   - Mantém a mesma assinatura do método original

3. **Herança Múltipla**
   - Python permite herdar de várias classes
   - Cuidado com conflitos de nomes

4. **Princípio da Substituição de Liskov**
   - Subclasses devem poder substituir suas classes base
   - Mantenha comportamento consistente

5. **Composição vs Herança**
   - Use herança para relação "é um"
   - Prefira composição para relação "tem um"
