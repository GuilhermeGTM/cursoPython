compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14},
)


def calc_preco_total(compra):
    return compra['quantidade'] * compra['preco']


totais = tuple(map(calc_preco_total, compras))

print('Preços torais:', totais)
print('Totais geral:', sum(totais))
