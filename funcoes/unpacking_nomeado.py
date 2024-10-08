# **kwargs
# exemplo de unpacking
# pegando um dicionario desempacotando ele passando como parametro /
# para uma função que recebe 3 parametros
def resultado_f1(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')


if __name__ == '__main__':
    # dicionario desempacotado
    podium = {'segundo': 'M. Verstappen',
              'primeiro': 'L. Hamilton',
              'terceiro': 'S. Vettel'}
    resultado_f1(**podium)
