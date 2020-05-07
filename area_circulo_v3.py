#!/usr/bin/python3.6
from math import pi


def circulo(raio):
    resultado = float(pi * (raio ** 2))
    print(f'A area do circulo e {resultado:.2f}')


if __name__ == '__main__':
    raio = float(input('Informe o raio:'))
    circulo(raio)
