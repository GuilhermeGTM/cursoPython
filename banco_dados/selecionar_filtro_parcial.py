from db import nova_conexao
# like '%ca%' ele busca todos que tem a letra ca
# like 'Lu% busca todos que começa com LU
# like '%a' busca todos que termina com a
sql = "SELECT * FROM contatos WHERE nome like '%ca%'"

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)
