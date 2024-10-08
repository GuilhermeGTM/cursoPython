# 0, 1, 1, 2, 3, 5, 8, 13, 21... sequencia de fibonacci

#       0 1 3 4 5 6 -->
# lista[i n d i c e]
#         ....-3-2-1 <---
def fibonacci(quantidade):  # parametro  quantidade
    resultado = [0, 1]  # lista
    for i in range(2, quantidade):  # a partir do 2
        # dentro do sum(soma) eu pego o -2 -1 por causa do :
        resultado.append(sum(resultado[-2:]))

    return resultado


if __name__ == '__main__':
    # listar os 20 primeiros numeros da sequencia
    for fib in fibonacci(20):
        print(fib)
