O **PyInstaller** é um módulo Python que permite converter scripts `.py` em executáveis standalone (como `.exe` no Windows ou binários no Ubuntu/Linux), que funcionam mesmo sem o Python instalado na máquina.

---

## ✅ OBJETIVO

Criar um executável a partir de um script Python, usando o `pyinstaller`, tanto no **Windows 10** como no **Ubuntu Linux**.

---

## 1. 🔧 INSTALAR O PYINSTALLER

### ▶ No Windows 10 e Ubuntu:

Abra o terminal (CMD no Windows, Terminal no Ubuntu) e instale com:

```bash
pip install pyinstaller
```

Se quiser verificar se instalou corretamente:

```bash
pyinstaller --version
```

---

## 2. 📝 CRIAR UM SCRIPT PYTHON DE EXEMPLO

### Exemplo: `ola.py`

```python
# ola.py
def main():
    print("Olá, mundo! Este é um executável criado com PyInstaller.")

if __name__ == "__main__":
    main()
```

---

## 3. 🛠️ GERAR O EXECUTÁVEL

### ▶ Comando básico:

```bash
pyinstaller ola.py
```

O PyInstaller cria:

```
ola.spec               # ficheiro de configuração do build
build/                 # ficheiros temporários
dist/                  # o executável final está aqui
__pycache__/           # cache Python
```

### ▶ O executável final estará em:

* **Windows:** `dist\ola\ola.exe`
* **Ubuntu:** `dist/ola/ola` (binário)

---

## 4. ⚙️ OPÇÕES ÚTEIS DO PYINSTALLER

### 🔹 Criar apenas 1 ficheiro (`--onefile`)

```bash
pyinstaller --onefile ola.py
```

* Cria um único ficheiro `.exe` (ou binário) em `dist/`.

### 🔹 Ocultar o terminal (apenas no Windows GUI)

```bash
pyinstaller --onefile --noconsole ola.py
```

> Ideal para aplicações gráficas (ex: com `tkinter`, `PyQt`, etc.)

### 🔹 Incluir ícone (Windows)

```bash
pyinstaller --onefile --icon=icone.ico ola.py
```

> O ícone deve estar no mesmo diretório.

---

## 5. 🧪 TESTAR O EXECUTÁVEL

### ▶ Windows:

* Ir à pasta `dist\ola\`
* Executar `ola.exe` (duplo clique ou via terminal)

### ▶ Ubuntu:

* Ir à pasta `dist/ola/`
* Dar permissão de execução:

```bash
chmod +x ola
./ola
```

---

## 6. 🧹 LIMPAR ARQUIVOS TEMPORÁRIOS

Após compilar, pode apagar estas pastas:

```bash
rm -rf build __pycache__ ola.spec
```

---

## 7. 📦 EMPACOTAMENTO PARA DISTRIBUIÇÃO

* **Windows**: envie apenas o `ola.exe` (se usou `--onefile`)
* **Ubuntu**: envie o binário `ola` e verifique dependências com `ldd ola`

---

## 💡 DICA EXTRA (Módulos com dependências)

Se o script usar módulos como `requests`, `tkinter`, `pygame`, etc., o `pyinstaller` normalmente os inclui automaticamente. Se faltar algo, adicione com:

```bash
pyinstaller --onefile --hidden-import=nome_do_modulo ola.py
```

---

## ✅ RESUMO

| Passo | Comando                   | Descrição                  |
| ----- | ------------------------- | -------------------------- |
| 1     | `pip install pyinstaller` | Instalar                   |
| 2     | `pyinstaller ola.py`      | Criar executável           |
| 3     | `--onefile`               | Gerar um único ficheiro    |
| 4     | `--noconsole`             | Ocultar terminal (Windows) |
| 5     | `--icon=icone.ico`        | Adicionar ícone (Windows)  |

---
