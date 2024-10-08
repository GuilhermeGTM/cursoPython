#! python
from math import pi

# criando uma função com retorno


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area = circulo(raio)
    print('Área do circulo: ', area)
