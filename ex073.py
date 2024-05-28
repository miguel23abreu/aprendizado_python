lista = []
c = 0
while True:
    c += 1
    n = int(input(f'digite o {c}° valor: '))
    lista.append(n)
    son = ' '
    while not son in 'sSnN':
        son = str(input('deseja continuar? [S/N]')).strip().upper()[0]
    if son in 'N':
        break
print(f'Foram digitados {len(lista)} números na lista')
lista.sort(reverse=True)
print(f'A lista na ordem decrescente fica assim > {lista}')
if 5 in lista:
    print(f'O número 5(CINCO) está na lista')
else:
    print(f'O número 5(CINCO) não foi digitado')

