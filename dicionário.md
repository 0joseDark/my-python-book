- [voltar atrás](https://github.com/0joseDark/my-python-book/blob/main/index.md)
- Em Python, um dicionário é uma estrutura de dados que armazena pares de chave-valor. Ele é útil quando queremos associar informações e acessá-las por uma chave única, que funciona como uma "etiqueta" para o valor correspondente. As chaves devem ser únicas e imutáveis (como strings, números ou tuplas), enquanto os valores podem ser de qualquer tipo e repetidos.

Aqui está um exemplo de uso de dicionário, com explicações em cada passo:

```python
# Criando um dicionário vazio
dicionario_vazio = {}

# Criando um dicionário com pares de chave-valor
pessoa = {
    "nome": "João",      # 'nome' é a chave e "João" é o valor
    "idade": 30,         # 'idade' é a chave e 30 é o valor
    "cidade": "Lisboa"   # 'cidade' é a chave e "Lisboa" é o valor
}

# Acessando o valor de uma chave específica
print("Nome:", pessoa["nome"])  # Saída: Nome: João

# Adicionando um novo par de chave-valor
pessoa["profissão"] = "Engenheiro"  # Agora o dicionário inclui a profissão
print("Dicionário atualizado:", pessoa)

# Alterando o valor de uma chave existente
pessoa["cidade"] = "Porto"  # Atualizamos a cidade de "Lisboa" para "Porto"
print("Cidade alterada:", pessoa)

# Removendo um par chave-valor
del pessoa["idade"]  # Remove a chave "idade" e seu valor do dicionário
print("Após remoção da idade:", pessoa)

# Iterando sobre as chaves do dicionário
for chave in pessoa:
    print(f"{chave}: {pessoa[chave]}")  # Exibe cada chave e seu valor

# Usando o método get() para acessar valores com segurança
idade = pessoa.get("idade", "Idade não especificada")  # Retorna "Idade não especificada" se a chave não existe
print("Idade:", idade)

# Dicionário final
print("Dicionário final:", pessoa)
```

### Explicação dos principais conceitos:
1. **Criação de dicionário**: Iniciamos com `{}` para um dicionário vazio ou incluímos pares de chave-valor entre `{}`.
2. **Acesso a valores**: Usamos `dicionario[chave]` para obter o valor de uma chave específica.
3. **Inserção e alteração de valores**: Podemos adicionar ou modificar pares de chave-valor usando `dicionario[chave] = valor`.
4. **Remoção de elementos**: Com `del dicionario[chave]` removemos uma chave e seu valor.
5. **Iteração**: Podemos percorrer as chaves de um dicionário usando um loop `for chave in dicionario`.
6. **Método `get()`**: Acessa um valor com uma opção de valor padrão caso a chave não exista.
