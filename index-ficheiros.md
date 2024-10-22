A "Manipulação de Ficheiros" em Python envolve operações como criar, ler, escrever, e fechar ficheiros. Vamos explorar as funções básicas usadas para manipulação de ficheiros e depois explicar com exemplos:

### 1. **Abrir e Fechar Ficheiros**

- **`open()`**: Usada para abrir um ficheiro. O modo de abertura pode ser:
  - `'r'`: leitura (read)
  - `'w'`: escrita (write) – apaga o conteúdo existente
  - `'a'`: anexar (append) – adiciona ao final
  - `'b'`: modo binário (binary), como `'rb'` para leitura binária
  - `'x'`: criar um ficheiro (gera erro se o ficheiro já existir)
  
- **`close()`**: Fecha o ficheiro para liberar recursos.

### Exemplo de Abertura e Fecho de Ficheiros
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

### Exemplo de Leitura
```python
ficheiro = open('exemplo.txt', 'r')
# Ler todo o conteúdo do ficheiro
conteudo = ficheiro.read()
print(conteudo)
ficheiro.close()
```

### 3. **Escrever em Ficheiros**
- **`write()`**: Escreve uma string no ficheiro.
- **`writelines()`**: Escreve uma lista de strings.

### Exemplo de Escrita
```python
ficheiro = open('exemplo.txt', 'w')
# Escrever no ficheiro
ficheiro.write("Este é um exemplo de escrita.\n")
ficheiro.writelines(["Linha 1\n", "Linha 2\n"])
ficheiro.close()
```

### 4. **Gerir Erros com `with`**
Ao abrir ficheiros com `with`, não é necessário usar `close()`. O Python fecha automaticamente o ficheiro quando sai do bloco.

### Exemplo de Uso com `with`
```python
with open('exemplo.txt', 'r') as ficheiro:
    conteudo = ficheiro.read()
    print(conteudo)
# O ficheiro é automaticamente fechado aqui
```

### 5. **Anexar Conteúdo a Ficheiros**
Usamos o modo `'a'` para adicionar ao final do ficheiro, sem apagar o conteúdo anterior.

### Exemplo de Anexar
```python
with open('exemplo.txt', 'a') as ficheiro:
    ficheiro.write("Adicionando mais texto ao ficheiro.\n")
```

### 6. **Trabalhar com Ficheiros Binários**
Ficheiros binários, como imagens ou ficheiros de vídeo, podem ser manipulados com os modos `'rb'` e `'wb'`.

### Exemplo de Manipulação de Ficheiro Binário
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

### Exemplo de `seek()` e `tell()`
```python
with open('exemplo.txt', 'r') as ficheiro:
    ficheiro.seek(5)  # Mover para a 6ª posição
    print(ficheiro.read())  # Ler a partir daqui
    print(ficheiro.tell())  # Mostrar a posição atual
```

### Conclusão
Manipular ficheiros em Python é um processo simples e direto com funções como `open()`, `read()`, `write()`, e `close()`. A utilização de contextos (`with`) torna o código mais limpo, enquanto funções como `seek()` permitem maior controle sobre a leitura e escrita.

Esses exemplos fornecem uma base sólida para operações básicas e avançadas de manipulação de ficheiros.
8.1 Manipulação de Ficheiros CSV

Ficheiros CSV (Comma Separated Values) são amplamente usados para armazenar dados tabulares. O Python oferece o módulo csv para ler e escrever estes ficheiros de forma eficiente.
1. Ler Ficheiros CSV

Para ler um ficheiro CSV, utilizamos a função csv.reader(), que converte cada linha do ficheiro numa lista.
Exemplo de Leitura de CSV

python

import csv

with open('dados.csv', 'r') as ficheiro_csv:
    leitor_csv = csv.reader(ficheiro_csv)
    for linha in leitor_csv:
        print(linha)

2. Escrever Ficheiros CSV

Para escrever num ficheiro CSV, usamos csv.writer().
Exemplo de Escrita de CSV

python

import csv

dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['Ana', '28', 'Lisboa'],
    ['Carlos', '35', 'Porto']
]

with open('dados.csv', 'w', newline='') as ficheiro_csv:
    escritor_csv = csv.writer(ficheiro_csv)
    escritor_csv.writerows(dados)

3. Ler e Escrever com Dicionários

O csv.DictReader() e csv.DictWriter() permitem trabalhar com CSV usando dicionários, onde as chaves são os cabeçalhos das colunas.
Exemplo de Leitura de CSV com Dicionário

python

import csv

with open('dados.csv', 'r') as ficheiro_csv:
    leitor_csv = csv.DictReader(ficheiro_csv)
    for linha in leitor_csv:
        print(linha)

Exemplo de Escrita de CSV com Dicionário

python

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

8.3 Manipulação de Ficheiros JSON

Ficheiros JSON (JavaScript Object Notation) são usados para armazenar e transmitir dados estruturados. Em Python, o módulo json facilita a conversão de dicionários Python para JSON e vice-versa.
1. Ler Ficheiros JSON

Para ler ficheiros JSON, usamos json.load().
Exemplo de Leitura de JSON

python

import json

with open('dados.json', 'r') as ficheiro_json:
    dados = json.load(ficheiro_json)
    print(dados)

2. Escrever Ficheiros JSON

Para gravar dados num ficheiro JSON, usamos json.dump().
Exemplo de Escrita de JSON

python

import json

dados = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "Lisboa"
}

with open('dados.json', 'w') as ficheiro_json:
    json.dump(dados, ficheiro_json, indent=4)

3. Converter JSON em String e Vice-versa

    json.dumps(): Converte um dicionário em uma string JSON.
    json.loads(): Converte uma string JSON em dicionário.

Exemplo

python

import json

# Dicionário para JSON
dados = {"nome": "Ana", "idade": 28}
json_string = json.dumps(dados)
print(json_string)

# JSON para Dicionário
dados_reconvertidos = json.loads(json_string)
print(dados_reconvertidos)

8.4 Manipulação de Ficheiros XML

O XML (eXtensible Markup Language) é utilizado para representar dados estruturados hierarquicamente. O Python oferece o módulo xml.etree.ElementTree para trabalhar com ficheiros XML.
1. Ler Ficheiros XML

Usamos ElementTree para analisar e navegar pelos elementos de um ficheiro XML.
Exemplo de Leitura de XML

python

import xml.etree.ElementTree as ET

# Parse do ficheiro XML
arvore = ET.parse('dados.xml')
raiz = arvore.getroot()

# Aceder aos elementos
for filho in raiz:
    print(filho.tag, filho.attrib, filho.text)

Estrutura Exemplo de dados.xml

xml

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

2. Criar e Escrever Ficheiros XML

Podemos criar elementos e árvores XML com ElementTree e depois guardá-los.
Exemplo de Escrita de XML

python

import xml.etree.ElementTree as ET

# Criar a estrutura XML
raiz = ET.Element("usuarios")

usuario1 = ET.SubElement(raiz, "usuario", nome="Ana")
ET.SubElement(usuario1, "idade").text = "28"
ET.SubElement(usuario1, "cidade").text = "Lisboa"

usuario2 = ET.SubElement(raiz, "usuario", nome="Carlos")
ET.SubElement(usuario2, "idade").text = "35"
ET.SubElement(usuario2, "cidade").text = "Porto"

# Criar a árvore e gravar o ficheiro XML
arvore = ET.ElementTree(raiz)
arvore.write("dados.xml", encoding="utf-8", xml_declaration=True)

3. Modificar e Atualizar Ficheiros XML

Podemos também modificar o conteúdo de ficheiros XML, como alterar valores de texto ou atributos.
Exemplo de Modificação de XML

python

import xml.etree.ElementTree as ET

# Parse do ficheiro XML
arvore = ET.parse('dados.xml')
raiz = arvore.getroot()

# Alterar o valor de um elemento
for usuario in raiz.findall('usuario'):
    if usuario.get('nome') == 'Ana':
        usuario.find('cidade').text = 'Coimbra'

# Gravar as alterações no ficheiro
arvore.write('dados_atualizados.xml', encoding="utf-8", xml_declaration=True)

Conclusão

A manipulação de ficheiros CSV, JSON e XML em Python é simples e poderosa com as bibliotecas nativas. Cada formato tem suas particularidades e o uso adequado de cada um depende do tipo de dados e das necessidades do projeto.

    CSV é ideal para dados tabulares simples.
    JSON é mais flexível, adequado para dados estruturados em dicionários.
    XML é ideal para dados hierárquicos, sendo muito usado em troca de dados entre sistemas.

