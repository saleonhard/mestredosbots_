"""
Gerador de Meme

Descrição:
Este script gera uma imagem de meme com texto personalizado no topo e na parte inferior. Utiliza a biblioteca Pillow 
para manipulação de imagens e suporta a adição de texto com sombra para um efeito visual aprimorado. A fonte padrão 
é Impact, mas pode ser alterada através dos parâmetros fornecidos.

Objetivo:
Este script foi criado para fins de aprendizagem e demonstra como criar memes com texto sobre imagens usando Python.

Dependências:
- Python 3.x
- Pillow (PIL Fork): Biblioteca para manipulação de imagens.
- textwrap: Biblioteca para quebrar texto em várias linhas.

Função:
- gerar_meme: Gera um meme com texto no topo e na parte inferior da imagem.

Parâmetros da Função:
- image_path (str): Caminho para a imagem base.
- top_text (str): Texto a ser exibido no topo da imagem.
- bottom_text (str, opcional): Texto a ser exibido na parte inferior da imagem.
- font_path (str, opcional): Caminho para o arquivo de fonte (default: "./impact.ttf").
- font_size (int, opcional): Tamanho da fonte como percentual da altura da imagem (default: 0).

Como usar:
1. Coloque sua imagem no mesmo diretório ou forneça o caminho correto para `image_path`.
2. Certifique-se de que a fonte está disponível no caminho especificado ou ajuste `font_path`.
3. Chame a função `gerar_meme` com os parâmetros desejados.

Autor: Leonardo Aquino
Data de Criação: 20/09/2020

Licença:
Distribuído sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo conforme necessário.

"""

from PIL import Image, ImageDraw, ImageFont
import textwrap
import random
import string


def gerar_meme(
    image_path, top_text, bottom_text="", font_path="./impact.ttf", font_size=0
):
    # load image
    im = Image.open(image_path)
    draw = ImageDraw.Draw(im)
    image_width, image_height = im.size
    shadowcolor = "black"
    fontcolor = "yellow"

    # load font
    font = ImageFont.truetype(font=font_path, size=int(image_height * font_size) // 100)

    # convert text to uppercase
    top_text = top_text.upper()
    bottom_text = bottom_text.upper()

    # text wrapping
    char_width, char_height = font.getsize("A")
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(top_text, width=chars_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)

    #  top lines border
    y = 10
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x - 1, y - 1), line, fill=shadowcolor, font=font)
        draw.text((x + 1, y - 1), line, fill=shadowcolor, font=font)
        draw.text((x - 1, y + 1), line, fill=shadowcolor, font=font)
        draw.text((x + 1, y + 1), line, fill=shadowcolor, font=font)
        y += line_height

    # draw top lines
    y = 10
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill=fontcolor, font=font)
        y += line_height

    # bottom lines border
    y = image_height - char_height * len(bottom_lines) - 15
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x - 1, y - 1), line, fill=shadowcolor, font=font)
        draw.text((x + 1, y - 1), line, fill=shadowcolor, font=font)
        draw.text((x - 1, y + 1), line, fill=shadowcolor, font=font)
        draw.text((x + 1, y + 1), line, fill=shadowcolor, font=font)
        y += line_height

    # draw bottom lines
    y = image_height - char_height * len(bottom_lines) - 15
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill=fontcolor, font=font)
        y += line_height

    # save meme
    letters = strletters = string.ascii_lowercase
    out = "".join(random.choice(letters) for i in range(10))
    f_write = open("nome.txt", "w")
    f_write.write(str(out))
    f_write.close()
    im.save(out + ".jpg")
