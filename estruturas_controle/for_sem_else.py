# pelo PEP8 uma constante é com letras MAISCULAS
PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'politica')  # tupla
# lista
textos = [
    'João gosta de futebol e politica',
    'A praia foi divertida',
]

for texto in textos:
    found = False  # se nenhuma palavra for encontrada é falso
    # lower deixa tudo minusculo, split pega os espaços em branco
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida:', palavra)
            found = True
            break

    if not found:
        print('Texto autorizado:', texto)
