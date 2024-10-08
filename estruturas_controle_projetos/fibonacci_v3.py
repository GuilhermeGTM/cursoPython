# 0, 1, 1, 2, 3, 5, 8, 13, 21... sequencia de fibonacci
def fibonacci(limite):  # parametro  limite
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=',')  # imprimiu o 0,1 no console
    while ultimo < limite:  # colocando um limite no while
        # penultimo recebe ultimo = 1
        # ultimo recebe penultimo + ultimo 1+1 = 2
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo,  end=',')


if __name__ == '__main__':
    fibonacci(10000)  # parametro limite de  10000
