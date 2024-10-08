# sequencia é uma tupla
def fibonacci(quantidade, sequencia=(0, 1)):
    # importante condição de parada

    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    # listar os 20 primeiros numeros da sequencia
    for fib in fibonacci(20):
        print(fib)
