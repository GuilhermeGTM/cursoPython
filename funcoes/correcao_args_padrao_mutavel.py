# usando o none e o or o valor de sequencia sera [0, 1]
# assim corrigindo o erro do problema_args_padrao_mutavel
def fibonacci(sequencia=None):
    sequencia = sequencia or [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]
# assim o id fica diferente
# [0, 1, 1] 2111064789120
# [0, 1, 1, 2]
# [0, 1, 1] 2111067415744
