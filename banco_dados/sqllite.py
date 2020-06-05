from sqlite3 import connect, ProgrammingError, Row

tabela_grupo = """
    CREATE TABLE IF NOT EXISTS grupos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao VARCHAR(30)
    )
"""

tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50),
        tel VARCHAR(40),
        grupo_id INTEGER,
        FOREIGN KEY (grupo_id) REFERENCES grupos(id)
    )
"""

insert_grupos = 'INSER INTO (descricao) VALUES (?)'
select_grupos = 'SELECT id, descricao FROM grupos'
insert_contatos = 'INSERT INTO contatos (nome, tel, grupo_id) VALUES (?, ?, ?)'
select = """
    SELECT grupos.descricao AS grupo,

