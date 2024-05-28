linha = []
coluna = n = co = 0
num = list()
for c in range(0, 3):
    num.append(int(input(f'digite o valor [{coluna}, {n}]: ')))
    n += 1
    num.append(int(input(f'digite o valor [{coluna}, {n}]: ')))
    n += 1
    num.append(int(input(f'digite o valor [{coluna}, {n}]: ')))
    n += 1
    linha.append(num[:])
    num.clear()
    coluna += 1
    n -= n
for num in linha[0]:
    print(f'[{num:^4}]', end=' ')
print()
for num in linha[1]:
    print(f'[{num:^4}]', end=' ')
print()
for num in linha[2]:
    print(f'[{num:^4}]', end=' ')