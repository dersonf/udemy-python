#!/usr/bin/python3.6
import csv
from urllib import request


def read(url):
    with request.urlopen(url) as download:
        print('Baixando o CSV...')
        dados = download.read() 
        dadoscsv = csv.reader(dados)
        for pessoa in csv.reader(dados):
            print(pessoa)


#    with request.urlopen(url) as download:
#        print('Baixando o CSV...')
#        dados = csv.DictReader(download.read().decode('latin-1'))
            #planilha = csv.DictReader(planilha)
            #for linha in csv.reader(planilha.splitlines()):
#        for linha in dados:
#            print(linha)
            #print(f"Campo 9:{linha['nome_desti']}, Campo 4:{linha['nome_orige']}")


#    with open('arquivos/desafio-ibge.csv', encoding='iso-8859-1') as dadosibge:
#        dado = csv.DictReader(dadosibge)
#        for linha in dado:
#            print(f"Campo 9:{linha['nome_desti']}, Campo 4:{linha['nome_orige']}")


if __name__ == '__main__':
    read(r'http://localhost/desafio-ibge.csv')
