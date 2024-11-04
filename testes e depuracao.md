### 10.1 Introdução aos Testes Unitários

Os testes unitários são uma técnica de validação de software onde cada parte do código é testada isoladamente para garantir que funcione corretamente. O objetivo é verificar a funcionalidade de componentes individuais, como funções ou métodos, e detectar problemas logo no início do desenvolvimento.

#### Exemplo básico:

Vamos supor que temos uma função para somar dois números:

```python
def soma(a, b):
    return a + b
```

Para testá-la, podemos criar testes unitários para verificar se a função retorna o valor esperado:

```python
import unittest

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-2, -3), -5)

    def test_soma_zero(self):
        self.assertEqual(soma(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
```

Neste exemplo, estamos verificando se a função `soma` lida corretamente com números positivos, negativos e zero.

---

### 10.2 Testes com `unittest`

O módulo `unittest` é uma estrutura de testes embutida no Python, que permite criar, organizar e executar testes de maneira sistemática.

#### Exemplo de teste com `unittest`:

Para um código mais complexo, vamos supor que temos uma classe `Calculadora`:

```python
class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b
```

Podemos criar uma classe de teste para `Calculadora`:

```python
import unittest

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_soma(self):
        self.assertEqual(self.calc.soma(2, 3), 5)

    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(5, 3), 2)

    def test_soma_negativos(self):
        self.assertEqual(self.calc.soma(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
```

O método `setUp` é executado antes de cada teste e é útil para configurar o ambiente. No final, `unittest.main()` executa todos os testes definidos.

---

### 10.3 Depuração com `pdb`

O `pdb` (Python Debugger) é uma ferramenta para depuração, que permite pausar a execução do programa, inspecionar variáveis e executar comandos para descobrir onde o código está falhando.

#### Exemplo de uso básico do `pdb`:

Vamos depurar a função `soma` com um ponto de interrupção:

```python
import pdb

def soma(a, b):
    pdb.set_trace()  # Pausa a execução aqui
    return a + b

resultado = soma(2, 3)
print("Resultado:", resultado)
```

Quando executamos este código, a execução pausa no `set_trace()`, e podemos interagir no terminal para ver o valor das variáveis (`a`, `b`) e verificar como o código está sendo executado.

Alguns comandos úteis do `pdb`:
- `n` (next): Executa a próxima linha.
- `c` (continue): Continua a execução até o próximo ponto de parada.
- `p <variável>`: Imprime o valor de uma variável.

---

### 10.4 Logging

O módulo `logging` permite registrar mensagens em diferentes níveis de gravidade (info, warning, error) para monitorar o comportamento da aplicação. Ao invés de usar `print` para depuração, o `logging` organiza as mensagens e facilita a análise de problemas em produção.

#### Exemplo básico de uso do `logging`:

```python
import logging

logging.basicConfig(level=logging.INFO)

def soma(a, b):
    logging.info(f"Somando {a} + {b}")
    return a + b

resultado = soma(2, 3)
logging.info(f"Resultado: {resultado}")
```

#### Níveis de logging:
- `DEBUG`: Informação detalhada, usada para diagnóstico.
- `INFO`: Confirmação de que tudo está funcionando.
- `WARNING`: Indicação de que algo inesperado aconteceu.
- `ERROR`: Um problema mais grave que impediu a execução de uma função.
- `CRITICAL`: Um erro grave, indicando que o programa pode não continuar.

---

Esses conceitos ajudam a identificar problemas de maneira organizada e a garantir que cada componente funcione corretamente antes de ser integrado.
