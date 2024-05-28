from time import sleep
n1 = int(input('qual o 1° número: '))
n2 = int(input('qual o 2° número: '))
soma = n1 + n2
multi = n1 * n2
op = 0
while op != 5:
    print(40 *'=')
    print('''    [ 1 ] soma
    [ 2 ] multiplicação
    [ 3 ] maior 
    [ 4 ] novos números
    [ 5 ] parar programa''')
    op = int(input('Qual a sua opção? '))
    print(40 * '=')
    if op == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif op == 2:
            print('A multiplicação entre {} e {} é {}'.format(n1, n2, multi))
    elif op == 3:
        if n1 > n2:
                print('o valor de {} é maior'.format(n1))
        elif n2 > n1:
                print('o valor de {} é maior'.format(n2))
        else:
                print('ambos os valores são iguais')
    elif op == 4:
            n1 = int(input('Qual o 1° número: '))
            n2 = int(input('Qual o 2° número: '))
    elif op > 5:
            print('opção inválida!')

print('fechando programa', end='')
sleep(0.7)
print('.', end='')
sleep(0.7)
print('.', end='')
sleep(0.7)
print('.')
sleep(0.5)
