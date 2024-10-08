#! python
from math import pi
import sys

# criando uma função com retorno


def help():
    print("É necessário informar  o raio do circulo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0][0:]))


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:  # validando
        help()
    else:
        raio = sys.argv[1]  # obtendo argumento via terminal
        area = circulo(raio)
        print('Área do circulo: ', area)
