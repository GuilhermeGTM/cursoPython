# String
palavra = 'paralepipito'
for letra in palavra:
    # oq está dentro do end vai faze ação na palavra no caso \n vai pular linha
    print(letra, end=',')
print('Fim')  # para não ficar na mesma linha colocamos esse print


# lista
aprovados = ['Rafaela', 'Pedro', 'Renado', 'Maria']
for nome in aprovados:
    print(nome)
# para acessar o indice coloca-se enumerate
for posicao, nome in enumerate(aprovados):
    # +1 é para n sair do zero pq o indice sai 0-1-2-3-4
    print(f'{posicao + 1})', nome)


# tupla
dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sabado')
for dia in dias_semana:
    print(f'Hoje é {dia}')


# set ou conjunto
for letra in set('muito legal'):  # não garante a ordem
    print(letra)
# set literal
for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
