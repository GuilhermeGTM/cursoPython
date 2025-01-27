from mysql.connector.errors import ProgrammingError
from db import nova_conexao


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute('DROP TABLE IF EXISTS emails')
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
