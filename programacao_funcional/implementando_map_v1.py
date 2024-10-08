# implementação simplificada do map

def mapear(funcao, lista):
    # criando um generator nosso
    for elemento in lista:
        print('passei por aqui!!!')
        yield funcao(elemento)


if __name__ == '__main__':
    print(list(mapear(lambda x: x ** 2, [2, 3, 4])))
