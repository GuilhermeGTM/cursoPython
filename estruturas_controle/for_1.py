for i in range(1, 11):  # vai do 1 até 10
    print('i={}'.format(i))

for j in range(10):  # vai do 0 até 9
    print('j={}'.format(j))


# nesse caso o f dentro do print ele vai interpolar
# a string para depois fazer o calculo
for x in range(1, 11):
    for y in range(1, 11):
        print(f'{x} * {y} = {x * y}')
