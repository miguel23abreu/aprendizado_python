h = m = pm = p = 0
while True:
    p += 1
    print('-'*20)
    id = int(input(f'{p}° idade: '))
    s = ' '
    while not s in 'mMfF':
        s = str(input(f'{p}° sexo [M/F]: ')).upper().strip()[0]
    print('-'*20)
    if id >= 18:
        pm += 1
    if s == 'M':
        h += 1
    if s == 'F' and id < 20:
        m += 1
    son = ' '
    while not son in 'sSnN':
        son = str(input('deseja continuar [S/N]? ')).upper().strip()[0]
    if son in 'nN':
        break
    else:
            print('continuando...')
print(f'- {pm} pessoas são maiores de 18 anos;')
print(f'- {h} Homens foram cadastrados;')
print(f'- {m} mulheres tem menos de 20 anos;')