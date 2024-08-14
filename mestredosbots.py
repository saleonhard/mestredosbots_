"""
Mestre Dos Bots - Worker de Resposta e Interação - Arquivo Main

Descrição:
Este script faz parte do projeto "Mestre Dos Bots" e é responsável por interagir com menções no Twitter. 
O bot responde a menções com mensagens personalizadas e imagens geradas dinamicamente, além de 
monitorar e interagir com tendências. O script utiliza a API do Twitter para buscar e responder a tweets 
e a API do Google Sheets para gerenciar dados relacionados a menções e frases.

Objetivo:
O projeto foi desenvolvido para fins de aprendizado e aprimoramento das habilidades em programação, 
automação de tarefas com bots, e integração com APIs do Twitter e Google Sheets.

Dependências:
- Python 3.x
- tweepy: Biblioteca para interagir com a API do Twitter.
- gspread: Biblioteca para manipular planilhas do Google Sheets.
- oauth2client: Biblioteca para autenticação via OAuth 2.0.
- Outros módulos personalizados: gerador_meme, trends, keys.

Como usar:
1. Configure suas credenciais da API do Twitter e do Google Sheets.
2. Insira suas credenciais nos arquivos `keys.py` e `credenciais.json` (ou use variáveis de ambiente).
3. Execute o script em um ambiente apropriado, como o Heroku, para garantir que ele execute continuamente.

Autor: Leonardo Aquino
Data de Criação: 20/09/2020

Licença:
Distribuído sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo conforme necessário.

"""

import tweepy
import time
from keys import *
from gerador_meme import *
import random
import string
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from trends import *

nome = "nome.txt"
out = ""


img = "./" + out + ".jpg"


# Usando as credenciais do Google Drive API
scope = ["https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json", scope)
client = gspread.authorize(creds)

# Abrindo planilha.
sheet = client.open("Mestre Dos Bots").sheet1

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def reply_to_tweets(last_seen_id=0):
    print("🔎 Buscando por menção de um pupilo...", flush=True)
    rt = False

    # last_seen_id = retrieve_last_seen_id(FILE_NAME)
    last_seen_id = int(sheet.acell("A44").value)

    tweets = api.search(
        q="#mestredosbots  OR  #seupupilodisse -filter:retweets",
        since_id=last_seen_id,
        count=50,
        tweet_mode="extended",
    )
    for tweet in reversed(tweets):

        if (
            tweet.id != last_seen_id
            and tweet.author.screen_name.lower() != "mestredosbots"
        ):
            print("	Menção encotrada 😀\n")
            last_seen_id = tweet.id
            sheet.update("A44", str(last_seen_id))
            # store_last_seen_id(last_seen_id, FILE_NAME)
            print("	Ultimo ID", last_seen_id)
            print("	Novo ID:", tweet.id)
            print("	Name:", tweet.author.name)
            print("	User:", tweet.author.screen_name)
            print("	Data do Tweet:", tweet.created_at)
            print("	Tweet:", tweet.full_text)
            txt = tweet.full_text.lower()

            if "#mestredosbots" in txt:
                print("	Tipo de Resposta: #MestreDosBots")
                tipo = random.randint(1, 5)
                print("Random: ", tipo)
                if tipo <= 3:
                    print("🧙🏻‍♂️ Mestre")
                    sheet2 = client.open("Mestre Dos Bots").worksheet("Frases")
                    num = int(sheet2.acell("C2").value)
                    while True:
                        linha = str(random.randint(2, num))
                        frase = str(sheet2.acell("A" + linha).value)
                        if frase != " ":
                            break

                        time.spleep(5)

                    top_text = "Saudaçao, jovem @" + tweet.author.screen_name
                    bottom_text = frase
                    ind = random.randint(1, 10)
                    img = "./mestre" + str(ind) + ".jpg"
                else:
                    print("👳 Pupilos")
                    sheet3 = client.open("Mestre Dos Bots").worksheet("Frases Pupilos")
                    num = int(sheet3.acell("E8").value)
                    while True:
                        linha = str(random.randint(2, num))
                        frase = str(sheet3.acell("A" + linha).value)
                        user = str(sheet3.acell("B" + linha).value)
                        status = sheet3.acell("C" + linha).value.lower()
                        if frase != " " and status == "true":
                            break

                        time.sleep(5)

                    top_text = "como disse meu/minha pupilo(a) " + user + " :"
                    bottom_text = frase
                    ind = random.randint(1, 10)
                    img = "./pupilo" + str(ind) + ".jpg"

            else:
                print("	Tipo de Resposta: #SeuPupiloDisse")
                if "https://t.co/" in txt:
                    txt = txt[:-23]
                txt = txt.replace("#seupupilodisse", "")

                if txt == "" and tweet.in_reply_to_status_id is None:
                    user = "@" + str(tweet.author.screen_name)

                    bottom_text = "Não há frase alguma aqui, jovem...\nVocê está vendo coisa...\nEspera! Por acaso você comeu algum daqueles cogumelos do pântano?"
                    txt = bottom_text
                    top_text = "Saudação, jovem " + user
                    ind = random.randint(1, 10)
                    img = "./mestre" + str(ind) + ".jpg"
                else:

                    rt = True
                    ind = random.randint(1, 10)
                    img = "./pupilo" + str(ind) + ".jpg"

                    if tweet.in_reply_to_status_id is not None:

                        user = (
                            "@"
                            + str(
                                api.get_status(
                                    id=tweet.in_reply_to_status_id,
                                    tweet_mode="extended",
                                ).author.screen_name
                            ).lower()
                        )

                        txt = txt.replace(user, "")

                    if txt == "" or txt == " ":

                        # print('	ID: ', tweet.in_reply_to_status_id)
                        user = api.get_status(
                            id=tweet.in_reply_to_status_id, tweet_mode="extended"
                        ).author.screen_name
                        txt = api.get_status(
                            id=tweet.in_reply_to_status_id, tweet_mode="extended"
                        ).full_text
                        if "https://t.co/" in txt:
                            txt = txt[:-23]
                        txt = txt.replace("#seupupilodisse", "")

                        bottom_text = txt
                        top_text = "meu/minha pupilo(a) @" + user + " me disse:"
                    else:

                        user = "@" + str(tweet.author.screen_name)

                        bottom_text = txt
                        top_text = "meu/minha pupilo(a) " + user + " me disse:"
            print("📝 Frase de resposta:", bottom_text)

            gerar_meme(img, top_text=top_text, bottom_text=bottom_text, font_size=5.5)

            f_read = open(nome, "r")
            out = f_read.read().strip()
            f_read.close()
            time.sleep(45)
            api.update_with_media(
                "./" + out + ".jpg",
                status="@" + tweet.user.screen_name,
                possible_sensitive=False,
                in_reply_to_status_id=tweet.id,
            )
            print(" ✅ Respondido!")
            os.remove("./" + out + ".jpg")

            if rt:
                rpy = api.user_timeline("@mestredosbots", count=1)
                for r in rpy:
                    print(r.text)
                    time.sleep(15)
                    api.retweet(r.id)
                rt = False

    else:
        print("	Nenhuma menção  encotrada 😢")
        print("_______________________________________")


while True:

    reply_to_tweets()
    cont = 0
    fim = ""

    buscar = sheet.acell("D9").value.lower()

    if buscar == "true":
        print("🔎 Buscando...")
        buscar_trends()
        buscar = sheet.acell("D9").value.lower()
        print(buscar)
        fim = ""
        cont = 0
        while buscar == "false":
            print(cont, "⌛ Agurdando...")
            curtir = sheet.acell("D19").value.lower()
            if curtir == "true":
                print("👍 Curtindo...")
                fim = like_trends()
            if fim == "fim" or cont == 15:
                break
            time.sleep(2)
            buscar = sheet.acell("D9").value.lower()
            cont += 1
    time.sleep(10)
