Vamos fazer exemplos práticos de como compilar **vários ficheiros `.py`** com o **PyInstaller**.
Existem dois cenários principais:

---

# 🔹 1. Compilar **cada script separadamente**

Se queres que cada `.py` vire o seu próprio `.exe`:

```bash
pyinstaller --onefile script1.py
pyinstaller --onefile script2.py
pyinstaller --onefile script3.py
```

Resultado no `dist/`:

```
script1.exe
script2.exe
script3.exe
```

---

# 🔹 2. Usar ficheiro `.spec` para vários executáveis

Se quiseres gerar **vários `.exe` de uma só vez**, crias um ficheiro `.spec`.

Exemplo: `multi.spec`

```python
# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

# Primeiro executável
exe1 = EXE(
    ['script1.py'],
    name='Script1',
    console=True,      # mostra terminal
    icon='icone1.ico'
)

# Segundo executável
exe2 = EXE(
    ['script2.py'],
    name='Script2',
    console=False,     # sem terminal (GUI)
    icon='icone2.ico'
)

# Terceiro executável
exe3 = EXE(
    ['script3.py'],
    name='Script3',
    console=True
)

coll = COLLECT([exe1, exe2, exe3])
```

Compilar:

```bash
pyinstaller multi.spec
```

Resultado no `dist/`:

```
Script1.exe
Script2.exe
Script3.exe
```

---

# 🔹 3. Scripts que dependem uns dos outros

Se tens **múltiplos ficheiros `.py` mas só um é o principal** (os outros são módulos importados), então só precisas compilar o principal:

Exemplo:

```
meu_app/
 ├─ main.py       (script principal)
 ├─ utils.py      (funções auxiliares)
 ├─ gui.py        (interface gráfica)
```

Compilas apenas o `main.py`:

```bash
pyinstaller --onefile main.py
```

O PyInstaller vai detetar automaticamente `utils.py` e `gui.py` como dependências e incluí-los no executável.

---

# 🔹 4. Compilar com ficheiros extras

Se cada script precisa de imagens, XML ou sons, podes usar `--add-data` em conjunto:

```bash
pyinstaller --onefile --add-data "config.xml;." --icon=icone1.ico script1.py
pyinstaller --onefile --add-data "dados.db;." --icon=icone2.ico script2.py
```

---

# 🔹 5. Compilar vários de uma vez com PowerShell / Bash

No **Windows (PowerShell)**:

```powershell
foreach ($f in Get-ChildItem *.py) {
    pyinstaller --onefile $f.Name
}
```

No **Linux/Mac (Bash)**:

```bash
for f in *.py; do
    pyinstaller --onefile "$f"
done
```

Assim compilas todos os `.py` da pasta automaticamente.

---
