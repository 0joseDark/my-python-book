- [voltar atrás](https://github.com/0joseDark/my-python-book/blob/main/index.md)
- Para criar uma API RESTful em Python, vamos usar o framework Flask, que é leve e fácil de configurar. Aqui está o passo a passo para criar uma API RESTful simples com Flask:

### Instalação de Dependências

1. **Instalar Flask**:
   Se ainda não tiver Flask instalado, instale-o usando `pip`:

   ```bash
   pip install Flask
   ```

2. **Instalar outras dependências (opcional)**:
   Caso queira trabalhar com manipulação de JSON ou bancos de dados como SQLite, pode instalar bibliotecas adicionais.

---

### Estrutura do Projeto

Vamos criar um projeto simples com os seguintes ficheiros:
- `app.py` — O ficheiro principal com a API.
- `data.json` (opcional) — Um ficheiro que contém dados para simulação de um banco de dados.

```bash
/api_restful_project
  ├── app.py
  └── data.json
```

---

### Passo 1: Estrutura Básica da API

Crie o ficheiro `app.py`:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados simulados (poderia ser de um banco de dados)
usuarios = [
    {'id': 1, 'nome': 'João Silva', 'idade': 30},
    {'id': 2, 'nome': 'Maria Oliveira', 'idade': 25},
    {'id': 3, 'nome': 'Carlos Pereira', 'idade': 40}
]

# Rota para obter todos os usuários
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios), 200

# Rota para obter um único usuário pelo ID
@app.route('/api/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        return jsonify(usuario), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404

# Rota para adicionar um novo usuário
@app.route('/api/usuarios', methods=['POST'])
def adicionar_usuario():
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201

# Rota para atualizar um usuário existente
@app.route('/api/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        dados_atualizados = request.get_json()
        usuario.update(dados_atualizados)
        return jsonify(usuario), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404

# Rota para apagar um usuário
@app.route('/api/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        usuarios.remove(usuario)
        return jsonify({'mensagem': 'Usuário removido com sucesso'}), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

---

### Passo 2: Explicação do Código

1. **Importações e inicialização do Flask**:
   - `Flask`: Importamos o módulo Flask para criar a aplicação.
   - `jsonify`: Para converter objetos Python em formato JSON.
   - `request`: Para obter dados enviados pelos métodos `POST` e `PUT`.

2. **Simulação de banco de dados**:
   - Criamos uma lista `usuarios` com alguns dados fictícios. Em uma aplicação real, estes dados viriam de um banco de dados.

3. **Rotas (endpoints)**:
   - Cada rota está associada a uma função que responde a um determinado caminho (`/api/usuarios`) e método HTTP (`GET`, `POST`, etc.).

4. **Funções de cada rota**:
   - `GET /api/usuarios`: Retorna todos os usuários.
   - `GET /api/usuarios/<int:id>`: Retorna um usuário específico com base no ID.
   - `POST /api/usuarios`: Adiciona um novo usuário. Os dados são enviados em formato JSON no corpo da requisição.
   - `PUT /api/usuarios/<int:id>`: Atualiza um usuário existente.
   - `DELETE /api/usuarios/<int:id>`: Remove um usuário da lista.

5. **Execução**:
   - O `app.run(debug=True)` inicializa a aplicação Flask no modo de desenvolvimento, o que nos permite ver erros e recarregar a aplicação automaticamente.

---

### Passo 3: Testando a API

Agora, para testar a API, você pode usar ferramentas como o **Postman** ou o **cURL**. Aqui estão alguns exemplos de testes:

1. **Obter todos os usuários**:

   ```bash
   curl -X GET http://127.0.0.1:5000/api/usuarios
   ```

2. **Adicionar um novo usuário**:

   ```bash
   curl -X POST http://127.0.0.1:5000/api/usuarios \
   -H "Content-Type: application/json" \
   -d '{"id": 4, "nome": "Ana Costa", "idade": 22}'
   ```

3. **Atualizar um usuário existente**:

   ```bash
   curl -X PUT http://127.0.0.1:5000/api/usuarios/2 \
   -H "Content-Type: application/json" \
   -d '{"nome": "Maria Oliveira", "idade": 26}'
   ```

4. **Deletar um usuário**:

   ```bash
   curl -X DELETE http://127.0.0.1:5000/api/usuarios/3
   ```

---

### Conclusão

Este é um exemplo simples de uma API RESTful usando Flask. A API permite realizar operações básicas de CRUD (Create, Read, Update, Delete) com usuários. Para expandir, você pode integrar um banco de dados, autenticação, e mais validações nos dados recebidos.
