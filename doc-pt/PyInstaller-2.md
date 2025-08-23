O **PyInstaller** é uma ferramenta em Python que permite transformar os teus scripts `.py` em executáveis independentes (`.exe` no Windows, binários no Linux/Mac).
Ele consegue **compilar vários scripts**, mas há algumas coisas importantes a entender:

---

## 1. Comando básico

Para compilar **um único script**:

```bash
pyinstaller script.py
```

Isso gera:

* uma pasta `build/` (ficheiros temporários da compilação)
* uma pasta `dist/` (onde fica o executável final)
* um ficheiro `script.spec` (configuração da compilação)

---

## 2. Modos de saída

* **Um executável + dependências em pasta**:

  ```bash
  pyinstaller script.py
  ```

  → Gera `dist/script/` com `script.exe` + DLLs + ficheiros necessários.

* **Um único ficheiro executável (standalone)**:

  ```bash
  pyinstaller --onefile script.py
  ```

  → Gera `dist/script.exe` (contém tudo dentro de um só `.exe`).

* **Com ícone**:

  ```bash
  pyinstaller --onefile --icon=icone.ico script.py
  ```

---

## 3. Compilar **vários scripts**

Existem **duas formas**:

### 🔹 A) Gerar um executável por script

Basta compilar cada um separadamente:

```bash
pyinstaller --onefile script1.py
pyinstaller --onefile script2.py
pyinstaller --onefile script3.py
```

Assim, no `dist/`, terás `script1.exe`, `script2.exe`, `script3.exe`.

---

### 🔹 B) Usar ficheiro `.spec` para vários scripts

Se quiseres **vários executáveis numa única compilação**, editas o ficheiro `.spec`.

Exemplo: `multi.spec`

```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Executável 1
exe1 = EXE(
    ['script1.py'],
    name='Script1',
    console=True
)

# Executável 2
exe2 = EXE(
    ['script2.py'],
    name='Script2',
    console=True
)

# Executável 3
exe3 = EXE(
    ['script3.py'],
    name='Script3',
    console=True
)

coll = COLLECT([exe1, exe2, exe3])
```

Depois compilas todos de uma vez:

```bash
pyinstaller multi.spec
```

E no `dist/` vão aparecer `Script1.exe`, `Script2.exe`, `Script3.exe`.

---

## 4. Opções úteis do PyInstaller

* `--onefile` → cria único executável.
* `--noconsole` → remove a janela de terminal (para apps GUI).
* `--icon=icone.ico` → adiciona ícone.
* `--add-data "ficheiro;."` → inclui ficheiros extra (ex: imagens, DLLs, XML, etc).
* `--clean` → remove cache antes de compilar.
* `--name=NomeApp` → define o nome do executável.

Exemplo completo:

```bash
pyinstaller --onefile --noconsole --icon=app.ico --add-data "config.xml;." --name=MeuApp script.py
```

---

## 5. Workflow recomendado para vários scripts

1. Faz primeiro `pyinstaller script.py` para gerar o `.spec`.
2. Junta todos os scripts nesse `.spec`.
3. Compila com:

   ```bash
   pyinstaller multi.spec
   ```

---
