[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fsaleonhard%2Fmestredosbots_&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

<p align="center">
  <img src="https://github.com/user-attachments/assets/56c16b3d-37d3-498f-849b-1932b37069bb" alt="Descrição da Imagem" width="900" height="auto" />
</p>

# 🧙‍ Mestre Dos Bots

## Descrição

O projeto **Mestre Dos Bots** é um bot desenvolvido para interagir com o Twitter e o Google Sheets, criado em setembro de 2020 com o propósito de aprendizado. Inspirado no personagem **Mestre dos Magos** do desenho animado **"A Caverna do Dragão"**, o bot emula o estilo enigmático e inspirador desse mentor enigmático, conhecido por suas respostas misteriosas e conselhos valiosos. Na série baseada no jogo de RPG Dungeons & Dragons, o Mestre dos Magos orienta um grupo de adolescentes transportados para um mundo mágico, tentando encontrar o caminho de volta para casa e enfrentando diversos desafios, oferecendo uma direção mística e sábia. O bot tem o objetivo de responder aos usuários (ou "pupilos") com mensagens enigmáticas e inspiradoras, refletindo o estilo do personagem e proporcionando uma experiência interativa e mística.


## Funcionalidades

- **Busca por Menções**: O bot procura por menções no Twitter usando hashtags específicas e responde com memes personalizados.
- **Respostas Automatizadas**: Responde a tweets com imagens geradas a partir de frases armazenadas em uma planilha do Google Sheets.
- **Interação com Tendências**: Busca e curte tweets relacionados às tendências do Twitter.
- **Atualização de Planilha**: Mantém uma planilha do Google Sheets atualizada com as tendências atuais e o status das interações.

## Hashtags Utilizadas

O bot utiliza as seguintes hashtags para buscar interações no Twitter:

- **#mestredosbots**: Utilizada para buscar menções diretas ao bot e responder com memes enigmáticos.
- **#seupupilodisse**: Usada para responder a frases ou mensagens enviadas por "pupilos" com imagens geradas a partir das frases.
  
Além dessas hashtags, o bot também busca por tendências no Twitter para aumentar o engajamento e curte tweets relacionados, conforme configurado na planilha do Google Sheets.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Tweepy**: Biblioteca para interação com a API do Twitter.
- **Gspread**: Biblioteca para manipulação de planilhas do Google Sheets.
- **Pillow**: Biblioteca para processamento de imagens e geração de memes.
- **Numpy**: Biblioteca para computação numérica.
- **OAuth2Client**: Biblioteca para autenticação OAuth.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas. Você pode instalar todas as dependências com o seguinte comando:

```bash
pip install -r requirements.txt

```

## Arquivos e Diretórios

- **`mestredosbots.py`**: Script principal que gerencia a interação com o Twitter e o Google Sheets. Ele busca menções, responde com memes, e lida com as tendências do Twitter.
- **`timeline.py`**: Script auxiliar para buscar e curtir tweets relacionados às tendências.
- **`requirements.txt`**: Arquivo de dependências que lista as bibliotecas Python necessárias para o projeto.
- **`keys.py`**: Arquivo onde estão armazenadas as credenciais da API do Twitter (não incluído no repositório por segurança).
- **`credenciais.json`**: Arquivo de credenciais para a API do Google Sheets (deve ser obtido e configurado conforme as instruções).
- **`gerador_meme.py`**: Script responsável pela geração de memes com base nas frases armazenadas e nas imagens fornecidas.
- **`trends.py`**: Script que lida com a busca e a manipulação das tendências do Twitter.
- **`nome.txt`**: Arquivo que armazena o nome da imagem que será usada para responder aos tweets.
- **Imagens (`*.jpg`)**: Diretório contendo as imagens usadas para gerar os memes.

### Scripts Principais

- **`mestredosbots.py`**:
  - Autentica com o Twitter e Google Sheets.
  - Busca por menções e responde com memes personalizados.
  - Atualiza a planilha do Google Sheets com informações de menções e tendências.
  - Faz interações automáticas, como curtir tweets e retweetar.

- **`timeline.py`**:
  - Busca por tendências no Twitter e curte tweets relacionados a essas tendências com base nas configurações da planilha.

### Funções Importantes

- **`buscar_trends()`**: Função que busca e atualiza as tendências do Twitter na planilha.
- **`like_trends()`**: Função que curte tweets relacionados às tendências especificadas na planilha.
- **`reply_to_tweets()`**: Função que responde a menções no Twitter com mensagens enigmáticas e memes.

## Configuração

### Google Sheets API

1. Crie um projeto no [Google Cloud Console](https://console.developers.google.com/).
2. Ative a API do Google Sheets e crie credenciais de serviço.
3. Baixe o arquivo de credenciais e renomeie-o para `credenciais.json`.

### Twitter API

1. Crie um aplicativo no [Twitter Developer Portal](https://developer.twitter.com/).
2. Gere e insira as credenciais da API no arquivo `keys.py`.

### Planilha Google

1. Crie uma planilha chamada "Mestre Dos Bots" e adicione as abas necessárias para armazenar frases e informações de tendências.

## Uso

### Configuração do Ambiente

1. Configure as credenciais e a planilha conforme as instruções acima.
2. Certifique-se de que os arquivos de imagem para memes estão no diretório correto.

### Execução

Execute o script principal para iniciar o bot:

```bash
python mestredosbots.py

```
<p align="center">
  <img src="https://github.com/user-attachments/assets/c83308d9-a2da-4aaf-861f-6d9a913edea6" alt="Descrição da Imagem" width="500" height="auto" />
</p>

## Observações

- ⏳ O bot foi configurado para esperar 15 minutos entre cada verificação de novos seguidores, para evitar o limite de taxa da API do Twitter.
- 🖼️ As imagens e mensagens devem estar corretamente configuradas no diretório onde o script é executado.

## Licença

📜 Este projeto é distribuído sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo como quiser! ✨.

## Contato
Se você tiver alguma dúvida ou sugestão, entre em contato:
    
- ✉️ **Email:** sa.leonardo13@gmail.com
- 🔗 **LinkedIn:** [LinkedIn - Leonardo Aquino](https://linkedin.com/in/aquinoleonardo/)  
     
