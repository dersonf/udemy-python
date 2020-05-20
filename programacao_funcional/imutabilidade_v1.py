#!/usr/bin/python3
from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Português do Brasil
setlocale(LC_ALL, 'pt_BR')


# Listar todos os meses do ano com 31 dias
def meseslongos():
    # pega o indice que é igual a 31
    meses_31 = filter(lambda mes: mdays[mes] == 31, range(1, 13))
    # pega o indice e transforma em nome do mês
    meses_nomes = map(lambda mes: month_name[mes], meses_31)
    # junta tudo pra ficar bonito
    juntar_meses = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
                          meses_nomes, 'Meses com 31 dias:')
    return juntar_meses


if __name__ == '__main__':
    print(meseslongos())


# uma segunda forma de fazer
print(
    reduce(
        lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
        map(
            lambda mes: month_name[mes],
            filter(
                lambda mes: mdays[mes] == 31,
                range(1, 13)
            )
        ),
        'Meses com 31 dias:'
    )
)
