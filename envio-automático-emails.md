O envio automático de emails em Python pode ser feito com a biblioteca `smtplib`, que facilita a comunicação com servidores SMTP (Simple Mail Transfer Protocol). Para enviar emails automáticos, vamos configurar um servidor SMTP, criar uma mensagem de email e usar as credenciais da conta de envio (como Gmail ou Outlook). Se você quiser anexar arquivos, a biblioteca `email` oferece ferramentas para formatar a mensagem e adicionar anexos.

Aqui está um exemplo básico de envio de email usando o Gmail, que inclui configurações e código comentado.

---

### Passo 1: Configuração de uma Conta de Envio (Gmail)

1. **Permitir Aplicativos Menos Seguros**:
   Para contas do Gmail, acesse [Acesso a apps menos seguros](https://myaccount.google.com/lesssecureapps) e ative-o. O Gmail restringe aplicativos "menos seguros" por padrão.

2. **Gerar Senha de Aplicativo**:
   Para maior segurança, use uma senha específica para aplicativos. No painel de segurança da conta do Google, gere uma senha de aplicativo para enviar emails via Python.

---

### Exemplo Básico: Envio de Email Simples

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do servidor SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587
email_sender = "seu_email@gmail.com"
email_password = "sua_senha"

# Configurações do destinatário e da mensagem
email_recipient = "destinatario@gmail.com"
subject = "Email Automático com Python"
body = "Este é um email automático enviado por um script em Python."

# Cria a mensagem
msg = MIMEMultipart()
msg["From"] = email_sender
msg["To"] = email_recipient
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

try:
    # Conecta ao servidor e envia o email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Segurança TLS
    server.login(email_sender, email_password)  # Login
    server.sendmail(email_sender, email_recipient, msg.as_string())
    print("Email enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar o email: {e}")
finally:
    server.quit()
```

### Explicação do Código:

1. **Configuração SMTP**: Define o servidor SMTP (Gmail usa `smtp.gmail.com` na porta `587` para conexão TLS).
2. **Mensagem**: Criamos uma mensagem usando `MIMEMultipart` para facilitar o uso de múltiplas partes, como corpo de texto e anexos.
3. **Envio do Email**:
   - Conectamos ao servidor SMTP usando o protocolo TLS.
   - Fazemos login usando o email e a senha do remetente.
   - Enviamos o email com `sendmail`.
4. **Fechamento da Conexão**: Com o método `server.quit()`, encerramos a conexão com o servidor SMTP.

---

### Exemplo com Anexo

Para adicionar um anexo, podemos usar `MIMEBase` e `encoders`.

```python
from email.mime.base import MIMEBase
from email import encoders
import os

# Definir o caminho do arquivo que deseja anexar
file_path = "caminho_do_arquivo/a_anexar.txt"

# Lê o arquivo e cria uma parte MIME para o anexo
attachment = MIMEBase("application", "octet-stream")
with open(file_path, "rb") as f:
    attachment.set_payload(f.read())

# Codifica em Base64
encoders.encode_base64(attachment)
attachment.add_header(
    "Content-Disposition",
    f"attachment; filename= {os.path.basename(file_path)}",
)

# Anexa o arquivo à mensagem
msg.attach(attachment)
```

Basta adicionar o código acima após a criação da mensagem para incluir o anexo.

---

### Notas Finais

1. **Outros Servidores SMTP**: Se você estiver usando outro serviço de email (como Outlook, Yahoo), use o servidor e a porta correspondentes.
2. **Tratamento de Erros**: O exemplo inclui um bloco `try-except` para capturar e exibir erros durante o envio.
3. **Envio de Vários Emails**: Para enviar a vários destinatários, você pode adicionar uma lista de emails em `email_recipient` e iterar sobre ela, ou passar uma string com emails separados por vírgula.

Esses exemplos cobrem os princípios básicos do envio automático de emails em Python.
