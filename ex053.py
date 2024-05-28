print(20*'=', 'PROGRESSÃO ARITMÉTICA', 20*'=')
p = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))
dt = 0
while dt < 10:
    dt += 1
    #if p == p:
    print('{} '.format(p), end='')
    if dt != 10:
        print('>> ', end='')
    p = p + r