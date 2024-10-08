arquivo = open('pessoas.csv')

for registro in arquivo:
    # strip tira as bordas no caso espaços em brancos e quebra de linhas
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()
