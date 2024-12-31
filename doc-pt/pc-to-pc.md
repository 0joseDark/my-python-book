Para criar dois scripts em Python que se comuniquem pela internet entre dois PCs, permitindo escrever, modificar e apagar texto usando o teclado, você pode usar **Flask** como servidor HTTP e **requests** para a comunicação. Um dos scripts será o servidor Flask que armazena e manipula o texto, enquanto o outro será o cliente que envia os dados.

Aqui estão os passos:

### Script 1: Servidor (Python Flask)
Este script atuará como servidor, recebendo texto e permitindo modificações.

1. **Instalar Flask**:
   ```bash
   pip install Flask
   ```

2. **Código do Servidor**:
   ```python
   from flask import Flask, request, jsonify

   app = Flask(__name__)

   # Armazenamento do texto
   texto_armazenado = ""

   # Criar rota para ler o texto
   @app.route('/texto', methods=['GET'])
   def obter_texto():
       return jsonify({'texto': texto_armazenado})

   # Criar rota para modificar o texto
   @app.route('/texto', methods=['POST'])
   def modificar_texto():
       global texto_armazenado
       novo_texto = request.json.get('texto')
       if novo_texto:
           texto_armazenado = novo_texto
           return jsonify({'mensagem': 'Texto atualizado com sucesso!'})
       return jsonify({'mensagem': 'Nenhum texto enviado!'}), 400

   # Criar rota para apagar o texto
   @app.route('/texto', methods=['DELETE'])
   def apagar_texto():
       global texto_armazenado
       texto_armazenado = ""
       return jsonify({'mensagem': 'Texto apagado com sucesso!'})

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)  # Servidor disponível na rede
   ```

### Explicação (Servidor):
- **Flask** cria rotas para **GET** (obter texto), **POST** (modificar texto) e **DELETE** (apagar texto).
- O texto é armazenado na variável `texto_armazenado`.
- O servidor Flask está configurado para escutar em todas as interfaces da rede (`0.0.0.0`), permitindo o acesso de outros PCs.

### Script 2: Cliente (Python com requests)
Este script enviará solicitações para o servidor, permitindo que você escreva, modifique ou apague o texto.

1. **Instalar requests**:
   ```bash
   pip install requests
   ```

2. **Código do Cliente**:
   ```python
   import requests

   # URL do servidor Flask
   url_servidor = 'http://<IP_DO_SERVIDOR>:5000/texto'

   def obter_texto():
       resposta = requests.get(url_servidor)
       if resposta.status_code == 200:
           print("Texto atual no servidor:", resposta.json()['texto'])
       else:
           print("Erro ao obter o texto")

   def modificar_texto():
       novo_texto = input("Digite o novo texto: ")
       resposta = requests.post(url_servidor, json={'texto': novo_texto})
       if resposta.status_code == 200:
           print(resposta.json()['mensagem'])
       else:
           print("Erro ao modificar o texto")

   def apagar_texto():
       resposta = requests.delete(url_servidor)
       if resposta.status_code == 200:
           print(resposta.json()['mensagem'])
       else:
           print("Erro ao apagar o texto")

   def menu():
       while True:
           print("\n1. Obter Texto")
           print("2. Modificar Texto")
           print("3. Apagar Texto")
           print("4. Sair")
           opcao = input("Escolha uma opção: ")

           if opcao == '1':
               obter_texto()
           elif opcao == '2':
               modificar_texto()
           elif opcao == '3':
               apagar_texto()
           elif opcao == '4':
               break
           else:
               print("Opção inválida, tente novamente.")

   if __name__ == '__main__':
       menu()
   ```

### Explicação (Cliente):
- **requests** é usado para enviar **GET**, **POST** e **DELETE** ao servidor Flask.
- O cliente permite ao usuário visualizar, modificar ou apagar o texto no servidor.
- Insira o IP do servidor Flask na variável `url_servidor`.

### Passos:
1. No **PC Servidor**, execute o **script do servidor Flask**.
2. No **PC Cliente**, execute o **script do cliente**.
3. Use o menu do cliente para se comunicar com o servidor, enviando texto para criar, modificar ou apagar.

Esses scripts criarão uma comunicação básica entre dois PCs usando texto e teclas.
