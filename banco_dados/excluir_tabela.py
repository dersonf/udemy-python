from bd import nova_conexao
from mysql.connector import ProgrammingError


apaga_tabela = """
    DROP TABLE IF EXISTS emails
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(apaga_tabela)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
