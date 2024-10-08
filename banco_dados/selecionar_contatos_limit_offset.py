from mysql.connector.errors import ProgrammingError
from db import nova_conexao
# LIMIT limita a quantidade de busca
# OFFSET apartir de qual contato se quer buscar
# para funcionar o OFFSET tem que ter o LIMIT
sql = 'SELECT * FROM contatos LIMIT %s OFFSET %s'
args = (3, 8)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato[2]:2d} - {contato[0]:10s} Telefone: {contato[1]}')
