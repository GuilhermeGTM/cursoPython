from mysql.connector import connect

# criando conexão com banco de dados
conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='12345678'
)

# testando conexão
print(conexao)
