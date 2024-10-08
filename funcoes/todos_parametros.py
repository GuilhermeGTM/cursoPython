# *args parametros posicionais variaveis
# *kwargs nomeados variaveis
def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs:{kwargs}')


if __name__ == "__main__":
    # parametros posicionais
    todos_params('a', 'b', 'c')
    # retornou
    # args: ('a', 'b', 'c')
    # kwargs: {}

    # parametros nomeados
    todos_params('1', '2', '3', legal=True, valor=12.99)
    # retornou
    # args: ('1', '2', '3')
    # kwargs: {'legal': True, 'valor': 12.99}

    # 'Ana', False, [1,2,3] parametros posicionais *args
    # tamanho='M', fragil=false parametros nomeados **kwargs
    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
    # retornou
    # args: ('Ana', False, [1, 2, 3])
    # kwargs: {'tamanho': 'M', 'fragil': False}
