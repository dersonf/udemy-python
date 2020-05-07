#!/usr/bin/python3.6
with open('arquivos/pessoas.csv') as arquivo:
    for registro in arquivo:
       print('Nome: {}, Idade: {}'.format(registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo já foi fechado!')
