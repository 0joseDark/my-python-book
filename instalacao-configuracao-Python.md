Vou explicar detalhadamente cada um desses tópicos sobre a instalação e configuração do Python.

### 1.2.1 Instalar Python no Windows, macOS e Linux

**Windows:**
1. Acesse python.org/downloads
2. Baixe a versão mais recente do Python
3. Execute o instalador e marque a opção "Add Python to PATH"
4. Clique em "Install Now"
5. Para verificar a instalação, abra o CMD e digite:
```bash
python --version
```

**macOS:**
1. O Python geralmente já vem instalado
2. Para uma versão mais recente, você pode:
   - Usar o Homebrew:
```bash
brew install python
```
   - Ou baixar do python.org/downloads

**Linux:**
- Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3
```
- Fedora:
```bash
sudo dnf install python3
```

### 1.2.2 Utilizar o pip para gerir pacotes

O pip é o gerenciador de pacotes do Python. Exemplos de uso:

1. Verificar versão do pip:
```bash
pip --version
```

2. Instalar um pacote:
```bash
pip install nome_do_pacote
```

3. Instalar versão específica:
```bash
pip install nome_do_pacote==2.0.0
```

4. Listar pacotes instalados:
```bash
pip list
```

5. Desinstalar um pacote:
```bash
pip uninstall nome_do_pacote
```

6. Criar arquivo de requisitos:
```bash
pip freeze > requirements.txt
```

7. Instalar pacotes de um arquivo requirements.txt:
```bash
pip install -r requirements.txt
```

### 1.3 Executar o Primeiro Programa em Python

Vamos criar e executar um programa simples:

1. Crie um arquivo chamado `primeiro.py` com um editor de texto
2. Adicione este código:

```python
# Primeiro programa em Python
print("Olá, Mundo!")
nome = input("Digite seu nome: ")
print(f"Bem-vindo ao Python, {nome}!")
```

3. Para executar, há várias formas:

**Via terminal:**
```bash
python primeiro.py
```

**Via IDE (como PyCharm ou VS Code):**
- Abra o arquivo
- Clique no botão de executar ou pressione F5

Aqui está um exemplo mais elaborado que demonstra alguns conceitos básicos:

```python
# Exemplo de programa mais completo
def calcular_media(notas):
    return sum(notas) / len(notas)

# Lista para armazenar as notas
notas = []

# Solicitar 3 notas
for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

# Calcular e mostrar a média
media = calcular_media(notas)
print(f"\nA média das notas é: {media:.1f}")

# Verificar aprovação
if media >= 7.0:
    print("Situação: Aprovado!")
else:
    print("Situação: Reprovado!")
```

Algumas dicas importantes:
1. Use um ambiente virtual (venv) para projetos diferentes
2. Mantenha o Python e o pip atualizados
3. Sempre verifique a documentação oficial para comandos específicos
4. Começe com programas simples e vá aumentando a complexidade gradualmente
