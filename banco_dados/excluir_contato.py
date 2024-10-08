from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'DELETE FROM  contatos WHERE nome = %s'
args = ('Lucas',)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        # o commit tem que ser dado sempre que for alterar a tabela
        # seja em um DELETE ou INSERT, tipo no SELECT n precisa
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        # rowcount conta a quantidade de registros
        print(f'{cursor.rowcount} registro(s) deletado(s).')
