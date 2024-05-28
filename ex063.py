print('='*45)
print('{:^45}'.format('BANCOS MORGAN'))
print('='*45)
nt50 = nt20 = nt10 = nt1 = 0
sac = int(input('quanto você deseja sacar? R$'))
d = sac
while True:
    if sac >= 1 and sac < 10:
        sac -= 1
        nt1 += 1
    elif sac >= 10 and sac < 20:
        sac -= 10
        nt10 += 1
    elif sac >= 20 and sac < 50:
        sac -= 20
        nt20 += 1
    elif sac >= 50:
        sac -= 50
        nt50 += 1
    if sac == 0:
        break
print('-'*45)
print(f'você escolheu sacar R${d},00')
print('-'*45)
if nt50 >= 1:
    print(f'serão sacadas {nt50} notas de R$50,00')
if nt20 >= 1:
    print(f'serão sacadas {nt20} notas de R$20,00')
if nt10 >= 1:
    print(f'serão sacadas {nt10} notas de R$10,00')
if nt1 >= 1:
    print(f'serão sacadas {nt1} notas de R$1,00')
print('-'*45)
print('tchau, até mais e tenha um bom dia!')