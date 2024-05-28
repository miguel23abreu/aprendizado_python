from math import factorial
print(10*'=', 'CALCÚLO DE FATORIAL!', 10*'=')
n = int(input('digite um número: '))
print('{}! = '.format(n), end='')
ref = factorial(n)
c = n
aco = 1
while c > 0:
    print('{} '.format(c), end='')
    if c > 1:
        print('x ', end='')
    aco *= c
    c -= 1
print('= {}'.format(aco))
print('Agora usando "for"')
print('{}! = '.format(n), end='')
for c in range(n, 1 - 1, -1):
    print(c, end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
print('{}'.format(aco))

