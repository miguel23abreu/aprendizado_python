print('='*40)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('='*40)
pr = int(input('DIGITE O PRIMEIRO TERMO: '))
r = int(input('DIGITE A RAZÃO: '))
d = pr + (10-1) * r
for c in range(pr, d + r, r):
    print('{} >> '.format(c), end='')
print('ACABOU')
