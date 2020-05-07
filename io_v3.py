#!/usr/bin/python3.6
arquivo = open('arquivos/pessoas.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()

