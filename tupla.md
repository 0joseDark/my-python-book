Em Python, uma tupla é uma estrutura de dados semelhante a uma lista, mas que é **imutável**, o que significa que, uma vez criada, seus elementos não podem ser alterados, adicionados ou removidos. As tuplas são úteis para armazenar dados que não devem ser modificados ao longo do programa, como coordenadas, dados de configuração, e outras informações que precisam de proteção contra alterações acidentais.

### Características das Tuplas:
1. **Imutáveis**: Os elementos não podem ser modificados, adicionados ou removidos.
2. **Indexadas**: Podemos acessar os elementos pela sua posição.
3. **Permitem tipos variados**: Uma tupla pode conter tipos de dados diferentes.

### Exemplo de criação e uso de uma tupla:

```python
# Criando uma tupla com alguns elementos
coordenadas = (10.5, 20.3)

# Acessando elementos por índice
print("Primeira coordenada:", coordenadas[0])  # Saída: 10.5
print("Segunda coordenada:", coordenadas[1])   # Saída: 20.3

# Tentando modificar um elemento (isso causará um erro)
# coordenadas[0] = 15.0  # Isso gera um erro pois a tupla é imutável

# Criando uma tupla com tipos de dados mistos
dados_pessoais = ("João", 30, "Lisboa")

# Desempacotamento de tuplas
nome, idade, cidade = dados_pessoais  # Atribui cada elemento da tupla a uma variável
print("Nome:", nome)
print("Idade:", idade)
print("Cidade:", cidade)

# Verificando o tamanho da tupla
print("Número de elementos na tupla 'dados_pessoais':", len(dados_pessoais))

# Concatenando duas tuplas
dados_extra = ("engenheiro",)
dados_completos = dados_pessoais + dados_extra  # Cria uma nova tupla concatenando as duas
print("Dados completos:", dados_completos)

# Verificando a presença de um elemento na tupla
print("A cidade é Lisboa?", "Lisboa" in dados_pessoais)  # Saída: True
```

### Explicação dos principais conceitos:
1. **Criação de tuplas**: Podemos definir uma tupla usando parênteses `()`.
2. **Acesso por índice**: Podemos acessar elementos específicos da tupla usando índices, como nas listas.
3. **Imutabilidade**: Tentativas de alterar os elementos resultam em erro.
4. **Desempacotamento**: As tuplas permitem atribuir seus elementos a várias variáveis ao mesmo tempo.
5. **Operações com tuplas**:
   - **Tamanho** (`len()`): Verifica a quantidade de elementos.
   - **Concatenar** (`+`): Cria uma nova tupla ao unir duas.
   - **Verificar presença** (`in`): Confirma se um elemento existe na tupla.
