#!/usr/bin/python3.6
from math import pi
import sys


class Colors:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def help(erro):
    if erro == 1:
        print('Informar o parametro do raio.')
        print(f'Sintaxe: {sys.argv[0]} <raio> ')
    elif erro == 2:
        print(Colors.ERRO + f'{sys.argv[1]} não é um valor numerico' +
              Colors.NORMAL)


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
