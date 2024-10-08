
# with ele fecha o arquivo automatico sem precisar do closed
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

# testar se o arquivo foi fechado
if arquivo.closed:
    print('Arquivo foi fechado')
