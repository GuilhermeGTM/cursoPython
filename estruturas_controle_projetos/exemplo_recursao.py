def imprimir(maximo, atual):
    if atual < maximo:  # condição de parada
        print(atual)
        # recursão
        imprimir(maximo, atual + 1)  # valor atual vai ser acrescentado +1


imprimir(990, 1)
