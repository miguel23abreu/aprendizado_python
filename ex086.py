media = soma = 0
pessoas = list()
dados = dict()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = ' '
    while not 'mfMF' in dados['sexo']:
        dados['sexo'] = str(input('sexo: [F/M]')).strip().upper()[0]
        if dados['sexo'] not in 'mMfF':
            print('\033[31mDigito inválido!\033[m digite "F" ou "M"')
        if dados['sexo'] in 'mMfF':
            break
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    son = ' '
    while not son in 'sSnN':
        son = str(input('deseja continuar? [S/N] ')).strip().upper()[0]
        if not son in 'sSnN':
            print('\033[31mERRO! DIGITE NOVAMENTE\033[m')
    if son in 'Nn':
        break
media = soma / len(pessoas)
print(f'- No total foram cadastradas {len(pessoas)} pessoas')
print(f'- A media de idade é de {media:.1f}')
print(f'- As mulheres cadastradas foram: ', end=' ')
for m in pessoas:
    if m['sexo'] in 'F':
        print(m['nome'], end='')
print()
print(f'- As pessoas com idade acima da média são:')
for p in pessoas:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'- {k} = {v};', end=' ')
    print()
