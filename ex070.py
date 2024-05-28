mmnum = 0
mnum = 0
pos1 = 0
pos2 = 0
pos = 0
num = list()
#for n in num:
#    print(n, end=' ')
for n in range(0, 5):
    num.append(int(input(f'digite o número na posição {pos}°: ')))
    pos += 1
print(f'Os valores da lista são: ', end='')
for pos,n in enumerate(num):
    print(n, end=' ')
    if pos == 0:
        mmnum = n
        mnum = n
        pos1 = pos
        pos2 = pos
    else:
        if mmnum < n:
            mmnum = n
            pos1 = pos
        if mnum > n:
            mnum = n
            pos2 = pos
print(f'\nO maior valor da lista é {mmnum} nas posiçõoes: ', end='')
for ns, v in enumerate(num):
    if v == mmnum:
        print(f'{ns}...', end=' ')
print(f'\nO menor valor da lista foi {mnum} nas posições ', end='')
for ns,v in enumerate(num):
    if v == mnum:
        print(f'{ns}...', end=' ')


