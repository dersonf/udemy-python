#!/usr/bin/python3.6
from math import pi


def circulo(raio):
    return float(pi * (raio ** 2))
    #print(f'A area do circulo e {resultado:.2f}')


if __name__ == '__main__':
    raio = float(input('Informe o raio: '))
    area = circulo(raio)
    print(f'A área do círculo é {area:.2f}')
