from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce


# portugues do brasil
setlocale(LC_ALL, 'pt_br')

# listar todos meses do ano com 31 dias
# 1.(filter) pegar os indices de todos os meses com 31 dias 1,3,5...
# 2.(map) transformar os indices em nome
# 3.(reduce) juntar tudo  para imprimir

meses_31 = filter(lambda mes: mdays[mes] == 31, range(1, 13))
meses_nome = map(lambda mes: month_name[mes], meses_31)
juntar_meses = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
                      meses_nome, 'Meses com 31 dias:')
print(juntar_meses)

# tbm da para fazer assim
print(
    reduce(
        lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
        map(
            lambda mes: month_name[mes],
            filter(
                lambda mes: mdays[mes] == 31,
                range(1, 13)
            )
        ),
        'Meses com 31 dias:'
    )
)
