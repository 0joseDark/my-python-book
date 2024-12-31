Executar o primeiro programa em Python é um processo simples e direto. Basta escrever um script Python (um arquivo com a extensão `.py`) e executá-lo usando o interpretador Python. Vamos seguir algumas etapas:

### 1. Verificar a Instalação do Python

Primeiro, é importante confirmar que o Python está instalado no sistema:

- Abra o terminal (ou o Prompt de Comando no Windows) e digite:
  ```bash
  python --version
  ```
- Se o Python estiver instalado, você verá a versão instalada, como `Python 3.x.x`.

### 2. Escrever o Primeiro Programa

Vamos criar um programa simples que imprime uma mensagem na tela.

1. Abra um editor de texto (como o VS Code, Notepad++, ou mesmo o Bloco de Notas).
2. Escreva o código Python básico para exibir a mensagem “Olá, Mundo!”:
   ```python
   print("Olá, Mundo!")
   ```
3. Salve o arquivo com o nome `primeiro_programa.py` em um local fácil de encontrar, como a área de trabalho ou uma pasta de projetos.

### 3. Executar o Programa

Agora, vamos executar o script.

#### Usando o Terminal ou Prompt de Comando

1. Abra o terminal (ou o Prompt de Comando).
2. Navegue até o diretório onde o arquivo `primeiro_programa.py` está salvo. Se estiver na área de trabalho, você pode navegar até lá com o comando:
   - No Windows:
     ```bash
     cd Desktop
     ```
   - No Linux/macOS:
     ```bash
     cd ~/Desktop
     ```
3. Execute o programa digitando:
   ```bash
   python primeiro_programa.py
   ```
4. Você verá a saída no terminal:
   ```
   Olá, Mundo!
   ```

#### Executando a partir de um IDE (como o VS Code ou PyCharm)

1. Abra o `primeiro_programa.py` no VS Code ou PyCharm.
2. Execute o programa. Normalmente, há um botão “Run” (Executar) ou você pode pressionar `F5` (no VS Code) para executar.
3. A saída aparecerá no terminal embutido do editor, mostrando:
   ```
   Olá, Mundo!
   ```

### Explicação do Código

O código `print("Olá, Mundo!")` usa a função `print()` para exibir uma mensagem na tela. Neste caso, a string `"Olá, Mundo!"` é passada como argumento para a função `print()`, que então a imprime no terminal.

### Outros Exemplos de Programas Simples

1. **Exemplo de cálculo simples**
   ```python
   numero1 = 5
   numero2 = 10
   soma = numero1 + numero2
   print("A soma é:", soma)
   ```

   Este código soma dois números e imprime o resultado. A saída será:
   ```
   A soma é: 15
   ```

2. **Receber entrada do usuário**
   ```python
   nome = input("Qual é o seu nome? ")
   print("Olá,", nome, "!")
   ```

   Este código solicita o nome do usuário e o exibe na tela. Por exemplo, se o usuário digitar "Maria", a saída será:
   ```
   Olá, Maria!
   ```

Esses exemplos mostram a simplicidade de criar e executar programas em Python, desde o "Olá, Mundo!" até interações básicas com o usuário.
