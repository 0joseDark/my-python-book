- [voltar atrás](https://github.com/0joseDark/my-python-book/blob/main/README.md)
- Em Python, uma lista é uma estrutura de dados que armazena uma coleção de itens de maneira ordenada e mutável. É uma das estruturas mais usadas em Python, pois permite armazenar qualquer tipo de dado (números, strings, outras listas, etc.) e modificar seus elementos facilmente.

### Características das Listas:
1. **Mutáveis**: Podemos modificar os elementos, adicionar ou remover itens.
2. **Ordenadas**: Os elementos mantêm a ordem em que foram adicionados.
3. **Tipos variados**: Podem conter dados de diferentes tipos.

### Exemplo de criação e uso de uma lista:

```python
# Criando uma lista com alguns elementos
frutas = ["maçã", "banana", "laranja"]

# Acessando elementos por índice
print("Primeira fruta:", frutas[0])  # Saída: maçã
print("Segunda fruta:", frutas[1])   # Saída: banana

# Adicionando elementos
frutas.append("uva")  # Adiciona "uva" ao final da lista
print("Lista após adicionar uva:", frutas)

# Inserindo um elemento em uma posição específica
frutas.insert(1, "manga")  # Insere "manga" na posição 1
print("Lista após inserir manga:", frutas)

# Modificando um elemento
frutas[2] = "kiwi"  # Substitui "laranja" por "kiwi"
print("Lista após substituir laranja por kiwi:", frutas)

# Removendo um elemento específico
frutas.remove("maçã")  # Remove "maçã" da lista
print("Lista após remover maçã:", frutas)

# Removendo o último elemento
ultima_fruta = frutas.pop()  # Remove e retorna o último elemento
print("Última fruta removida:", ultima_fruta)
print("Lista após remover o último elemento:", frutas)

# Verificando o tamanho da lista
print("Número de frutas na lista:", len(frutas))

# Iterando sobre a lista
print("Frutas na lista:")
for fruta in frutas:
    print("-", fruta)

# Verificando a presença de um elemento
print("A lista contém 'banana'?", "banana" in frutas)  # Saída: True ou False
```

### Explicação dos principais conceitos:
1. **Criação de lista**: Definimos uma lista usando colchetes `[]`.
2. **Acesso por índice**: Usamos índices para acessar elementos individuais.
3. **Adição de elementos**: Métodos como `append()` e `insert()` permitem adicionar novos itens.
4. **Modificação e remoção**: Podemos modificar itens diretamente usando índices e remover itens com `remove()` ou `pop()`.
5. **Tamanho**: A função `len()` retorna o número de itens na lista.
6. **Iteração**: Podemos percorrer a lista com um loop `for`.
7. **Verificação de presença**: `in` confirma se um elemento existe na lista.
