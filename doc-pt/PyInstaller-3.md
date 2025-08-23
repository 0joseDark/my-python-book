O `--add-data` do **PyInstaller** serve para incluir **ficheiros externos** (imagens, XML, bases de dados, sons, etc.) dentro do executável.
Assim, quando o `.exe` for executado, esses ficheiros vão estar disponíveis no mesmo diretório de execução.

⚠️ **Atenção**: a sintaxe é **diferente no Windows e no Linux/Mac**

* **Windows** → usa `;` como separador
* **Linux/Mac** → usa `:` como separador

---

## 1. Exemplo simples (Windows)

Tens um script que usa um `config.xml`.

```bash
pyinstaller --onefile --add-data "config.xml;." script.py
```

* `"config.xml;."` → copia o `config.xml` para a mesma pasta que o `.exe`
* `.` → significa "diretório atual" dentro do `dist/`

Depois, ao correr o `.exe`, o ficheiro `config.xml` estará na mesma pasta.

---

## 2. Colocar ficheiros numa subpasta

Se quiseres que os ficheiros fiquem dentro de uma pasta específica:

```bash
pyinstaller --onefile --add-data "config.xml;config" script.py
```

* Vai criar `dist/script/config/config.xml`

---

## 3. Vários ficheiros

Basta repetir o parâmetro:

```bash
pyinstaller --onefile --add-data "config.xml;." --add-data "imagem.png;." script.py
```

No `dist/script/` vais ter:

* `script.exe`
* `config.xml`
* `imagem.png`

---

## 4. Incluir uma pasta inteira

Se tens uma pasta `assets/` com imagens e sons:

```bash
pyinstaller --onefile --add-data "assets;assets" script.py
```

Vai copiar a pasta inteira `assets/` para `dist/script/assets/`

---

## 5. Exemplo prático com ícone, ficheiros e GUI

```bash
pyinstaller --onefile --noconsole --icon=app.ico ^
  --add-data "config.xml;." ^
  --add-data "imagens;imagens" ^
  --add-data "sons;sons" ^
  --name=MeuPrograma app.py
```

Resultado final (`dist/MeuPrograma/`):

```
MeuPrograma.exe
config.xml
imagens/...
sons/...
```

---

## 6. Como aceder aos ficheiros no código

⚠️ Quando corres o `.py` diretamente, os ficheiros estão na pasta normal.
⚠️ Mas quando corres o `.exe`, o PyInstaller usa uma pasta temporária (`sys._MEIPASS`).

Por isso, no Python deves fazer assim:

```python
import sys, os

def recurso(caminho):
    """Encontra ficheiro tanto em .py como no .exe"""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, caminho)
    return os.path.join(os.path.abspath("."), caminho)

# exemplo: carregar config.xml
ficheiro_config = recurso("config.xml")
print("Caminho do config:", ficheiro_config)
```

Assim funciona **tanto em modo normal como compilado**.

---
