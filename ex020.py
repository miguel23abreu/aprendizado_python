from random import randint
from time import sleep
print(5*'=', 'VOU PENSAR EM UM NÚMERO ENTRE 0 E 5, TENTE ADVINHAR!', 5*'=')
n = randint(0, 5) #Faz o computador "pensar"
ne = (int(input('qual número você escolhe?'))) #Momento em que o jogador escolhe um número
print('\033[0;37mPROCESSANDO...\033[m')
sleep(2)
if n == ne:
    print('\033[32mparábens você venceu')
elif ne > 5:
    print('ops!esse número é invalido, tente novamente com um número que seja entre 0 e 5')

else:
    print('você perdeu!eu pensei no número {} e você escolheu o {} '.format(n, ne))
print('='*5, 'FIM DE JOGO', '='*5)