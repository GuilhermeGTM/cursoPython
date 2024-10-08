import csv
from urllib import request


def read(url):
    # requisição dentro de um bloco with acessando como entrada
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
# leitura da entrada acessando como decode latin1 para pegar acentos
# armazenando em dados
        dados = entrada.read().decode('latin1')
        print('Download completo!')
# foi usado o csv.reader para ler as linhas de fato separado por ,
        for cidade in csv.reader(dados.splitlines()):
            # foi usado fstring para imprimir a 8 e a 3 coluna
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    # foi usado a strin r row para entepretar os caracteres especiais
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
