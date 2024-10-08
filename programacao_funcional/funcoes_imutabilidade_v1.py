from functools import reduce
from operator import add

# lista
valores = [30, 10, 25, 70, 100, 94]

# não mudou a lista original de forma imutavel
print(sorted(valores))
print(valores)

# desta maneira a lista original foi mudada pq é mutavel
# valores.sort()
# print(valores)
# valores.reverse()
# print(valores)

# esses comandos não modificam a lista mesmo ela sendo mutavel
print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(reversed(valores))
print(list(reversed(valores)))
print(valores)
