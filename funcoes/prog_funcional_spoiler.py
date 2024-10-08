# passando uma função como parametro dento de uma função
def executar(funcao):
    # no caso foi passado um parametro int 1 no executar /
    # então foi colocado o callable para tirar o erro
    if callable(funcao):
        funcao()


def bom_dia():
    print('Bom dia!')


def boa_tarde():
    print('Boa tarde!')


if __name__ == '__main__':
    executar(bom_dia)
    executar(boa_tarde)
    executar(1)
