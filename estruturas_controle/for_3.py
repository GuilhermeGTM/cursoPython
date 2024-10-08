# dicionario
produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

for chave in produto.keys():  # percorre a chave
    print(chave)

for valor in produto.values():  # percorre o valor
    print(valor)

for chave, valor in produto.items():  # percorre a chave e valor juntos
    print(chave, '=', valor)

# consigo ultilizar chave e valor mesmo depois do lasso retornando
# o ultimo valor, eles estão visiveis fora do lasso tbm
print(chave, valor)
