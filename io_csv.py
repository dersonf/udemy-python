#!/usr/bin/python3.6
import csv

with open('arquivos/pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))

