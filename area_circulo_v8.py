#!/usr/bin/python3.6
from math import pi
import sys


def help(erro):
    if erro == 1:
        print('Informar o parametro do raio.')
        print(f'Sintaxe: {sys.argv[0]} <raio> ')
    elif erro == 2:
        print('Insira um valor numerico')


def circulo(raio):
    return float(pi * (raio ** 2))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help(1)
        sys.exit(1)
    elif not sys.argv[1].isnumeric():
        help(2)
        sys.exit(1)
    else:
        area = circulo(float(sys.argv[1]))
        print(f'A área do círculo é {area:.2f}')
