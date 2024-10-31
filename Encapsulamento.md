## Encapsulamento em Programação Orientada a Objetos (POO)

**Encapsulamento** é um dos quatro pilares da Programação Orientada a Objetos (POO) e refere-se ao conceito de **esconder os detalhes internos de uma classe** e expor apenas o que é necessário. Isso permite que o estado interno de um objeto (ou seja, seus dados) seja protegido de modificações externas inesperadas, controlando como esses dados são acessados e modificados.

### Principais Vantagens do Encapsulamento
1. **Segurança**: Permite proteger os dados internos de acesso ou modificações indesejadas.
2. **Modularidade**: Cada classe controla seus próprios dados, tornando o código mais organizado.
3. **Facilidade de manutenção**: Com os detalhes internos ocultos, é possível alterar a implementação interna sem impactar outras partes do código.

### Como o Encapsulamento é Implementado em Python?
Em Python, usamos convenções para definir os níveis de acesso:
- **Público** (`public`): Atributos e métodos sem sublinhados são públicos, podendo ser acessados de fora da classe.
- **Protegido** (`protected`): Um sublinhado (`_`) antes de um atributo ou método indica que ele é protegido, sendo uma convenção de que não deve ser acessado diretamente.
- **Privado** (`private`): Dois sublinhados (`__`) antes de um atributo ou método tornam-no privado, e ele só pode ser acessado de dentro da classe.

### Exemplo de Encapsulamento em Python

Vamos criar uma classe `ContaBancaria` que possui métodos para **depositar** e **retirar** dinheiro, usando encapsulamento para proteger o saldo da conta.

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular      # Atributo público
        self.__saldo = saldo_inicial  # Atributo privado
    
    # Método público para visualizar o saldo
    def ver_saldo(self):
        return self.__saldo
    
    # Método público para depositar dinheiro
    def depositar(self, quantia):
        if quantia > 0:
            self.__saldo += quantia
            print(f"Depósito de {quantia} realizado com sucesso!")
        else:
            print("Quantia inválida para depósito.")
    
    # Método público para retirar dinheiro
    def retirar(self, quantia):
        if 0 < quantia <= self.__saldo:
            self.__saldo -= quantia
            print(f"Retirada de {quantia} realizada com sucesso!")
        else:
            print("Quantia inválida ou saldo insuficiente.")

# Criando uma conta bancária
conta = ContaBancaria("João", 1000)

# Acessando e modificando o saldo através dos métodos
print("Saldo inicial:", conta.ver_saldo())  # Saída: Saldo inicial: 1000

# Realizando um depósito
conta.depositar(500)  # Saída: Depósito de 500 realizado com sucesso!
print("Saldo após depósito:", conta.ver_saldo())  # Saída: Saldo após depósito: 1500

# Realizando uma retirada
conta.retirar(200)  # Saída: Retirada de 200 realizada com sucesso!
print("Saldo após retirada:", conta.ver_saldo())  # Saída: Saldo após retirada: 1300

# Tentando acessar o atributo privado diretamente (vai gerar erro)
# print(conta.__saldo)  # AtributoError: 'ContaBancaria' object has no attribute '__saldo'
```

### Explicação do Exemplo:
1. **Atributo privado** `__saldo`: O atributo `__saldo` é privado e só pode ser acessado ou modificado dentro da classe. Fora da classe, ele não é acessível diretamente.
2. **Métodos públicos** `ver_saldo`, `depositar`, `retirar`: Esses métodos fornecem acesso controlado ao saldo, permitindo ver o saldo e fazer transações de forma segura.
3. **Controle de Acesso**: Por meio desses métodos, garantimos que apenas transações válidas sejam realizadas (por exemplo, não permitindo depósitos negativos ou retiradas acima do saldo).

### Conclusão
O encapsulamento protege os dados de uma classe ao expor apenas o que é necessário, facilitando o controle de acesso e a segurança dos dados. Em Python, podemos usar convenções para definir atributos e métodos públicos, protegidos e privados, aplicando o encapsulamento de maneira eficiente.
