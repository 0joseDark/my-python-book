## 📌 O que é uma API?

**API** significa **Application Programming Interface** (Interface de Programação de Aplicações).
É um **conjunto de regras e definições** que permite que diferentes programas, sistemas ou serviços **comuniquem entre si**.

👉 Pensa nela como um **"contrato" ou "ponte"**:

* Um programa expõe funções, dados ou serviços.
* Outro programa pode **usar essas funções** sem precisar saber como foram implementadas internamente.

---

## 📌 Analogia simples

Imagina um **restaurante** 🍽️:

* Tu és o cliente.
* A **cozinha** é o sistema interno (complexo, cheio de processos).
* O **menu** é a API: ele mostra o que podes pedir e como pedir.
* O **empregado** (API) leva o pedido, entrega na cozinha e traz a comida pronta.

Assim, tu não precisas saber **como cozinham**, só precisas do **menu (API)**.

---

## 📌 Tipos principais de API

1. **APIs locais (bibliotecas/frameworks)**

   * Exemplo: Em Python, quando usas `math.sqrt(9)`, estás a usar a **API da biblioteca math**.

2. **APIs de sistema operativo**

   * O Windows, Linux ou macOS oferecem APIs para abrir ficheiros, criar janelas, aceder a hardware, etc.

3. **APIs web**

   * Permitem que aplicações comuniquem via **HTTP**.
   * Exemplo: A API do **Google Maps** para obter mapas, a API do **Twitter/X** para ler e escrever tweets.

---

## 📌 Como funciona uma API Web

1. O cliente (um programa ou browser) faz um **pedido HTTP**:

   ```
   GET https://api.exemplo.com/utilizadores/123
   ```
2. O servidor responde em **JSON ou XML**:

   ```json
   {
     "id": 123,
     "nome": "Ricardo",
     "idade": 30
   }
   ```
3. O cliente usa estes dados na sua aplicação (ex.: mostrar num site ou app).

---

## 📌 Vantagens de usar APIs

* **Reutilização**: não precisas reinventar a roda.
* **Integração**: conectar sistemas diferentes (ex.: app do Uber usa API do Google Maps).
* **Escalabilidade**: separar serviços em módulos independentes.
* **Segurança**: o sistema só expõe o que quer, mantendo o resto escondido.

---

## 📌 Exemplo prático em Python (API Web)

```python
import requests

# Faz um pedido à API pública "catfact"
resposta = requests.get("https://catfact.ninja/fact")

# Mostra o resultado em JSON
if resposta.status_code == 200:
    dados = resposta.json()
    print("Fato sobre gatos:", dados["fact"])
else:
    print("Erro ao aceder à API")
```

---

✅ **Resumindo**:
Uma **API é uma interface** que permite que programas e sistemas comuniquem de forma organizada, sem o utilizador precisar saber como tudo funciona “por dentro”.
