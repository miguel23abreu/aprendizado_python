def maior(*num):
    mai = cont = 0
    for valor in num:
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
    print('='*70)
    print(f'Analisando os valores: ')
    for valor in num:
        print(valor, end=' ')
    print(f'\nO maior valor é {mai}')
    print('='*70)



maior(1, 5, 8, 4, 2, 6)
maior(5,10,20,5,80,70,90,25)
maior(4,2,6,8,9,10,3)
maior()
