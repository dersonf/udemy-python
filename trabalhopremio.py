#!/usr/bin/python3.6

primeirotrabalho = input('Deu certo o primeiro trabalho? (OK/NOK):')
segundotrabalho = input('Deu certo o segundo trabalho? (OK/NOK):')

if primeirotrabalho == 'OK' and segundotrabalho == 'OK':
    print('Vai gastar com uma TV de 50" e sorvete pra familia.')
elif primeirotrabalho != segundotrabalho:
    print('Vai gastar com uma TV de 32" e sorvete pra familia.')
else:
    print('Vai ficar em casa, sem gastar $$$ e sem comer gordice!!!')

