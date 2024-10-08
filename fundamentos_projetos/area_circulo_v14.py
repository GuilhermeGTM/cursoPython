#! python
from math import pi
import sys
import errno

# criando uma função com retorno


def help():
    print("É necessário informar  o raio do circulo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0][0:]))


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:  # validando se foi colocado algum valor na entrada
        help()
        sys.exit(errno.EPERM)
    if not sys.argv[1].isnumeric():  # validando se não for numerico a entrada
        help()
        print('O raio deve ter um valor numerico')
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]  # obtendo argumento via terminal
    area = circulo(raio)
    print('Área do circulo: ', area)
