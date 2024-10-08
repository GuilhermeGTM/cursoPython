# 0, 1, 1, 2, 3, 5, 8, 13, 21... sequencia de fibonacci

#       0 1 3 4 5 6 -->
# lista[i n d i c e]
#         ....-3-2-1 <---
def fibonacci(limite):  # parametro  limite
    resultado = [0, 1]  # lista
    # colocando um limite no while -1 é o ultimo elemento da lista
    while resultado[-1] < limite:
        # dentro do sum eu pego o -2 -1 por causa do :
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(10000):
        print(fib)
