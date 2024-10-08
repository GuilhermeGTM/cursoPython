#! python
from math import pi

# criando uma função de retorno


def circulo(raio):
    print('Área do circulo', pi * float(raio) ** 2)


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)
