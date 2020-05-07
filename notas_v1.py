#!/usr/bin/python3.6
import sys


def resultado(conceito):
    print(f'Conceito {conceito}')


nota = float(sys.argv[1])

if __name__ == '__main__':
    if nota > 10 or nota < 0:
        print('Digite um valor válido (0-10)')
        sys.exit(1)
    if nota >= 9.1:
        resultado('A')
    elif nota >= 8.1:
        resultado('A-')
    elif nota >= 7.1:
        resultado('B')
    elif nota >= 6.1:
        resultado('B-')
    elif nota >= 5.1:
        resultado('C')
    elif nota >= 4.1:
        resultado('C-')
    elif nota >= 3.1:
        resultado('D')
    elif nota >= 2.1:
        resultado('D-')
    elif nota >= 1.1:
        resultado('E')
    else:
        resultado('E-')
