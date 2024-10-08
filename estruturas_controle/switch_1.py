# simulando o switch
# def get_dia_semana(dia):  # Função
# dicionario
#    dias = {
#        1: 'Domingo',
#        2: 'Segunda',
#        3: 'Terça',
#        4: 'Quarta',
#        5: 'Quinta',
#        6: 'Sexta',
#        7: 'Sabado',
#    }
#    # parametro dia é a chave 1,2... segundo parameto é o default
#    return dias.get(dia, '**invalido**')


# if __name__ == '__main__':
#    for dia in range(0, 9):
#        print(f'{dia}: {get_dia_semana(dia)}')

def get_dia_semana(dia):
    match dia:
        case 1:
            return 'Domingo'
        case 2:
            return 'Segunda'
        case 3:
            return 'Terça'
        case 4:
            return 'Quarta'
        case 5:
            return 'Quinta'
        case 6:
            return 'Sexta'
        case 7:
            return 'Sabado'
        case _:
            return '** inválido **'


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_dia_semana(dia)}')
