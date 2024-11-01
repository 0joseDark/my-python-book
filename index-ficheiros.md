- [voltar atrás](https://github.com/0joseDark/my-python-book/blob/main/index.md)
# Manipulação de Ficheiros em Python

A manipulação de ficheiros em Python envolve operações como criar, ler, escrever e fechar ficheiros. Vamos explorar as funções básicas usadas para manipulação de ficheiros e depois explicar com exemplos:

### 1. **Abrir e Fechar Ficheiros**

- **`open()`**: Usada para abrir um ficheiro. O modo de abertura pode ser:
  - `'r'`: leitura (read)
  - `'w'`: escrita (write) – apaga o conteúdo existente
  - `'a'`: anexar (append) – adiciona ao final
  - `'b'`: modo binário (binary), como `'rb'` para leitura binária
  - `'x'`: criar um ficheiro (gera erro se o ficheiro já existir)
  
- **`close()`**: Fecha o ficheiro para liberar recursos.

#### Exemplo de Abertura e Fecho de Ficheiros
```python
# Abrir o ficheiro para leitura
ficheiro = open('exemplo.txt', 'r')
# Operações com o ficheiro
print(ficheiro.read())
# Fechar o ficheiro
ficheiro.close()
```

### 2. **Ler Ficheiros**
- **`read()`**: Lê o conteúdo inteiro.
- **`readline()`**: Lê uma linha de cada vez.
- **`readlines()`**: Lê todas as linhas e retorna uma lista.

#### Exemplo de Leitura
```python
ficheiro = open('exemplo.txt', 'r')
conteudo = ficheiro.read()
print(conteudo)
ficheiro.close()
```

### 3. **Escrever em Ficheiros**
- **`write()`**: Escreve uma string no ficheiro.
- **`writelines()`**: Escreve uma lista de strings.

#### Exemplo de Escrita
```python
ficheiro = open('exemplo.txt', 'w')
ficheiro.write("Este é um exemplo de escrita.\n")
ficheiro.writelines(["Linha 1\n", "Linha 2\n"])
ficheiro.close()
```

### 4. **Gerir Erros com `with`**
Ao abrir ficheiros com `with`, não é necessário usar `close()`. O Python fecha automaticamente o ficheiro quando sai do bloco.

#### Exemplo de Uso com `with`
```python
with open('exemplo.txt', 'r') as ficheiro:
    conteudo = ficheiro.read()
    print(conteudo)
# O ficheiro é automaticamente fechado aqui
```

### 5. **Anexar Conteúdo a Ficheiros**
Usamos o modo `'a'` para adicionar ao final do ficheiro, sem apagar o conteúdo anterior.

#### Exemplo de Anexar
```python
with open('exemplo.txt', 'a') as ficheiro:
    ficheiro.write("Adicionando mais texto ao ficheiro.\n")
```

### 6. **Trabalhar com Ficheiros Binários**
Ficheiros binários, como imagens ou ficheiros de vídeo, podem ser manipulados com os modos `'rb'` e `'wb'`.

#### Exemplo de Manipulação de Ficheiro Binário
```python
# Leitura binária
with open('imagem.png', 'rb') as ficheiro:
    dados = ficheiro.read()
    print(dados[:20])  # Exibir os primeiros 20 bytes

# Escrita binária
with open('nova_imagem.png', 'wb') as novo_ficheiro:
    novo_ficheiro.write(dados)
```

### 7. **Mover o Cursor de Leitura/Escrita**
- **`seek()`**: Move o cursor para uma posição específica no ficheiro.
- **`tell()`**: Retorna a posição atual do cursor.

#### Exemplo de `seek()` e `tell()`
```python
with open('exemplo.txt', 'r') as ficheiro:
    ficheiro.seek(5)  # Mover para a 6ª posição
    print(ficheiro.read())  # Ler a partir daqui
    print(ficheiro.tell())  # Mostrar a posição atual
```

### Conclusão
Manipular ficheiros em Python é um processo simples e direto com funções como `open()`, `read()`, `write()`, e `close()`. A utilização de contextos (`with`) torna o código mais limpo, enquanto funções como `seek()` permitem maior controle sobre a leitura e escrita.

---

## 8.1 Manipulação de Ficheiros CSV

Ficheiros CSV (Comma Separated Values) são amplamente usados para armazenar dados tabulares. O Python oferece o módulo `csv` para ler e escrever estes ficheiros de forma eficiente.

### 1. Ler Ficheiros CSV
Para ler um ficheiro CSV, utilizamos a função `csv.reader()`, que converte cada linha do ficheiro numa lista.

#### Exemplo de Leitura de CSV
```python
import csv

with open('dados.csv', 'r') as ficheiro_csv:
    leitor_csv = csv.reader(ficheiro_csv)
    for linha in leitor_csv:
        print(linha)
```

### 2. Escrever Ficheiros CSV
Para escrever num ficheiro CSV, usamos `csv.writer()`.

#### Exemplo de Escrita de CSV
```python
import csv

dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['Ana', '28', 'Lisboa'],
    ['Carlos', '35', 'Porto']
]

with open('dados.csv', 'w', newline='') as ficheiro_csv:
    escritor_csv = csv.writer(ficheiro_csv)
    escritor_csv.writerows(dados)
```

### 3. Ler e Escrever com Dicionários
O `csv.DictReader()` e `csv.DictWriter()` permitem trabalhar com CSV usando dicionários, onde as chaves são os cabeçalhos das colunas.

#### Exemplo de Leitura de CSV com Dicionário
```python
import csv

with open('dados.csv', 'r') as ficheiro_csv:
    leitor_csv = csv.DictReader(ficheiro_csv)
    for linha in leitor_csv:
        print(linha)
```

#### Exemplo de Escrita de CSV com Dicionário
```python
import csv

cabecalhos = ['Nome', 'Idade', 'Cidade']
dados = [
    {'Nome': 'Ana', 'Idade': '28', 'Cidade': 'Lisboa'},
    {'Nome': 'Carlos', 'Idade': '35', 'Cidade': 'Porto'}
]

with open('dados.csv', 'w', newline='') as ficheiro_csv:
    escritor_csv = csv.DictWriter(ficheiro_csv, fieldnames=cabecalhos)
    escritor_csv.writeheader()
    escritor_csv.writerows(dados)
```

---

## 8.3 Manipulação de Ficheiros JSON

Ficheiros JSON (JavaScript Object Notation) são usados para armazenar e transmitir dados estruturados. Em Python, o módulo `json` facilita a conversão de dicionários Python para JSON e vice-versa.

### 1. Ler Ficheiros JSON
Para ler ficheiros JSON, usamos `json.load()`.

#### Exemplo de Leitura de JSON
```python
import json

with open('dados.json', 'r') as ficheiro_json:
    dados = json.load(ficheiro_json)
    print(dados)
```

### 2. Escrever Ficheiros JSON
Para gravar dados num ficheiro JSON, usamos `json.dump()`.

#### Exemplo de Escrita de JSON
```python
import json

dados = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "Lisboa"
}

with open('dados.json', 'w') as ficheiro_json:
    json.dump(dados, ficheiro_json, indent=4)
```

### 3. Converter JSON em String e Vice-versa
- `json.dumps()`: Converte um dicionário em uma string JSON.
- `json.loads()`: Converte uma string JSON em dicionário.

#### Exemplo
```python
import json

# Dicionário para JSON
dados = {"nome": "Ana", "idade": 28}
json_string = json.dumps(dados)
print(json_string)

# JSON para Dicionário
dados_reconvertidos = json.loads(json_string)
print(dados_reconvertidos)
```

---

## 8.4 Manipulação de Ficheiros XML

O XML (eXtensible Markup Language) é utilizado para representar dados estruturados hierarquicamente. O Python oferece o módulo `xml.etree.ElementTree` para trabalhar com ficheiros XML.

### 1. Ler Ficheiros XML
Usamos `ElementTree` para analisar e navegar pelos elementos de um ficheiro XML.

#### Exemplo de Leitura de XML
```python
import xml.etree.ElementTree as ET

# Parse do ficheiro XML
arvore = ET.parse('dados.xml')
raiz = arvore.getroot()

# Aceder aos elementos
for filho in raiz:
    print(filho.tag, filho.attrib, filho.text)
```

#### Estrutura Exemplo de `dados.xml`
```xml
<usuarios>
    <usuario nome="Ana">
        <idade>28</idade>
        <cidade>Lisboa</cidade>
    </usuario>
    <usuario nome="Carlos">
        <idade>35</idade>
        <cidade>Porto</cidade>
    </usuario>
</usuarios>
```

### 2. Criar e Escrever Ficheiros XML
Podemos criar elementos

 e gravar no ficheiro XML.

#### Exemplo de Escrita de XML
```python
import xml.etree.ElementTree as ET

# Criação da estrutura XML
raiz = ET.Element("usuarios")
usuario = ET.SubElement(raiz, "usuario", nome="Ana")
ET.SubElement(usuario, "idade").text = "28"
ET.SubElement(usuario, "cidade").text = "Lisboa"

# Gravar o ficheiro
arvore = ET.ElementTree(raiz)
arvore.write("dados.xml", encoding="utf-8", xml_declaration=True)
```

---

## Conclusão
A manipulação de ficheiros em Python é uma competência fundamental para trabalhar com diversos formatos de dados. O Python oferece uma série de módulos que facilitam essas operações, adaptando-se a diferentes tipos de ficheiros e usos. Experimente utilizar essas operações para aprofundar o seu domínio sobre manipulação de dados em Python.

---
