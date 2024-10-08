# **kwargs
# exemplo de packing
# temos a chamada de varios parametros para a função resultado_f1
# ele pacata dentro do dicinario
def resultado_f1(**podium):  # foi tudo pacotado dentro do **podium
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    # parametros para função f1
    resultado_f1(primeiro='L. Hamilton',
                 segundo='M. Verstappen',
                 terceiro='S. Vettel')
