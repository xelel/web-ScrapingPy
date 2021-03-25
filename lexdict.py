from bs4 import BeautifulSoup
from collections import defaultdict
import codecs
from glob import glob


# armazena os nomes dos arquivos que terminam com a extensão .htm ou html
arquivos = glob('*.ht*')


dados = defaultdict(list)  # dicionario de listas com os dados das paginas
t = ''
for arq in arquivos:
    # analise pagina submarino
    if arq.endswith('.html'):  # percorre os .html do submarino

        with codecs.open(arq, encoding='utf-8') as fp:
            submarino = BeautifulSoup(fp, 'lxml')
         # titulo da pagina
        titulo_Html = submarino.title.string

    # acha as informacoes html na árvore
        informacoes_Html = submarino.select('tbody tr td span')

    # transforma a lista em uma string
        informacoes_Html = ''.join([str(i) for i in informacoes_Html])

    # converte para objeto beautifulSoup
        informacoes_Html = BeautifulSoup(informacoes_Html, 'lxml')
        for texto in informacoes_Html.stripped_strings:  # percorre os textos de informações html
            dados[titulo_Html].append(texto)

    # analise pagina magazine luiza
    if arq.endswith('.htm'):
        with codecs.open(arq, encoding='utf-8') as m:
            magazine = BeautifulSoup(m, 'lxml')
        titulo = magazine.title.string

    # extrai as informações tecnicas na árvore
        info_Produto_Html = magazine.find_all(
            'td', class_=['description__information-left', 'description__information-right'])

    # transforma a lista em uma string
        texto = ''.join([str(i) for i in info_Produto_Html])

# converte a string para objeto BeautifulSoup()
        texto = BeautifulSoup(texto, 'lxml')

# coloca os valores de texto em uma lista

        for i in texto.stripped_strings:
            dados[titulo].append(i)


for k, v in dados.items():
    print('-='*60)
    print(k)
    print('-='*60)

    for values in v:
        print(values)
