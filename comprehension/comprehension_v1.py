# [expressão for item in list]
# i*2 é a expressão
# for i in range(10) é o laço

dobros = [i * 2 for i in range(10)]
print(dobros)


# versão "normal"
dobros = []
for i in range(10):
    dobros.append(i * 2)
print(dobros)
