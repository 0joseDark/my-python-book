A manipulação de ficheiros em Python permite ler, escrever, e modificar conteúdos de diferentes tipos de ficheiros, incluindo os ficheiros JSON, que são comumente usados para armazenar e transferir dados estruturados. Vamos ver um pouco sobre manipulação de ficheiros em geral, focando em ler e escrever dados, e depois vamos explorar o formato JSON especificamente.

### Manipulação de Ficheiros em Python

Em Python, a função `open()` é usada para abrir um ficheiro. Esta função pode abrir o ficheiro em diferentes modos:
- `"r"` para leitura (read)
- `"w"` para escrita (write)
- `"a"` para acrescentar (append)
- `"r+"` para leitura e escrita

Aqui está um exemplo básico para abrir, ler, e escrever num ficheiro de texto:

```python
# Abrir um ficheiro em modo de escrita e adicionar conteúdo
with open("exemplo.txt", "w") as file:
    file.write("Esta é uma linha de exemplo.")

# Abrir o ficheiro em modo de leitura e exibir o conteúdo
with open("exemplo.txt", "r") as file:
    conteudo = file.read()
    print(conteudo)
```

Neste exemplo:
1. Criamos o ficheiro `exemplo.txt` e escrevemos uma linha nele.
2. Depois, abrimos o ficheiro novamente, desta vez em modo de leitura, para exibir o conteúdo.

### Manipulação de Ficheiros JSON

O formato JSON (JavaScript Object Notation) é um padrão leve para troca de dados, bastante utilizado para estruturar dados em pares de chave-valor, como objetos e listas. Python tem o módulo `json` que permite manipular dados JSON facilmente.

#### Exemplo de Escrita em JSON

Aqui, vamos criar um dicionário em Python, convertê-lo para JSON e gravá-lo num ficheiro:

```python
import json

# Dados para salvar no ficheiro JSON
dados = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "Lisboa",
    "hobbies": ["leitura", "viajar", "caminhadas"]
}

# Escrever os dados num ficheiro JSON
with open("dados.json", "w") as file:
    json.dump(dados, file, indent=4)

print("Ficheiro JSON criado com sucesso.")
```

Neste exemplo:
1. Criamos um dicionário chamado `dados`.
2. Usamos `json.dump()` para gravar esse dicionário em `dados.json`, adicionando uma indentação de 4 espaços para deixar o JSON formatado.

#### Exemplo de Leitura de JSON

Para ler um ficheiro JSON e acessar os dados, utilizamos `json.load()`:

```python
import json

# Ler dados do ficheiro JSON
with open("dados.json", "r") as file:
    dados_lidos = json.load(file)

print(dados_lidos)
```

Este exemplo:
1. Abre o ficheiro `dados.json` em modo de leitura.
2. Carrega os dados JSON no dicionário `dados_lidos` e imprime-os.

#### Manipular Dados JSON Lidos

Com os dados lidos, podemos manipulá-los, adicionando ou modificando informações, e depois salvá-los de novo.

```python
# Modificar os dados lidos
dados_lidos["idade"] = 26
dados_lidos["cidade"] = "Porto"
dados_lidos["hobbies"].append("fotografia")

# Escrever as mudanças no ficheiro JSON novamente
with open("dados.json", "w") as file:
    json.dump(dados_lidos, file, indent=4)

print("Ficheiro JSON atualizado com sucesso.")
```

Neste exemplo:
1. Alteramos a idade, a cidade e adicionamos um novo hobby.
2. Gravamos as alterações no mesmo ficheiro JSON.

### Manipulação de Listas em JSON

Se quisermos armazenar uma lista de itens, podemos gravá-la no formato JSON assim:

```python
import json

# Lista de dados para salvar em JSON
lista_dados = [
    {"nome": "Carlos", "idade": 28},
    {"nome": "Maria", "idade": 32},
    {"nome": "Pedro", "idade": 19}
]

# Escrever a lista no ficheiro JSON
with open("lista_dados.json", "w") as file:
    json.dump(lista_dados, file, indent=4)

print("Lista de dados gravada com sucesso em JSON.")
```

Para ler e manipular esta lista, faríamos assim:

```python
# Ler a lista de dados do ficheiro JSON
with open("lista_dados.json", "r") as file:
    lista_lida = json.load(file)

# Exibir cada elemento da lista
for pessoa in lista_lida:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")
```

### Resumo dos Comandos JSON
- `json.dump(data, file)`: grava dados JSON num ficheiro.
- `json.load(file)`: lê dados JSON de um ficheiro.
- `json.dumps(data)`: converte um dicionário para uma string JSON.
- `json.loads(string)`: converte uma string JSON para um dicionário.

Estes exemplos dão uma boa base para criar e manipular ficheiros JSON, com potencial para armazenar e organizar dados estruturados em Python.
