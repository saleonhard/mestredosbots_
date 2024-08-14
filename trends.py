"""
Mestre Dos Bots - Worker de Tendências - Arquivo Aux

Descrição:
Este script faz parte do projeto "Mestre Dos Bots" e é responsável por buscar e interagir com tendências no Twitter. 
O bot coleta as tendências atuais para o Brasil, atualiza uma planilha do Google Sheets com essas tendências, e 
curte tweets relacionados a essas tendências. Utiliza a API do Twitter para buscar e curtir tweets, e a API do 
Google Sheets para atualizar e gerenciar dados.

Objetivo:
O projeto tem como objetivo aprender e aplicar habilidades em programação, automação de tarefas com bots, e 
integração com APIs do Twitter e Google Sheets.

Dependências:
- Python 3.x
- tweepy: Biblioteca para interagir com a API do Twitter.
- gspread: Biblioteca para manipular planilhas do Google Sheets.
- oauth2client: Biblioteca para autenticação via OAuth 2.0.
- Outros módulos personalizados: gerador_meme, keys.

Como usar:
1. Configure suas credenciais da API do Twitter e do Google Sheets.
2. Insira suas credenciais nos arquivos `keys.py` e `credenciais.json` (ou use variáveis de ambiente).
3. Execute o script para buscar tendências e curtir tweets relacionados às tendências.

Autor: Leonardo Aquino
Data de Criação: 20/09/2020

Licença:
Distribuído sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo conforme necessário.

"""

import numpy as np
import tweepy
import time
from keys import *
from gerador_meme import *
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

# Usando as credenciais do Google Drive API
scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json', scope)
client = gspread.authorize(creds)

# Abrindo planilha.
sheet = client.open("Mestre Dos Bots").sheet1
  
# WOEID do Brasil
woeid = 23424768
  
# Buscar trends
def buscar_trends():
   data = api.trends_place(id = woeid)
   trends = data[0]["trends"]
   col = 2 
   num = int(sheet.acell('D4:D5').value)
   print('Os trending topics atualizados são: ')
   for trend in trends[:num]:

            print(trend['name']) 
            sheet.update_cell(col, 1, trend['name'])
            col +=1
            
   sheet.update('D9', False)
   
#Curtindo trends selecionados  
def like_trends():	
  sheet.update('D9', False)
  qnt = sheet.acell('C14:D15').value
  num = int(sheet.acell('D4:D5').value) + 2
  print(num)
  for x in range(2, num):
      print(sheet.acell('A'+str(x)).value )
      ativo = (sheet.acell('B'+str(x)).value).lower()
      if ativo == 'true':
        
        t  = sheet.acell('A'+str(x)).value + ' -filter:retweets'
        tweets = api.search(q= t,lang = 'pt',count= int(qnt), tweet_mode='extended')
        for tweet in reversed(tweets):
              print(tweet.full_text +'\n')
              api.create_favorite(tweet.id)
              time.sleep(14)
        sheet.update('B'+str(x), False)
              
  sheet.update('D19', False)
  return 'fim'			
							   
