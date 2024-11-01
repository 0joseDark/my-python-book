- [voltar atrás](https://github.com/0joseDark/my-python-book/blob/main/index.md)
# Métodos e Atributos em POO (Python)

## Atributos
São as características ou propriedades que um objeto possui. Funcionam como variáveis dentro da classe.

### Tipos de Atributos:

#### 1. Atributos de Instância
- Específicos para cada objeto
- Definidos usando `self`
- Podem ter valores diferentes para cada objeto

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome    # Atributo de instância
        self.idade = idade  # Atributo de instância
```

#### 2. Atributos de Classe
- Compartilhados por todos os objetos
- Definidos fora do `__init__`
- Mesmo valor para todos os objetos

```python
class Funcionario:
    empresa = "TechCorp"  # Atributo de classe
    
    def __init__(self, nome, salario):
        self.nome = nome      # Atributo de instância
        self.salario = salario
```

#### 3. Atributos Privados
- Começam com dois underscores (`__`)
- Não devem ser acessados diretamente fora da classe

```python
class ContaBancaria:
    def __init__(self, titular):
        self.__saldo = 0      # Atributo privado
        self.titular = titular # Atributo público
```

## Métodos
São as funções que definem o comportamento dos objetos da classe.

### Tipos de Métodos:

#### 1. Métodos de Instância
- Acessam e modificam atributos do objeto
- Primeiro parâmetro é sempre `self`

```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0
    
    def acelerar(self, valor):  # Método de instância
        self.velocidade += valor
        return f"Velocidade atual: {self.velocidade}km/h"
    
    def frear(self):  # Método de instância
        self.velocidade = 0
        return "Carro parado"
```

#### 2. Métodos de Classe
- Decorados com `@classmethod`
- Primeiro parâmetro é `cls` (a própria classe)
- Podem acessar atributos de classe

```python
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    @classmethod
    def hoje(cls):  # Método de classe
        from datetime import date
        hoje = date.today()
        return cls(hoje.day, hoje.month, hoje.year)
```

#### 3. Métodos Estáticos
- Decorados com `@staticmethod`
- Não recebem `self` nem `cls`
- Não acessam atributos da classe/instância

```python
class Matematica:
    @staticmethod
    def somar(x, y):  # Método estático
        return x + y
    
    @staticmethod
    def multiplicar(x, y):  # Método estático
        return x * y
```

## Exemplo Completo
```python
class Estudante:
    escola = "Escola Python"  # Atributo de classe
    
    def __init__(self, nome, idade):
        self.nome = nome      # Atributo público de instância
        self.idade = idade    # Atributo público de instância
        self.__notas = []     # Atributo privado de instância
    
    def adicionar_nota(self, nota):  # Método de instância
        if 0 <= nota <= 10:
            self.__notas.append(nota)
            return "Nota adicionada com sucesso!"
        return "Nota inválida!"
    
    def calcular_media(self):  # Método de instância
        if self.__notas:
            return sum(self.__notas) / len(self.__notas)
        return 0
    
    @classmethod
    def mudar_escola(cls, nova_escola):  # Método de classe
        cls.escola = nova_escola
    
    @staticmethod
    def e_maior_idade(idade):  # Método estático
        return idade >= 18

# Usando a classe
aluno1 = Estudante("Ana", 16)
aluno2 = Estudante("Pedro", 17)

# Usando métodos de instância
print(aluno1.adicionar_nota(8.5))
print(aluno1.adicionar_nota(9.0))
print(f"Média do aluno: {aluno1.calcular_media()}")

# Usando método de classe
Estudante.mudar_escola("Nova Escola Python")
print(f"Nova escola: {Estudante.escola}")

# Usando método estático
print(f"Ana é maior de idade? {Estudante.e_maior_idade(aluno1.idade)}")
```

## Boas Práticas:

1. **Encapsulamento**
   - Use atributos privados quando necessário
   - Crie métodos para acessar e modificar atributos privados

2. **Nomenclatura**
   - Nomes de classes em CamelCase
   - Nomes de métodos e atributos em snake_case

3. **Documentação**
   - Use docstrings para documentar classes e métodos
   - Explique parâmetros e retornos

4. **Responsabilidade**
   - Cada método deve ter uma única responsabilidade
   - Mantenha métodos curtos e focados
