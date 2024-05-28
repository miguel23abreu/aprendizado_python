infoalunos = []
dado = list()
notalunos = 0
while True:
    dado.append(str(input('Nome do aluno: ')))
    dado.append(float(input('Nota 1: ')))
    dado.append(float(input('Nota 2: ')))
    dado.append((dado[1] + dado[2])/2)
    infoalunos.append(dado[:])
    dado.clear()
    son = ' '
    while not son in 'sSnN':
        son = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if son in 'nN':
        break
print(infoalunos[0])
print(f'{"No.":<6}NOME{"MÉDIA":>11}')
print('-'*22)
for pos, dado in enumerate(infoalunos):
    print(pos, end=' ')
    print(f'{dado[0]:^10}', end=' ')
    print(f'{dado[3]:>7.1f}', end=' ')
    print()
while True:
    print('-'*35)
    notalunos = int(input('De qual aluno você quer ver a nota? [999 interromper] '))
    print('-'*35)
    if notalunos == 999:
        print('FINALIZANDO...')
        break
    if notalunos <= len(infoalunos) - 1:
        print(f'As notas do aluno {infoalunos[notalunos][0]} são de {infoalunos[notalunos][1]} e {infoalunos[notalunos][2]}')
    print('VOLTE SEMPRE!')