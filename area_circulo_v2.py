#!/usr/bin/python3.6
from math import pi

if __name__ == '__main__':
    raio = float(input('Informe o raio:'))
    resultado = float(pi * (raio ** 2))
    print(f'A area do circulo e {resultado:.2f}')

