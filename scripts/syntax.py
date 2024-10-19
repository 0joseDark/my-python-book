# Este programa exemplifica a sintaxe básica de Python com explicações detalhadas.

# 1. VARIÁVEIS E TIPOS DE DADOS

# Em Python, as variáveis não precisam de ser declaradas com um tipo específico.
# Atribuímos valores diretamente às variáveis.
nome = "João"  # Variável do tipo string (texto)
idade = 25  # Variável do tipo inteiro (número inteiro)
altura = 1.75  # Variável do tipo float (número decimal)
casado = False  # Variável do tipo booleano (True ou False)

# Exibimos as variáveis no ecrã usando a função print().
# Usamos a função type() para mostrar o tipo de cada variável.
print("Nome:", nome, "- Tipo:", type(nome))
print("Idade:", idade, "- Tipo:", type(idade))
print("Altura:", altura, "- Tipo:", type(altura))
print("Casado:", casado, "- Tipo:", type(casado))

# 2. LISTAS

# Uma lista em Python é uma coleção de itens que podem ser de diferentes tipos.
# As listas podem ser modificadas (são mutáveis).
frutas = ["maçã", "banana", "laranja"]  # Criamos uma lista de frutas
print("\nLista de frutas:", frutas)  # \n é uma nova linha

# Podemos adicionar novos itens à lista com o método append().
frutas.append("uva")
print("Lista atualizada de frutas:", frutas)

# 3. ESTRUTURAS DE CONTROLO - IF, ELIF, ELSE

# Podemos usar o condicional if para verificar condições.
if idade >= 18:
    print("\nÉs maior de idade.")
else:
    print("\nÉs menor de idade.")

# Podemos usar elif (else if) para verificar várias condições.
if idade < 18:
    print("Menor de idade.")
elif idade >= 18 and idade < 65:
    print("Adulto.")
else:
    print("Idoso.")

# 4. LOOPS (CICLOS)

# Ciclo for: útil para iterar sobre uma sequência (como uma lista ou um intervalo de números).
print("\nFrutas na lista:")
for fruta in frutas:
    print(fruta)  # Exibimos cada fruta na lista

# Ciclo while: repete o bloco de código enquanto a condição for verdadeira.
contador = 0
print("\nContagem usando while:")
while contador < 3:
    print("Contador:", contador)
    contador += 1  # Aumentamos o contador em 1 a cada iteração

# 5. FUNÇÕES

# Definimos funções em Python usando a palavra-chave def.
def cumprimentar(nome):
    """Esta função imprime uma mensagem de saudação."""  # Comentário tipo docstring
    print("\nOlá,", nome)

# Chamamos a função e passamos um argumento.
cumprimentar("Ana")

# 6. TRABALHAR COM FICHEIROS

# Vamos abrir um ficheiro em modo de escrita e gravar texto nele.
with open("exemplo.txt", "w") as ficheiro:
    ficheiro.write("Este é um exemplo de gravação num ficheiro em Python.\n")

# Agora, vamos ler o conteúdo do ficheiro.
with open("exemplo.txt", "r") as ficheiro:
    conteudo = ficheiro.read()
    print("\nConteúdo do ficheiro:")
    print(conteudo)

# 7. EXCEÇÕES (ERROS)

# Podemos usar try e except para tratar erros no código.
try:
    divisao = 10 / 0  # Isto vai causar um erro de divisão por zero
except ZeroDivisionError:
    print("\nErro: Não é possível dividir por zero!")

# 8. CLASSES E OBJETOS (Programação Orientada a Objetos)

# Definimos uma classe chamada Pessoa.
class Pessoa:
    def __init__(self, nome, idade):
        """Construtor da classe Pessoa."""
        self.nome = nome  # Atributo nome
        self.idade = idade  # Atributo idade

    def mostrar_informacao(self):
        """Método para exibir informações sobre a pessoa."""
        print("\nNome:", self.nome)
        print("Idade:", self.idade)

# Criamos um objeto da classe Pessoa.
pessoa1 = Pessoa("Carlos", 30)

# Chamamos o método para mostrar as informações da pessoa.
pessoa1.mostrar_informacao()
