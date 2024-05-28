n = c = s = 0
n = int(input('digite um número: [999] para parar '))
while n != 999:
    if n != 999:
        c += 1
        s += n
        n = int(input('digite um número: [999] para parar '))
print('A quantidade de números digitadas foi {} e a soma delas é de {}'.format(c, s))