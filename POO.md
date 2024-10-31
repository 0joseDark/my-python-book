# Programação Orientada a Objetos (POO) em Python

A POO é um paradigma de programação que organiza o código em objetos que contêm dados e código. Os objetos são instâncias de classes, que podem ser vistas como "plantas" ou modelos para criar objetos.

## Conceitos Principais

### 1. Classe
Uma classe é um modelo para criar objetos. Define os atributos e métodos que os objetos terão.

```python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
```

### 2. Objeto
Um objeto é uma instância de uma classe.

```python
meu_carro = Carro("Toyota", "Corolla", 2020)
```

### 3. Encapsulamento
Protege os dados dentro de um objeto e esconde os detalhes de implementação.

```python
class ContaBancaria:
    def __init__(self):
        self.__saldo = 0  # atributo privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def consultar_saldo(self):
        return self.__saldo
```

### 4. Herança
Permite que uma classe herde atributos e métodos de outra classe.

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"
```

### 5. Polimorfismo
Permite que objetos de diferentes classes sejam tratados de maneira uniforme.

```python
def fazer_animal_som(animal):
    print(animal.fazer_som())

rex = Cachorro("Rex")
felix = Gato("Felix")

fazer_animal_som(rex)    # Imprime: Au au!
fazer_animal_som(felix)  # Imprime: Miau!
```

## Exemplo Completo
Aqui está um exemplo mais completo que utiliza todos estes conceitos:

```python
class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario
    
    def get_nome(self):
        return self.__nome
    
    def get_salario(self):
        return self.__salario
    
    def calcular_bonus(self):
        return self.__salario * 0.1

class Gerente(Funcionario):
    def __init__(self, nome, salario, senha):
        super().__init__(nome, salario)
        self.__senha = senha
    
    def calcular_bonus(self):  # sobrescrevendo o método da classe pai
        return self.get_salario() * 0.2

# Usando as classes
funcionario = Funcionario("João", 3000)
gerente = Gerente("Maria", 5000, "123456")

print(f"Bônus do {funcionario.get_nome()}: R${funcionario.calcular_bonus()}")
print(f"Bônus da {gerente.get_nome()}: R${gerente.calcular_bonus()}")
```

### Principais Benefícios da POO:
1. Reutilização de código
2. Organização e estruturação do código
3. Manutenibilidade
4. Flexibilidade e extensibilidade
