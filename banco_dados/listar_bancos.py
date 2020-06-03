from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='aferneda',
    passwd='12345678'
)

cursor = conexao.cursor()
cursor.execute('SHOW DATABASES')

for i, database in enumerate(cursor, start=1):
    print(f'Banco de Dados {i}: {database[0]}')

#for i in cursor:
#    print(i)

#print(tuple(cursor))
