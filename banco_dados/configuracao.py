from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='aferneda',
    passwd='12345678'
)

print(conexao)
