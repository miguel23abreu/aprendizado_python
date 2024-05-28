listag = [[], []]
for n in range(0, 7):
    n += 1
    num = int(input(f'digite o {n}° valor: '))
    if num % 2 == 0:
        listag[0].append(num)
    else:
        listag[1].append(num)
print('=-'*35)
listag[0].sort()
listag[1].sort()
print(f'Os valores pares digitador foram: {listag[0]}')
print(f'Os valores ímpar digitados foram: {listag[1]}')