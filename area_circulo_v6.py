#!/usr/bin/python3.6
from math import pi
import sys


def circulo(raio):
    return float(pi * (raio ** 2))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Informar o parametro do raio.')
        print(f'Sintaxe: {sys.argv[0]} <raio> ')
    else: 
        area = circulo(float(sys.argv[1]))
        print(f'A área do círculo é {area:.2f}')
