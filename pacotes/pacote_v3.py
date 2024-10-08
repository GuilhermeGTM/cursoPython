# aqui temos 2 nomes iguais de modulo1 sendo que
# pacote1 e pacote2 contem modulo1
# colocando as modulo1_sub colocando um apelido para n ter conflito
from pacote1 import modulo1
from pacote2 import modulo1 as modulo1_sub

print('Soma', modulo1.soma(3, 2))
print('Subtração', modulo1_sub.subtracao(3, 2))
