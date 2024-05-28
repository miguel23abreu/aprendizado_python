from random import randint
mmn = 0
mn = 0
c = 0
nt = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram: ', end='')
for n in nt:
    print(f' {n} ', end='')
print(f'\nO maior número da tupla é {max(nt)}')
print(f'O menor número da tupla é {min(nt)}')

