from db import nova_conexao

sql = "SELECT * FROM contatos WHERE nome like %s "

with nova_conexao() as conexao:
    nome = input('Contato a localizar: ')
    # %{nome}% busca oq vc digitou oq contem
    # {nome}% busca oq começa oq foi digitado
    # %{nome} busca oq termina oq foi digitado
    # a , é para dizer que é uma tupla
    args = (f'%{nome}%',)

    # passando os argumentos separado do sql
    # assim não tem alteração e perigo de sql injection
    cursor = conexao.cursor()
    cursor.execute(sql, args)

    for x in cursor:
        print(x)
