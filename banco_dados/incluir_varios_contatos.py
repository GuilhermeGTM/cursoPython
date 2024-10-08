from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES(%s, %s)'
args = (
    ('Ana', '96765-4321'),
    ('Bia', '97765-4321'),
    ('Luca', '89765-4321'),
    ('Lu', '99765-4321'),
    ('Gui', '98735-4321'),
    ('Beca', '98765-2221'),
    ('Pedro', '98765-6721'),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        # quanto for mais de 1 registro se usa o executemany
        cursor.executemany(sql, args)
        # só vai funcionar com conexao.commit() caso contrario ele não vai
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'forum incluidos {cursor.rowcount} registros!')
