from bd import nova_conexao

sql = 'SELECT tel, nome FROM contatos'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    # Pega o primeiro registro como pop()
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
