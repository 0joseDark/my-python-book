Em Python, um conjunto (ou *set*) é uma coleção de elementos únicos e desordenados. Eles são úteis para armazenar elementos sem duplicatas e para realizar operações matemáticas como união, interseção e diferença entre conjuntos.

### Características dos conjuntos:
1. **Elementos únicos**: Não permite valores duplicados.
2. **Desordenado**: Não garante a ordem dos elementos.
3. **Imutáveis**: Não podem conter elementos mutáveis, como listas, mas podem conter valores de tipos imutáveis como números, strings e tuplas.

### Exemplo de criação e uso de um conjunto:

```python
# Criando um conjunto com alguns elementos
frutas = {"maçã", "banana", "laranja"}

# Adicionando um elemento ao conjunto
frutas.add("uva")
print("Conjunto após adicionar uva:", frutas)  # Saída: {'maçã', 'banana', 'laranja', 'uva'}

# Tentando adicionar um elemento duplicado
frutas.add("maçã")
print("Conjunto após tentar adicionar 'maçã' novamente:", frutas)  # A 'maçã' já existe, então não será adicionada novamente

# Removendo um elemento do conjunto
frutas.remove("banana")
print("Conjunto após remover 'banana':", frutas)

# Verificando a presença de um elemento
print("A 'laranja' está no conjunto?", "laranja" in frutas)  # Saída: True

# Operações com conjuntos:
# Criando outro conjunto para demonstração
frutas_citricas = {"laranja", "limão"}

# União de conjuntos
todos_frutas = frutas.union(frutas_citricas)  # Combina todos os elementos dos dois conjuntos
print("União de frutas e frutas_citricas:", todos_frutas)

# Interseção de conjuntos
frutas_comuns = frutas.intersection(frutas_citricas)  # Apenas os elementos presentes em ambos os conjuntos
print("Interseção de frutas e frutas_citricas:", frutas_comuns)

# Diferença de conjuntos
frutas_exclusivas = frutas.difference(frutas_citricas)  # Elementos em 'frutas' que não estão em 'frutas_citricas'
print("Diferença de frutas e frutas_citricas:", frutas_exclusivas)

# Conjunto final
print("Conjunto final:", frutas)
```

### Explicação dos principais conceitos:
1. **Criação de conjunto**: Usamos `{}` para definir um conjunto com elementos.
2. **Adição de elementos**: Com o método `add()`, adicionamos elementos, e os duplicados são ignorados automaticamente.
3. **Remoção de elementos**: Com `remove()`, podemos remover um item específico.
4. **Verificação de presença**: `in` verifica se um elemento está no conjunto.
5. **Operações de conjuntos**:
   - **União** (`union()`): Junta todos os elementos de dois conjuntos.
   - **Interseção** (`intersection()`): Retorna elementos comuns aos dois conjuntos.
   - **Diferença** (`difference()`): Mostra elementos presentes em um conjunto, mas não no outro.
