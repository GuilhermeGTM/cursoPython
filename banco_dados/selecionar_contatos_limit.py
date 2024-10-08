from mysql.connector.errors import ProgrammingError
from db import nova_conexao
# LIMIT busca somente 5 resultados primeiros
sql = 'SELECT * FROM contatos LIMIT 5'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato[2]:2d} - {contato[0]:10s} Telefone: {contato[1]}')
