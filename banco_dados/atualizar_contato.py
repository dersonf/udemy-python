from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'UPDATE contatos set nome = %s WHERE id = %s'
args = ('Wanderleia', 16)

print(args)
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Registro {args[1]} atualizado para {args[0]}.')
