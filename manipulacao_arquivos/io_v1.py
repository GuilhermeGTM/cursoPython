# open,read,close são funções do buildings
arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()

# splitlines divine as linhas vai usar um delimitador para quebrar linhas
for registro in dados.splitlines():
    # print(*registro.split(','))
    # o split separa os registros por ,
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
