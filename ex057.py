n = c = s = 0
maior = 0
menor = 0
son = 'S'
while son not in 'Nn':
    n = int(input('digite o {}° valor: '.format(c + 1)))
    c += 1
    s += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    son = str(input('deseja continuar? [S/N]')).upper()
    while son not in 'Ss' and son not in 'nN':
            print('\033[31mopção inválida, digite novamente!\033[m')
            son = str(input('deseja continuar? [S/N]')).upper()
m = s / c
print('A quantidade de valores digitados foi de {}, a soma entre elas foi {}, o maior foi {} e o menor {} e a média de tudo é {:.2f} '.format(c, s, maior, menor, m))



