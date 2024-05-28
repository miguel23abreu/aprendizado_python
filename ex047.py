maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('digite o peso da {}° pessoa: '.format(pessoa)))
    if pessoa == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('A pessoa com o maior peso possui {}kg'.format(maior))
print('E a com o menor peso possui {}kg'.format(menor))