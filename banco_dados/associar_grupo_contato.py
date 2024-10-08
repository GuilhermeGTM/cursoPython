from mysql.connector.errors import ProgrammingError
from db import nova_conexao

selecionar_grupo = 'SELECT id FROM grupos WHERE descricao = %s'
atualizar_contato = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s'

# dicionario
contato_grupo = {
    'Ana': 'Casa',
    'Bia': 'Trabalho',
    'Luca': 'Casa',
    'Lu': 'Casa',
    'Gui': 'Trabalho',
    'Beca': 'Trabalho',
    'Pedro': 'Trabalho',
    'Lucas Yuri': 'Casa',
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        # for no dicionario
        for contato, grupo in contato_grupo.items():
            # consulta para selecionar o grupo passando o grupo
            cursor.execute(selecionar_grupo, (grupo,))
            # pegando o id
            grupo_id = cursor.fetchone()[0]
            # atualizando
            cursor.execute(atualizar_contato, (grupo_id, contato))
            conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('Contatos associados')
