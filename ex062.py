tg = pb = pm = c = 0
npb = ''
print('LOJAS AMERICANAS')
while True:
    c += 1
    print('-'*30)
    p = str(input(f'qual o nome do {c}° produto? ')).strip()
    pp = float(input('qual o preço? R$'))
    print('-'*30)
    tg += pp
    if pp >= 1000:
        pm += 1
    if c == 1:
        pb = pp
        npb = p
    else:
        if pb > pp:
            pb = pp
            npb = p
    son = ' '
    while not son in 'nNsS':
        son = str(input('tem mais produtos? [S/N]')).upper().strip()[0]
    if son == 'N':
        break
print(f'O total da sua compra deu R${tg:.2f}')
print(f'{pm} produtos custam mais de R$1000,00')
print(f'O produto mais barato foi um(a) {npb} que custa R${pb:.2f}')
print('{:-^40}'.format(' FIM DO PROGRAMA! '))



