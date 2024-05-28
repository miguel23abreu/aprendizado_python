print('-'*20)
print('PAR OU ÍMPAR!')
print('-'*20)
v = 0
from random import randint
while True:
    jog = int(input('digite o seu número [1 a 10]: '))
    print('-'*20)
    comp = randint(0, 10)
    poi = ' '
    while poi not in 'PI':
        poi = str(input('PAR OU ÍMPAR? [P/I] ')).upper().strip()[0]
    if poi == 'P':
        print(f'você escolheu par e o seu número foi {jog}'
              f' e o computador escolheu ímpar, que foi {comp}')
        print('-' * 20)
        print(f'e o resultado foi {jog + comp}')
        print('-' * 20)
        if (jog + comp) % 2 == 0:
            print('deu par!')
            print('você ganhou!')
            v += 1
            print('-' * 20)
            print('vamos continuar...')
            print('-' * 20)
        else:
            print('deu ímpar!')
            print('você perdeu!')
            print('-' * 20)
            break
    if poi == 'I':
        print(f'você escolheu ímpar, e o seu número foi {jog}'
              f' e o computador escolheu par, que foi {comp}')
        print('-'*20)
        print(f'e o resultado foi {jog + comp}')
        print('-'*20)
        if (jog + comp) % 2 == 0:
            print('deu par!')
            print('você perdeu!')
            print('-'*20)
            break
        else:
            print('deu ímpar!')
            print('você ganhou!')
            v += 1
            print('-' * 20)
            print('vamos continuar...')
            print('-' * 20)
    if jog > 10:
        print('\033[31mOPÇÃO INVÁLIDA\033[m')
        print('-' * 20)
if v > 0:
    print(f'GAME OVER!, MAS VOCE TEVE {v} VITÓRIAS CONSECUTIVAS!')
else:
    print('GAME OVER!')
