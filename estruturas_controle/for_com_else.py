# pelo PEP8 uma constante é com letras MAISCULAS
PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'politica')  # tupla
# lista
textos = [
    'João gosta de futebol e politica',
    'A praia foi divertida',
]

for texto in textos:
    # lower deixa tudo minusculo, split pega os espaços em branco
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida:', palavra)
            break
    else:
        print('Texto autorizado:', texto)
