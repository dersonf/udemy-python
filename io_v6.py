#!/usr/bin/python3.6
with open('arquivos/pessoas.csv') as arquivo:
    with open('arquivos/pessoas.txt', 'w') as saida:
        for registro in arquivo:
           pessoa = registro.strip().split(',')
           print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo entrada fechado!')


if saida.closed:
    print('Arquivo saida fechado!')
