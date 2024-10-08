
# with ele fecha o arquivo automatico sem precisar do closed
with open('pessoas.csv') as arquivo:  # modo leitura
    # o segundo parametro é o 'w' modo de escrita saida
    with open('pessoas.txt', 'w')as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            # a saida vai ser no tipo arquivo vai criar um arquivo pessoa.txt
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

# teste para ver se arquivo foi fechado
if arquivo.closed:
    print('Arquivo foi fechado')
# teste para ver se saida foi fechado
if saida.closed:
    print('saida foi fechado')
