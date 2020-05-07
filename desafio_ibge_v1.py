#!/usr/bin/python3.6
import csv


def dados():
    with open('arquivos/desafio-ibge.csv', encoding='iso-8859-1') as dadosibge:
        dado = csv.DictReader(dadosibge)
        for linha in dado:
            print(f"Campo 9:{linha['nome_desti']}, Campo 4:{linha['nome_orige']}")


if __name__ == '__main__':
    dados()
