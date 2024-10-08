
# bloco
try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        # strip tira as bordas no caso espaços em brancos e quebra de linhas
        # foi tirado o * para dar erro no *registro
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
# mesmo dando erro no codigo ele seguiu com o except indexerror
# o bloco está vazio com o pass
# except IndexError:
#    pass
# finally sempre sera executado mesmo que o codigo der erro no caso no bloco
finally:
    # print('finally')
    arquivo.close()

# testa se o arquivo foi fechado
if arquivo.closed:
    print('Arquivo foi fechado')
