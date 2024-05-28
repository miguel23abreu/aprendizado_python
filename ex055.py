print(10*'-', 'sequência de fibbonaci', 10 * '-')
n = int(input('digite o número de termos: '))
pt = 0
st = 1
tt = pt + st
termo = 0
#print(' {} >'.format(pt), end='')
#sleep(1)
#print(' {} >'.format(st), end='')
#sleep(1)
while termo < n:
    if termo != n:
        termo += 1
        print('{} >'.format(pt), end='')
    if termo != n:
        termo += 1
        print(' {} >'.format(st), end='')
    if termo != n:
        termo += 1
        print(' {} > '.format(tt), end='')
    pt = st + tt
    st = pt + tt
    tt = -1     #faz com que o valor 1 da variavel st seja anulado
    tt = st + pt
print(' Fim')



