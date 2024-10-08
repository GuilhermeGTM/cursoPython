# implementação simplificada do map

def mapear(funcao, lista):
    # tbm da para usar um generator não precisando emplementar com yirld
    # fazendo o mesmo trabalho que um map
    # usamos a função generator
    return (funcao(elemento) for elemento in lista)


if __name__ == '__main__':
    print(list(mapear(lambda x: x ** 2, [2, 3, 4])))
