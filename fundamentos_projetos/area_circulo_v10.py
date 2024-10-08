#! python
from math import pi
import sys

# criando uma função com retorno


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = sys.argv[1]  # obtendo argumento via terminal
    area = circulo(raio)
    print('Área do circulo: ', area)
