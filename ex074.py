lista = []
listap = []
listai = []
c = 0
while True:
    c += 1
    n = int(input(f'Digite o {c}° valor da lista: '))
    lista.append(n)
    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)
    son = ' '
    while not son in 'SsNn':
        son = str(input('deseja continuar? [S/N]')).strip().upper()[0]
    if son in 'nN':
        break
print(f'Os elementos da lista são: {lista}')
print(f'Os elementos da lista par são: {listap}')
print(f'Os elementos da lista ímpar são: {listai}')