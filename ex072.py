num = []
for c in range(0, 5):
    n = int(input('digite o seu número: '))
    if c == 0 or n > num[-1]:
        num.append(n)
        print(f'O número escolhido foi colocado na última posição')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'O número escolhido foi colocado na posição {num.index(n)}')
                break
            pos += 1
    c += 1
print('='*35)
print(f'Os valores da lista são: {num}')
