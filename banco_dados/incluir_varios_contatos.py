from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Ana', '96765-5341'),
    ('Bia', '96565-3341'),
    ('Gustavo', '96775-2341'),
    ('Armando', '93765-4141'),
    ('Jusefa', '96465-4371'),
    ('Jardirene', '96768-4241'),
    ('Maria', '99765-4641')
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluídos { cursor.rowcount } registros!')
