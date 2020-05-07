#!/usr/bin/python3.6
from random import randint

def sortear_dado():
    return randint(1, 6)


if __name__ == '__main__':
    sorteado = sortear_dado()
    print(sorteado)
    for i in range(1, 7):
        if i % 2 == 1:
            continue

        if sorteado == i:
            print('Acertou')
            break
    else:
        print('Errrrouuuu!!!')

