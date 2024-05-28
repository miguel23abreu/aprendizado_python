num = (int(input('digite um número: ')),
       int(input('digite outro número: ')),
       int(input('digite mais um número: ')),
       int(input('digite o último número: ')))
print(f'Os números digitados foram {num}')
print(f'O número 9 apareceu {num.count(9)}')
if 3 in num:
    print(f'A posição do primeiro número trés foi {num.index(3)+1}°')
else:
    print('O número trés não foi digitado')
print(f'Os número pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')