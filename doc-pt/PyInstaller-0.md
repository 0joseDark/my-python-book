## 🧰 O que é o **PyInstaller**?

O **PyInstaller** é uma ferramenta que transforma um script Python (`.py`) numa aplicação executável (`.exe` no Windows ou binário no Linux), **sem precisar do Python instalado na máquina de destino**.

---

## ✅ Vantagens do PyInstaller

* Cria ficheiros **executáveis standalone** (sem dependências externas).
* Funciona em **Windows, Linux e macOS**.
* Suporta **scripts com interfaces gráficas** (PyQt5, Tkinter, Kivy...).
* Compacta os ficheiros com **UPX** (opcional).
* Gera executáveis de **linha de comandos** ou **GUI**.

---

## 📦 Instalar PyInstaller

### No **Windows 10** ou **Ubuntu**:

```bash
pip install pyinstaller
```

> 💡 Recomendado usar um ambiente virtual (`venv`) para não afetar o sistema.

---

## 🛠️ Exemplo completo: criar um `.exe` ou binário

### Suponha o ficheiro `ola.py`:

```python
# ola.py
print("Olá! Este é o meu programa Python convertido em EXE!")
```

### 1. No terminal/cmd, ir à pasta do script:

```bash
cd caminho/para/o/ficheiro
```

### 2. Criar o executável:

```bash
pyinstaller --onefile ola.py
```

> **Explicação das opções**:

* `--onefile`: junta tudo num único `.exe` ou binário.
* `--noconsole`: para aplicações com GUI (oculta a consola).
* `--icon=icone.ico`: opcional, define ícone do executável.

---

### 3. Após a execução:

O PyInstaller cria 3 pastas/ficheiros:

```
/build/         ← ficheiros temporários da compilação  
/dist/          ← onde está o executável final  
ola.spec        ← ficheiro de configuração (pode editar)
```

#### 📁 Final:

* O executável está em: `dist/ola.exe` (Windows) ou `dist/ola` (Linux)

---

## 🪟 Exemplo com interface gráfica (Tkinter):

```python
# janela.py
import tkinter as tk

root = tk.Tk()
root.title("Exemplo com Tkinter")
tk.Label(root, text="Olá, mundo com GUI!").pack(padx=20, pady=20)
root.mainloop()
```

### Gerar executável sem consola:

```bash
pyinstaller --onefile --noconsole janela.py
```

---

## ⚙️ Customizar o ficheiro `.spec`

O `.spec` é gerado automaticamente, mas pode editar para:

* Adicionar ficheiros extra (imagens, vídeos, DLLs…)
* Incluir subpastas ou alterar nome do executável
* Compactar mais com UPX

---

## 🧪 Testar no Windows/Linux

* Em Windows: duplo clique no `.exe` na pasta `dist`.
* Em Ubuntu: dar permissão:

  ```bash
  chmod +x dist/ola
  ./dist/ola
  ```

---

## 🧯 Dicas úteis

* Evite caminhos com espaços.
* Se usar bibliotecas externas (PyQt5, pandas, numpy...), elas são incluídas.
* Se der erro de ficheiro não encontrado, adicione com `--add-data`.

---

## 📌 Exemplo com ficheiro de dados (imagem)

```python
# mostra_imagem.py
from tkinter import *
from PIL import Image, ImageTk

janela = Tk()
img = Image.open("foto.jpg")
img_tk = ImageTk.PhotoImage(img)
Label(janela, image=img_tk).pack()
janela.mainloop()
```

### Comando:

```bash
pyinstaller --onefile --noconsole --add-data "foto.jpg;." mostra_imagem.py
```

> Em **Windows**, separador é `;`, em **Linux** é `:`:

```bash
--add-data "foto.jpg:."
```

---

## 🧼 Limpar ficheiros temporários

Depois de gerar o executável, pode apagar:

```bash
rmdir /S /Q build
del *.spec
```

---

## 💡 Resumo rápido

| Comando                   | Descrição                        |
| ------------------------- | -------------------------------- |
| `--onefile`               | Gera 1 único ficheiro            |
| `--noconsole`             | Oculta a consola (GUI)           |
| `--icon=icone.ico`        | Define ícone                     |
| `--add-data "ficheiro;."` | Adiciona ficheiro (imagem, etc.) |

---
