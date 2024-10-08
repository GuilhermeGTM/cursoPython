from generators_v1 import cores_arco_iris


if __name__ == '__main__':
    generator = cores_arco_iris()
    # o for aqui faz a mesma coisa que o next só que ele trata
    # por isso não vimos o StopIteration do next do exemplo anterior
    # ele trata isso internamente
    for cor in generator:
        print(cor)
    print('Fim!')
