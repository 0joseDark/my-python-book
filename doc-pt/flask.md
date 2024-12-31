- [voltar atrás](https://github.com/0joseDark/my-python-book/blob/main/index.md)
- Flask é um micro framework em Python, que facilita o desenvolvimento de aplicações web. Ele é simples, leve, e extensível, o que significa que você pode começar com o básico e depois adicionar funcionalidades conforme necessário, sem a complexidade de frameworks maiores.
Estrutura Básica de uma Aplicação Flask

Vamos criar uma aplicação básica com Flask e explicar o passo a passo.
Passo 1: Instalar Flask

Primeiro, é necessário instalar o Flask. Se ainda não o fez, pode usar o pip:

bash

pip install Flask

Passo 2: Criar a Estrutura do Projeto

A estrutura mais simples de um projeto Flask pode ser algo como:

meu_projeto/
    app.py

Passo 3: Criar o Script app.py

Dentro de app.py, criaremos a nossa aplicação Flask. Aqui está um exemplo básico de código:

python

from flask import Flask

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Define a rota principal, que corresponde à URL '/'
@app.route('/')
def index():
    return 'Olá, Flask!'

# Inicia o servidor web
if __name__ == '__main__':
    app.run(debug=True)

Explicação:

    Importação do Flask: A primeira linha importa o módulo Flask, que fornece as funcionalidades principais do framework.
    Instância da Aplicação: app = Flask(__name__) cria uma instância da classe Flask. O argumento __name__ diz ao Flask onde procurar os recursos e módulos associados à aplicação.
    Rota: @app.route('/') define a rota principal (a URL) que a aplicação irá servir. Quando o utilizador visita a URL principal (por exemplo, http://localhost:5000/), a função index é chamada e retorna a string Olá, Flask!.
    Execução da Aplicação: A linha if __name__ == '__main__': garante que a aplicação só é executada quando o script app.py é executado diretamente. O método app.run() inicia o servidor web integrado do Flask e o parâmetro debug=True ativa o modo de depuração, permitindo rastrear erros em tempo real.

Passo 4: Executar a Aplicação

Para iniciar a aplicação Flask, execute o seguinte comando na pasta onde está o app.py:

bash

python app.py

Agora, se abrir um navegador e acessar http://localhost:5000/, verá a mensagem "Olá, Flask!".
Extensão da Aplicação

Aqui estão algumas funcionalidades mais avançadas que podem ser adicionadas a uma aplicação Flask:

    Receber Dados via Formulário: Para lidar com métodos HTTP como POST e GET, podemos usar o request para extrair dados de formulários ou URLs.

    Exemplo:

    python

from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return f'Bem-vindo, {username}!'
    return '''
        <form method="post">
            Username: <input type="text" name="username">
            <input type="submit">
        </form>
    '''

Templates com Jinja2: Flask suporta a renderização de templates HTML usando o Jinja2. Para isso, colocamos os ficheiros HTML numa pasta chamada templates e usamos render_template.

Exemplo:

python

from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

Conteúdo de templates/hello.html:

html

<html>
    <body>
        <h1>Olá, {{ name }}!</h1>
    </body>
</html>

JSON e APIs: Flask pode facilmente criar APIs RESTful, retornando respostas no formato JSON.

Exemplo:

python

    from flask import jsonify

    @app.route('/api/data')
    def get_data():
        data = {'key': 'valor', 'numero': 42}
        return jsonify(data)

Passo 5: Desdobramento de Funcionalidades

Com Flask, é possível adicionar mais funcionalidades usando extensões, como autenticação, bases de dados (usando SQLAlchemy, por exemplo), ou gestão de sessões. Aqui estão algumas opções populares:

    Flask-SQLAlchemy: Integração com bases de dados.
    Flask-Login: Gerenciamento de sessões de utilizadores.
    Flask-WTF: Suporte a formulários avançados.

Conclusão

Flask é ideal para quem quer começar com uma aplicação web em Python sem muita complexidade inicial. Ele permite que você construa desde simples páginas estáticas até APIs complexas e aplicações dinâmicas, adicionando funcionalidades conforme necessário.

