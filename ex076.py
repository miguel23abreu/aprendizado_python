pessoas = []
dados = []
p = 0
mmpeso = mpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mmpeso = dados[1]
        mpeso = dados[1]
    else:
        if mmpeso < dados[1]:
            mmpeso = dados[1]
        if mpeso > dados[1]:
            mpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    p += 1
    son = ' '
    while not son in 'SsNn':
            son = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if son == 'N':
        break
print(f'O número de pessoas cadastradas foi de {len(pessoas)}')
print(f'As pessoas com os maiores pesos de {mmpeso} são: ', end='')
for peso in pessoas:
    if peso[1] == mmpeso:
        print(f'{peso[0]}', end=' ')
print(f'\nAs pessoas com os menores pesos de {mpeso} são: ', end='')
for peso in pessoas:
    if peso[1] == mpeso:
        print(f'{peso[0]}', end=' ')


