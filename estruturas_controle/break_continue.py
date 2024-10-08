for x in range(1, 11):
    if x % 2 == 0:  # verefica se o x é = 0 se for par
        continue  # continue interronpe a iteração e vai para proxima
    print(x)


for x in range(1, 11):
    if x == 5:  # se o x é 5 ele freia ele para
        break  # fecha o lasso, mas continua a programa
    print(x)

print('fim')
