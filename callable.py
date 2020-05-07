#!/usr/bin/python3.6
def executar(funcao):
    print(callable(executar))
    if callable(funcao):
        funcao()


def bomdia():
    print('Bom dia!!!')


def boatarde():
    print('Boa tarde!!!')


if __name__ == '__main__':
    executar(boatarde)
    executar(bomdia)
    executar(boanoite)
