# for i in range(1, 11):
#    print(i)
# else:
#    print('Fim')

from random import randint


def sortear_dado():  # função
    return randint(1, 6)  # gera um numero inteiro aleatório do 1 ao 6


for i in range(1, 7):  # percorre uma lista do 1 ao 6
    if i % 2 == 1:  # verefica se o numero é impar pulando ele e continuando
        continue
# veferica se sortear_dado é igual ao i numeros pares por causa do filtro acima
    if sortear_dado() == i:

        print('Acerteou', i)
        break
# se tu não achou o numero par sorteado dentro do for ele cai no else
else:
    print('Não acertou o numero')
