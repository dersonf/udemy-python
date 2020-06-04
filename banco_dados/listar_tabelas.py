from bd import nova_conexao
from mysql.connector import ProgrammingError

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute('SHOW TABLES')
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')

for i, tabela in enumerate(cursor, start=1):
    print(f'Tabela {i}: {tabela[0]}')
