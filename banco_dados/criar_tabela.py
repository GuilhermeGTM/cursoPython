from db import nova_conexao
from mysql.connector.errors import ProgrammingError

# criando tabale contatos pode colocar IF NOT EXISTS ai não vai dar o erro
tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos(
        nome VARCHAR(50),
        tel VARCHAR(40)
    )
"""

# criando tabela emails
tabela_emails = """
    CREATE TABLE emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50)
    )
"""

# tratando a exceção da tabela_contatos e tabela_emails
# caso de um erro tentando criar novamente ele cai no ProgrammingError
# se quiser tratar o erro de fora coloca-se try fora da conexão ->
# e o except no mesmo bloco
# que poderia ser trataro dentro da nova_conexão
try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(tabela_contatos)
            cursor.execute(tabela_emails)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')
