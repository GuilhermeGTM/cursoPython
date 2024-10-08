# 0, 1, 1, 2, 3, 5, 8, 13, 21... sequencia de fibonacci
def fibonacci(limite):  # parametro  limite
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=',')  # imprimiu o 0,1 no console
    while ultimo < limite:  # colocando um limite no while
        proximo = penultimo + ultimo  # proximo = 0 + 1
        print(proximo,  end=',')  # imprimiu proximo 0+1=1
        penultimo = ultimo  # penultimo recebeu o ultimo
        ultimo = proximo  # ultimo vai ser a soma do proximo


if __name__ == '__main__':
    fibonacci(10000)  # parametro limite de  10000
