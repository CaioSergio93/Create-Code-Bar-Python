**API Geradora de Código de Barras**

Bem-vindo ao repositório da API Geradora de Código de Barras. Esta API permite que você gere imagens de código de barras com base em dados de entrada.

**Instalação de Requisitos**

Após baixar o repositorio na sua maquina, insira o seguinre comando em seu terminal, para que baixe todas as dependencias da API:

_pip install -r requirements.txt_

**Rotas Disponíveis para consumo**

1. Rota: /create_tag
Método HTTP: **POST**
Descrição: Esta rota permite criar uma nova tag com base nos dados fornecidos.
Parâmetros de Requisição:
Os dados da tag devem ser fornecidos no corpo da requisição no formato JSON.
