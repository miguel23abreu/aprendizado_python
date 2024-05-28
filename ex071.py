ln = []
while True:
    n = int(input('digite um valor: '))
    if not n in ln:
        ln.append(n)
    else:
        print('\033[31mEsse número já está na lista, não será adicionado\033[m')
    son = ' '
    while not son in 'sSnN':
        son = str(input('deseja continuar? [S/N]')).strip().upper()[0]
    if son == 'N':
        print('programa encerrado')
        break
    if son == 'S':
        print('continuando...')
ln.sort()
print(f'Os números escolhidos foram: {ln}')