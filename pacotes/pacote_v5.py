# com o pacote calc eu consigo importar direto pelo __all__ mais facil
# vc pode criar um pacote que agrupa diversas funcionalidades de um sistema
# pacote como uma fachada usando outros pacotes tudo nesse
from calc import soma, subtracao


print('Soma', soma(3, 2))
print('Subtração', subtracao(3, 2))
