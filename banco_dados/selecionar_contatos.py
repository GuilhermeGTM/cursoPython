from mysql.connector.errors import ProgrammingError
from db import nova_conexao
# LIMIT é a quantidade que vc quer buscar
# OFFSET é de onde quer começar apartir de qual posição
# sql = 'SELECT * FROM contatos LIMIT %s OFFSET %s'
sql = 'SELECT * FROM contatos'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        # se eu usar o LIMIT E OFFSET usaria apos (sql,(10, 10))
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        # no banco a coluna 0 é nome, 1 é telefone e 3 é ID
        for contato in contatos:
            print(f'{contato[2]:2d} - {contato[0]:10s} Telefone: {contato[1]}')
