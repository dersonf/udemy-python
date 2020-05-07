#!/usr/bin/python3.6
try:
    arquivo = open('arquivos/pessoas.csv')
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(registro.strip().split(',')))
finally:
    print('Fechando arquivo!')
    arquivo.close()

print('FIM')
