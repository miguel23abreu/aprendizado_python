print(10*'-=', 'PROGESSÃO ARITMÉTICA', 10*'-=')
p = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))
dt = 0
total = 0
dtm = 10
while dtm != 0:
    total = total + dtm
    while dt < total:
        dt += 1
        print('{} '.format(p), end='')
        if dt != total:
            print('>> ', end='')
        p += r
    print('\npausa')
    dtm = int(input('quantas vezes mais você deseja aumentar os termos? '))
print('programa finalizado com tantos {} termos mostrados'.format(total))
print('fim')
