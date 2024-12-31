No Python, os módulos `os` e `subprocess` permitem interagir com o sistema operacional para executar comandos e automatizar tarefas. Aqui está um resumo de como cada módulo pode ser utilizado, seguido de exemplos práticos.

### 1. Módulo `os`
O módulo `os` é útil para operações básicas de sistema, como manipulação de arquivos e diretórios, obtenção de variáveis de ambiente, execução de comandos simples, etc.

Principais funções úteis:
- `os.system(cmd)`: Executa um comando no terminal do sistema.
- `os.listdir(path)`: Lista arquivos e diretórios em um caminho específico.
- `os.mkdir(path)`: Cria um novo diretório.
- `os.remove(path)`: Remove um arquivo.
- `os.getenv(var_name)`: Obtém o valor de uma variável de ambiente.

#### Exemplo com `os`

Vamos fazer alguns exemplos básicos com o módulo `os`:

```python
import os

# 1. Executar um comando no terminal (exemplo: listar arquivos e diretórios)
os.system("dir")  # No Windows
# os.system("ls")  # No Linux/Mac

# 2. Listar arquivos e pastas no diretório atual
arquivos = os.listdir(".")
print("Arquivos e pastas no diretório atual:", arquivos)

# 3. Criar um novo diretório
os.mkdir("nova_pasta")
print("Diretório 'nova_pasta' criado.")

# 4. Remover um arquivo
# Primeiro criamos um arquivo temporário para remover
with open("arquivo_temporario.txt", "w") as f:
    f.write("Este é um arquivo temporário.")
os.remove("arquivo_temporario.txt")
print("Arquivo 'arquivo_temporario.txt' removido.")

# 5. Obter uma variável de ambiente
caminho = os.getenv("PATH")
print("Valor da variável PATH:", caminho)
```

### 2. Módulo `subprocess`
O módulo `subprocess` permite maior controle ao executar comandos de sistema. Ele é mais poderoso e flexível do que `os.system()`, pois permite capturar a saída dos comandos e manipular erros.

Principais funções úteis:
- `subprocess.run(cmd, ...)`: Executa um comando, onde `cmd` é uma lista de strings com o comando e os argumentos.
- `subprocess.Popen(...)`: Executa o comando em um processo separado, permitindo mais controle.
- `stdout=subprocess.PIPE`: Permite capturar a saída do comando.
- `stderr=subprocess.PIPE`: Permite capturar erros do comando.

#### Exemplo com `subprocess.run`

```python
import subprocess

# Executa um comando e captura a saída
resultado = subprocess.run(["dir"], capture_output=True, text=True, shell=True)  # No Windows
# resultado = subprocess.run(["ls"], capture_output=True, text=True)  # No Linux/Mac

print("Saída do comando:", resultado.stdout)
print("Erros do comando (se houver):", resultado.stderr)
```

#### Exemplo com `subprocess.Popen`

Vamos usar `Popen` para abrir um programa de forma assíncrona, ou seja, sem bloquear o Python enquanto o programa está aberto.

```python
import subprocess

# Abre o Bloco de Notas no Windows
processo = subprocess.Popen(["notepad.exe"])
print("Bloco de notas aberto. PID:", processo.pid)

# Espera o Bloco de Notas ser fechado antes de continuar
processo.wait()
print("Bloco de notas fechado.")
```

### Resumo das Diferenças
- Use `os` para operações simples de sistema e manipulação de arquivos.
- Use `subprocess` para executar comandos com controle sobre entrada, saída, e erros, ou quando precisar de execução assíncrona.

Esses exemplos são úteis para automatizar processos no sistema operacional, como manipulação de arquivos, execução de scripts e interação com outros programas.
