from db import nova_conexao

# ORDER BY ordena por nome ASC padrão, DESC decrescente
sql = 'SELECT nome, id FROM contatos ORDER BY nome DESC'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    print('\n'.join(str(registro) for registro in cursor))
