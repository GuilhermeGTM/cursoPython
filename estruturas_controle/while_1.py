# while True:
#     print('Vai demorar muito0000')

from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)  # radiant coloca um numeo random

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o numero: '))

print('Número secreto {} foi encontrado!'.format(numero_secreto))
