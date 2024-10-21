
```python
import re

def number_markdown_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.readlines()

    numbered_content = []
    heading_counts = [0] * 6  # Para h1 a h6

    for line in content:
        match = re.match(r'^(#{1,6})\s+(.*)$', line)
        if match:
            level = len(match.group(1))
            heading_counts[level-1] += 1
            for i in range(level, 6):
                heading_counts[i] = 0
            
            number = '.'.join(str(count) for count in heading_counts[:level] if count > 0)
            numbered_line = f"{match.group(1)} {number} {match.group(2)}\n"
            numbered_content.append(numbered_line)
        else:
            numbered_content.append(line)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(numbered_content)

# Uso do script
input_file = 'input.md'
output_file = 'output_numbered.md'
number_markdown_file(input_file, output_file)
print(f"Ficheiro numerado criado: {output_file}")

```

Este script faz o seguinte:

1. Lê um ficheiro Markdown de entrada.
2. Percorre cada linha do ficheiro.
3. Se encontrar um cabeçalho (linha que começa com #), adiciona uma numeração automática.
4. Escreve o conteúdo numerado em um novo ficheiro.

Para usar o script:
1. Salve-o como `number_markdown.py`.
2. Coloque seu ficheiro Markdown de entrada na mesma pasta com o nome `input.md`.
3. Execute o script com `python number_markdown.py`.
4. O ficheiro numerado será criado como `output_numbered.md`.

Agora, vou fazer um resumo das formatações Markdown mais comuns:

1. Cabeçalhos:
   ```
   # Cabeçalho 1
   ## Cabeçalho 2
   ### Cabeçalho 3
   ```

2. Ênfase:
   ```
   *itálico* ou _itálico_
   **negrito** ou __negrito__
   ***negrito e itálico*** ou ___negrito e itálico___
   ```

3. Listas:
   ```
   - Item não ordenado
   * Outro item não ordenado
   
   1. Item ordenado
   2. Outro item ordenado
   ```

4. Links:
   ```
   [Texto do link](https://www.exemplo.com)
   ```

5. Imagens:
   ```
   ![Texto alternativo](caminho/para/imagem.jpg)
   ```

6. Citações:
   ```
   > Isto é uma citação.
   ```

7. Código:
   ```
   `código em linha`
   
   ```python
   # bloco de código
   def funcao():
       return True
   ```
   ```

8. Linhas horizontais:
   ```
   ---
   ```

9. Tabelas:
   ```
   | Cabeçalho 1 | Cabeçalho 2 |
   |-------------|-------------|
   | Célula 1    | Célula 2    |
   ```

10. Listas de tarefas:
    ```
    - [x] Tarefa concluída
    - [ ] Tarefa pendente
    ```

Estas são as formatações mais comuns em Markdown. O Markdown é projetado para ser fácil de ler e escrever, e pode ser convertido para HTML e muitos outros formatos.
