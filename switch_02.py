#!/usr/bin/python3.6
from random import randint


def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado',
    }
    return dias.get(dia, '**invalido**')


if __name__ == '__main__':
    sorteiadia = randint(1, 7)
    print(get_dia_semana(sorteiadia))
    



