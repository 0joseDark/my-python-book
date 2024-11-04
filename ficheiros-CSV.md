O Python facilita a manipulação de ficheiros CSV (Comma-Separated Values), que são amplamente usados para armazenar dados tabulares em texto. Para trabalhar com ficheiros CSV, o Python oferece o módulo `csv`, que permite leitura, escrita e manipulação de dados de forma fácil e eficiente.

### 1. Estrutura Básica de um Ficheiro CSV

Um ficheiro CSV é composto por linhas onde cada coluna é separada por uma vírgula (ou outro delimitador como ponto e vírgula). A primeira linha geralmente contém os cabeçalhos (nomes das colunas). Exemplo:

```
nome,idade,email
Ana,28,ana@example.com
Carlos,35,carlos@example.com
```

### 2. Manipulação de Ficheiros CSV no Python

#### Importando o Módulo CSV

Primeiro, importa-se o módulo `csv`:

```python
import csv
```

#### Abrindo e Fechando um Ficheiro CSV

Para abrir um ficheiro CSV, usamos a função `open()` com o nome do ficheiro e o modo de abertura (`r` para leitura, `w` para escrita, `a` para acrescentar dados). Por exemplo:

```python
with open("exemplo.csv", mode="r", newline="") as file:
    # Manipulações do ficheiro aqui
```

Usar `with` garante que o ficheiro será fechado automaticamente após a manipulação.

### 3. Ler um Ficheiro CSV

Para ler um ficheiro CSV, usamos `csv.reader` (para uma leitura simples) ou `csv.DictReader` (para leitura baseada em dicionários).

#### Exemplo com `csv.reader`

O `csv.reader` lê cada linha do ficheiro como uma lista.

```python
with open("exemplo.csv", mode="r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

#### Exemplo com `csv.DictReader`

O `csv.DictReader` converte cada linha num dicionário onde as chaves são os cabeçalhos do ficheiro.

```python
with open("exemplo.csv", mode="r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # Cada linha é um dicionário
```

### 4. Escrever em um Ficheiro CSV

Para escrever em um ficheiro CSV, usamos `csv.writer` ou `csv.DictWriter`.

#### Exemplo com `csv.writer`

O `csv.writer` permite escrever listas diretamente no ficheiro.

```python
with open("exemplo.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["nome", "idade", "email"])  # Escrever cabeçalhos
    writer.writerow(["Ana", 28, "ana@example.com"])  # Escrever uma linha
    writer.writerow(["Carlos", 35, "carlos@example.com"])  # Outra linha
```

#### Exemplo com `csv.DictWriter`

O `csv.DictWriter` permite escrever dicionários onde as chaves correspondem aos cabeçalhos do ficheiro.

```python
with open("exemplo.csv", mode="w", newline="") as file:
    fieldnames = ["nome", "idade", "email"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Escrever cabeçalhos
    writer.writerow({"nome": "Ana", "idade": 28, "email": "ana@example.com"})  # Escrever uma linha
    writer.writerow({"nome": "Carlos", "idade": 35, "email": "carlos@example.com"})  # Outra linha
```

### 5. Acrescentar Dados a um Ficheiro CSV

Para acrescentar dados, usamos o modo de abertura `a` (append).

```python
with open("exemplo.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Pedro", 22, "pedro@example.com"])  # Adicionar uma linha
```

### 6. Ler e Processar Dados CSV em Python

Abaixo está um exemplo que lê um ficheiro CSV e faz algumas operações nos dados.

**Exemplo: Calcular a Média de Idade**

Suponha que queremos calcular a média de idade dos clientes.

```python
with open("exemplo.csv", mode="r", newline="") as file:
    reader = csv.DictReader(file)
    idades = [int(row["idade"]) for row in reader]  # Extrair idades como uma lista de inteiros

media_idade = sum(idades) / len(idades) if idades else 0
print(f"A média de idade é: {media_idade}")
```

### 7. Manipular Ficheiros CSV com Diferentes Delimitadores

O delimitador padrão em CSV é a vírgula, mas pode ser alterado. Por exemplo, para ficheiros com ponto e vírgula (`;`) como delimitador:

```python
with open("exemplo.csv", mode="r", newline="") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        print(row)
```

Para escrita com delimitador personalizado:

```python
with open("exemplo.csv", mode="w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["nome", "idade", "email"])
    writer.writerow(["Ana", 28, "ana@example.com"])
```

### 8. Manipular Ficheiros CSV com Pandas

Outra forma popular de manipular ficheiros CSV em Python é com a biblioteca `pandas`, que oferece funcionalidades mais avançadas.

Primeiro, instale o `pandas`:

```bash
pip install pandas
```

**Exemplo de Leitura com `pandas`**

```python
import pandas as pd

# Ler o CSV em um DataFrame
df = pd.read_csv("exemplo.csv")
print(df)
```

**Exemplo de Escrita com `pandas`**

```python
# Criar um DataFrame e escrever para CSV
data = {
    "nome": ["Ana", "Carlos", "Pedro"],
    "idade": [28, 35, 22],
    "email": ["ana@example.com", "carlos@example.com", "pedro@example.com"]
}

df = pd.DataFrame(data)
df.to_csv("exemplo.csv", index=False)
```

### Conclusão

Essas são as principais operações com ficheiros CSV em Python:

- **Ler e processar dados** com `csv.reader` e `csv.DictReader`.
- **Escrever e acrescentar dados** com `csv.writer` e `csv.DictWriter`.
- Manipular ficheiros CSV com `pandas` para funcionalidades mais avançadas.

Manipular ficheiros CSV com Python é essencial em muitas áreas, desde análise de dados até automação de tarefas administrativas.
