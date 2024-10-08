from mysql.connector import connect
from contextlib import contextmanager

# criando dicionario com os parametros de login do banco de dados
parametros = dict(
    host='localhost',
    port='3306',
    user='root',
    passwd='12345678',
    database='agenda'
)


# função usado no contexto do bloco with
@contextmanager
def nova_conexao():
    # criando conexão usando os parametros
    conexao = connect(**parametros)
    # retorna uma conexão
    try:
        yield conexao
    # caso esteja logado na conexão ele fecha com o close
    finally:
        if (conexao and conexao.is_connected()):
            conexao.close
            print('finally...')
