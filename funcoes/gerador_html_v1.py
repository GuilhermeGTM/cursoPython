# função que vai criar um bloco recebendo 1 parametros e uma classe

def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == "__main__":
    # teste (assertions) para ver se vai ter algum erro
    # caso a frase do html está diferente vai gerar erro
    assert tag_bloco('Incluido com sucesso!') == \
        '<div class="success">Incluido com sucesso!</div>'
    assert tag_bloco('Impossivel excluir!', 'error') == \
        '<div class="error">Impossivel excluir!</div>'
    # vai sair o resultado <div class="success">bloco</div>
    print(tag_bloco('bloco'))
