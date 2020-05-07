#!/usr/bin/python3.6
from math import pi
import sys


def circulo(raio):
    return float(pi * (raio ** 2))


if __name__ == '__main__':
    area = circulo(float(sys.argv[1]))
    print(f'A área do círculo é {area:.2f}')
