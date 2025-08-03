## ✅ 1. Instalar o PyInstaller

### **Comando**:

```bash
pip install pyinstaller
```

### **Explicação**:

* Usa-se este comando para instalar o PyInstaller.
* Funciona em Windows, Ubuntu, e Mac.
* O `pip` precisa de estar corretamente instalado e atualizado.

### **Exemplo (Windows ou Ubuntu Terminal)**:

```bash
pip install pyinstaller
```

---

## ✅ 2. Criar executável básico com PyInstaller

### **Comando**:

```bash
pyinstaller ola.py
```

### **Explicação**:

* Cria uma pasta `dist/` com o executável do ficheiro `ola.py`.
* Também cria pastas `build/` e um ficheiro `ola.spec`.

### **Exemplo**:

```bash
pyinstaller ola.py
```

---

## ✅ 3. Gerar um único ficheiro com `--onefile`

### **Comando**:

```bash
pyinstaller --onefile ola.py
```

### **Explicação**:

* Cria apenas **um executável único**, em vez de várias dependências.
* Útil para distribuição simples.

### **Exemplo**:

```bash
pyinstaller --onefile ola.py
```

---

## ✅ 4. Ocultar terminal com `--noconsole` (apenas no Windows)

### **Comando**:

```bash
pyinstaller --onefile --noconsole ola.py
```

### **Explicação**:

* **Oculta a janela de terminal/console** ao abrir o `.exe`.
* Ideal para **aplicações gráficas com `tkinter`, `PyQt`, etc.**

⚠️ Em aplicações **com interface de linha de comandos**, **não usar** este argumento.

### **Exemplo**:

```bash
pyinstaller --onefile --noconsole ola.py
```

---

## ✅ 5. Adicionar ícone ao executável com `--icon` (Windows)

### **Comando**:

```bash
pyinstaller --onefile --noconsole --icon=icone.ico ola.py
```

### **Explicação**:

* Adiciona o ícone `.ico` ao executável gerado.
* Só funciona com ficheiros `.ico` no Windows.
* O ícone deve estar na mesma pasta do `ola.py` ou indicar o caminho completo.

### **Exemplo**:

```bash
pyinstaller --onefile --noconsole --icon=icone.ico ola.py
```

---

## 🔍 Resultado final (Windows)

Depois de executar o comando completo:

```bash
pyinstaller --onefile --noconsole --icon=icone.ico ola.py
```

Será criada a pasta `dist/`, e dentro dela estará:

```
dist/
├── ola.exe ← este é o executável final
```

---

## 📦 Extras úteis

| Comando                     | Explicação                                    |
| --------------------------- | --------------------------------------------- |
| `--clean`                   | Limpa ficheiros temporários antes de compilar |
| `--name=meu_programa`       | Define o nome do `.exe` gerado                |
| `--add-data "imagem.png;."` | Adiciona ficheiros necessários (ver abaixo)   |

> No Windows: `--add-data "ficheiro.txt;."`
> No Linux/macOS: `--add-data "ficheiro.txt:."`

---
