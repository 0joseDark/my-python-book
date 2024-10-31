# Polimorfismo em POO (Python)

Polimorfismo é a capacidade de objetos de diferentes classes responderem à mesma mensagem (método) de maneiras diferentes. Em Python, existem dois tipos principais de polimorfismo.

## 1. Polimorfismo de Sobrescrita (Override)
Ocorre quando uma classe filha fornece uma implementação específica para um método já definido na classe pai.

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        return "Som genérico"
    
    def apresentar(self):
        return f"Eu sou {self.nome} e faço: {self.fazer_som()}"

class Cachorro(Animal):
    def fazer_som(self):  # Sobrescrevendo o método
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):  # Sobrescrevendo o método
        return "Miau!"

class Pato(Animal):
    def fazer_som(self):  # Sobrescrevendo o método
        return "Quack!"

# Usando o polimorfismo
animais = [
    Cachorro("Rex"),
    Gato("Felix"),
    Pato("Donald")
]

for animal in animais:
    print(animal.apresentar())
```

## 2. Polimorfismo de Sobrecarga (Overload)
Em Python, não existe sobrecarga de método tradicional, mas podemos simular usando parâmetros padrão ou *args/**kwargs.

```python
class Calculadora:
    def somar(self, *args):
        return sum(args)
    
    def multiplicar(self, x, y=1, z=1):
        return x * y * z

# Usando diferentes números de argumentos
calc = Calculadora()
print(calc.somar(1, 2))         # 3
print(calc.somar(1, 2, 3, 4))   # 10
print(calc.multiplicar(2))       # 2
print(calc.multiplicar(2, 3))    # 6
print(calc.multiplicar(2, 3, 4)) # 24
```

## 3. Exemplo com Formas Geométricas

```python
class Forma:
    def area(self):
        pass
    
    def perimetro(self):
        pass
    
    def descricao(self):
        return f"Área: {self.area():.2f}, Perímetro: {self.perimetro():.2f}"

class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.14159
    
    def area(self):
        return self.pi * self.raio ** 2
    
    def perimetro(self):
        return 2 * self.pi * self.raio

class Triangulo(Forma):
    def __init__(self, base, altura, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado2 = lado2
        self.lado3 = lado3
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return self.base + self.lado2 + self.lado3

# Usando as formas
formas = [
    Retangulo(5, 3),
    Circulo(4),
    Triangulo(6, 4, 5, 5)
]

for forma in formas:
    print(f"{forma.__class__.__name__}: {forma.descricao()}")
```

## 4. Exemplo com Sistema de Pagamento

```python
class Pagamento:
    def processar_pagamento(self, valor):
        pass
    
    def emitir_recibo(self, valor):
        return f"Recibo de pagamento: R${valor:.2f}"

class PagamentoCartao(Pagamento):
    def __init__(self, numero_cartao):
        self.numero_cartao = numero_cartao
    
    def processar_pagamento(self, valor):
        return f"Pagamento de R${valor:.2f} processado com cartão {self.numero_cartao[-4:]}"

class PagamentoPix(Pagamento):
    def __init__(self, chave_pix):
        self.chave_pix = chave_pix
    
    def processar_pagamento(self, valor):
        return f"Pagamento de R${valor:.2f} processado via PIX para {self.chave_pix}"

class PagamentoBoleto(Pagamento):
    def processar_pagamento(self, valor):
        return f"Boleto de R${valor:.2f} gerado para pagamento"
    
    def emitir_recibo(self, valor):
        return f"Recibo de boleto: R${valor:.2f} (Válido após compensação)"

# Usando o sistema de pagamento
def realizar_pagamento(metodo_pagamento, valor):
    print(metodo_pagamento.processar_pagamento(valor))
    print(metodo_pagamento.emitir_recibo(valor))

# Testando diferentes métodos
cartao = PagamentoCartao("1234567890123456")
pix = PagamentoPix("email@exemplo.com")
boleto = PagamentoBoleto()

realizar_pagamento(cartao, 100.50)
realizar_pagamento(pix, 200.75)
realizar_pagamento(boleto, 150.25)
```

## 5. Duck Typing
Python também suporta "duck typing", onde o polimorfismo é baseado no comportamento dos objetos em vez de sua herança.

```python
class Pato:
    def falar(self):
        return "Quack!"
    
    def andar(self):
        return "Andando como um pato"

class Pessoa:
    def falar(self):
        return "Olá!"
    
    def andar(self):
        return "Andando como uma pessoa"

class Robo:
    def falar(self):
        return "Beep!"
    
    def andar(self):
        return "Rodando sobre rodas"

def fazer_objeto_agir(objeto):
    print(objeto.falar())
    print(objeto.andar())

# Todos os objetos podem ser usados da mesma forma
fazer_objeto_agir(Pato())
fazer_objeto_agir(Pessoa())
fazer_objeto_agir(Robo())
```

## Pontos Importantes:

1. **Flexibilidade**
   - Permite tratar objetos diferentes de maneira uniforme
   - Facilita a extensão do código

2. **Manutenção**
   - Torna o código mais organizado
   - Facilita mudanças e adições de funcionalidades

3. **Reutilização**
   - Promove reuso de código
   - Reduz duplicação

4. **Abstração**
   - Permite trabalhar com conceitos de alto nível
   - Esconde detalhes de implementação

5. **Duck Typing**
   - "Se anda como um pato e faz quack como um pato, então é um pato"
   - Foco no comportamento, não na herança
