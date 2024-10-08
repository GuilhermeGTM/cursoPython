# [expressão for item in list if condicional]
# expressão é i * 2
# item in list é for i in range(10)
# if condicional é if i % 2 == 0
dobros_dos_pares = [i * 2 for i in range(10) if i % 2 == 0]
print(dobros_dos_pares)


# versão "normal"
dobros_dos_pares = []
for i in range(10):
    if i % 2 == 0:
        dobros_dos_pares.append(i * 2)
print(dobros_dos_pares)
