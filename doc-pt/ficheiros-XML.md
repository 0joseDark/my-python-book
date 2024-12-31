Em Python, podemos usar o módulo `xml.etree.ElementTree` para manipular ficheiros XML. XML (eXtensible Markup Language) é um formato de dados que organiza informações em tags hierárquicas, permitindo que dados complexos sejam armazenados de maneira estruturada e legível. É muito útil para armazenar dados que precisam de estrutura, como configurações, dados de usuários, ou configurações de software.

### Estrutura de um Ficheiro XML

Antes de começar, vejamos um exemplo de um ficheiro XML:

```xml
<dados>
    <pessoa>
        <nome>Ana</nome>
        <idade>25</idade>
        <cidade>Lisboa</cidade>
    </pessoa>
    <pessoa>
        <nome>João</nome>
        <idade>30</idade>
        <cidade>Porto</cidade>
    </pessoa>
</dados>
```

Neste exemplo:
- O elemento raiz é `<dados>`, e dentro dele temos várias tags `<pessoa>`.
- Cada `<pessoa>` tem sub-elementos `<nome>`, `<idade>`, e `<cidade>` para armazenar as informações individuais.

### Lendo um Ficheiro XML

Para ler um ficheiro XML em Python e extrair informações, usamos `ElementTree`.

```python
import xml.etree.ElementTree as ET

# Carregar o ficheiro XML
tree = ET.parse("dados.xml")
root = tree.getroot()

# Percorrer os elementos do XML e imprimir os dados
for pessoa in root.findall("pessoa"):
    nome = pessoa.find("nome").text
    idade = pessoa.find("idade").text
    cidade = pessoa.find("cidade").text
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")
```

Neste exemplo:
1. Carregamos o XML usando `ET.parse()`.
2. Acessamos o elemento raiz com `getroot()`.
3. Utilizamos `findall("pessoa")` para encontrar todas as tags `<pessoa>`, e `find()` para acessar as subtags.

### Criando um Ficheiro XML

Para criar um novo ficheiro XML, usamos `ElementTree` para construir a estrutura e depois gravamos num ficheiro.

```python
import xml.etree.ElementTree as ET

# Criar o elemento raiz
root = ET.Element("dados")

# Adicionar uma nova pessoa
pessoa1 = ET.SubElement(root, "pessoa")
ET.SubElement(pessoa1, "nome").text = "Ana"
ET.SubElement(pessoa1, "idade").text = "25"
ET.SubElement(pessoa1, "cidade").text = "Lisboa"

# Adicionar outra pessoa
pessoa2 = ET.SubElement(root, "pessoa")
ET.SubElement(pessoa2, "nome").text = "João"
ET.SubElement(pessoa2, "idade").text = "30"
ET.SubElement(pessoa2, "cidade").text = "Porto"

# Guardar a estrutura XML num ficheiro
tree = ET.ElementTree(root)
tree.write("novo_dados.xml", encoding="utf-8", xml_declaration=True)

print("Ficheiro XML criado com sucesso.")
```

Neste exemplo:
1. Criamos a tag raiz `<dados>`.
2. Adicionamos duas tags `<pessoa>`, cada uma com subtags `<nome>`, `<idade>`, e `<cidade>`.
3. Usamos `ElementTree.write()` para gravar o XML num ficheiro.

### Alterando um Ficheiro XML

Para modificar dados num ficheiro XML existente, carregamos o ficheiro, fazemos as alterações e depois salvamos novamente.

```python
import xml.etree.ElementTree as ET

# Carregar o ficheiro XML
tree = ET.parse("dados.xml")
root = tree.getroot()

# Modificar a idade da primeira pessoa
pessoa = root.find("pessoa")
if pessoa is not None:
    idade = pessoa.find("idade")
    if idade is not None:
        idade.text = "26"  # Alterando a idade para 26

# Guardar o XML modificado
tree.write("dados_modificado.xml", encoding="utf-8", xml_declaration=True)

print("Ficheiro XML atualizado com sucesso.")
```

Neste exemplo:
1. Carregamos o ficheiro `dados.xml`.
2. Usamos `find()` para acessar a primeira tag `<pessoa>` e depois modificamos o valor da tag `<idade>`.
3. Gravamos as alterações num novo ficheiro `dados_modificado.xml`.

### Excluindo Elementos de um Ficheiro XML

Podemos também remover elementos de um ficheiro XML usando `remove()`.

```python
import xml.etree.ElementTree as ET

# Carregar o ficheiro XML
tree = ET.parse("dados.xml")
root = tree.getroot()

# Encontrar e remover a primeira pessoa
pessoa = root.find("pessoa")
if pessoa is not None:
    root.remove(pessoa)

# Guardar o XML com o elemento removido
tree.write("dados_removido.xml", encoding="utf-8", xml_declaration=True)

print("Primeira pessoa removida do ficheiro XML.")
```

Neste exemplo:
1. Carregamos o XML.
2. Usamos `find("pessoa")` para localizar a primeira pessoa e `remove()` para removê-la do XML.
3. Salvamos a nova versão com o elemento excluído.

### Resumo das Funções Principais
- `ET.parse("file.xml")`: carrega um ficheiro XML.
- `getroot()`: obtém o elemento raiz.
- `find(tag)`: localiza o primeiro elemento com a tag especificada.
- `findall(tag)`: localiza todos os elementos com a tag especificada.
- `SubElement(parent, "tag")`: cria uma subtag de um elemento.
- `write("file.xml")`: grava as alterações no ficheiro XML.

Esses exemplos fornecem uma base para criar, ler, modificar e excluir dados em ficheiros XML usando Python, possibilitando o armazenamento e manipulação de dados complexos de forma estruturada.
