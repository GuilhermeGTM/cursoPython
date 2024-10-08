# parametro lista mutavel
def fibonacci(sequencia=[0, 1]):
    # uso de mutaveis como o valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))  # [0, 1, 1] 2212857729152
    print(fibonacci(inicio))  # [0, 1, 1, 2]
    restart = fibonacci()
    print(restart, id(restart))  # [0, 1, 1, 2, 3] 2212857729152
    # ou seja passar um parametro mutavel não é uma boa pratica
    # ele retorou diferente do padrão
    # por isso se usa uma tupla pelo fato de ser imutavel
    assert restart == [0, 1, 1]
