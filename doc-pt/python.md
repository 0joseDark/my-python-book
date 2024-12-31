![douctor](https://github.com/0joseDark/0joseDark/blob/main/assets/douctor-inteiro-trabalhando.jpg)
- [voltar atrás](https://github.com/0joseDark/my-python-book/blob/main/index.md)
- 1.1 O que é Python?

Python é uma linguagem de programação de alto nível, interpretada, criada por Guido van Rossum e lançada em 1991. Ela destaca-se pela sua simplicidade e legibilidade, sendo uma excelente escolha tanto para iniciantes quanto para programadores experientes. Python é amplamente utilizado em diversas áreas, como desenvolvimento web, automação, análise de dados, inteligência artificial, machine learning, e muito mais. A sua sintaxe simples e limpa permite aos programadores concentrar-se na resolução de problemas, sem se perder em detalhes complexos da linguagem.
Vantagens do Python:

    Código legível e fácil de manter.
    Grande comunidade e biblioteca extensa de pacotes e módulos.
    Multi-paradigma: suporta programação orientada a objetos, funcional e procedural.
    Portabilidade: funciona em diversos sistemas operativos, como Windows, macOS e Linux.
    Excelente integração com outras linguagens e tecnologias.

1.2 Instalação e Configuração

Para começar a programar em Python, é necessário instalar o interpretador Python no teu sistema. Python é compatível com os principais sistemas operativos, como Windows, macOS e Linux.
1.2.1 Instalar Python no Windows, macOS e Linux

Windows:

    Acede ao site oficial do Python (python.org) e faz o download do instalador para Windows.
    Executa o instalador e marca a opção "Add Python to PATH" para garantir que o Python será acessível a partir do terminal.
    Conclui a instalação seguindo as instruções no ecrã.

macOS:

    Python já vem pré-instalado no macOS, mas pode ser uma versão antiga. Para instalar a versão mais recente, utiliza o Homebrew:

    bash

    brew install python

    Homebrew instalará o Python e o pip (gestor de pacotes do Python).

Linux:

    Na maioria das distribuições Linux, o Python já está pré-instalado. Para garantir que tens a versão mais recente, usa o seguinte comando:

    bash

sudo apt update
sudo apt install python3

Para verificar se o Python foi instalado corretamente, executa:

bash

    python3 --version

1.2.2 Utilizar o pip para gerir pacotes

pip é o gestor de pacotes do Python, permitindo instalar, atualizar e desinstalar bibliotecas e módulos de terceiros. Estes pacotes são essenciais para expandir as funcionalidades do Python.

Verificar a instalação do pip:

    Após instalar o Python, o pip geralmente é instalado automaticamente. Para verificar:

    bash

    pip --version

Instalar um pacote:

    Para instalar um pacote usando o pip, usa o comando:

    bash

pip install nome-do-pacote

Por exemplo, para instalar a biblioteca requests, que facilita a comunicação HTTP:

bash

    pip install requests

Atualizar um pacote:

bash

pip install --upgrade nome-do-pacote

Desinstalar um pacote:

bash

pip uninstall nome-do-pacote

1.3 Executar o Primeiro Programa em Python

Após instalar o Python, é altura de executar o teu primeiro programa. Um programa clássico para começar é o “Olá, Mundo!”.
Passos para criar o programa:

    Criar um ficheiro Python:
        Abre um editor de texto (como o Notepad no Windows, TextEdit no macOS ou o editor Nano no Linux).
        Escreve o seguinte código:

        python

    print("Olá, Mundo!")

Guardar o ficheiro:

    Guarda o ficheiro com a extensão .py, por exemplo, ola_mundo.py.

Executar o programa:

    Abre o terminal ou prompt de comando.
    Navega até ao diretório onde guardaste o ficheiro.
    Executa o seguinte comando:

    bash

python nome_do_ficheiro.py

No caso do exemplo, o comando seria:

bash

        python ola_mundo.py

Se tudo correr bem, o output será:

css

Olá, Mundo!

Com isso, já terás o Python instalado no teu sistema e serás capaz de escrever e executar os teus primeiros programas. O Python é uma linguagem muito flexível e poderosa, e estes primeiros passos vão abrir caminho para explorares mais funcionalidades e bibliotecas que a linguagem oferece.
