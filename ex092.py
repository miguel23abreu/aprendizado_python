from random import randint
from time import sleep
def sorteia(num):
    while len(num) <= 4:
        n = randint(1,10)
        if n not in num:
            num.append(n)
    print(f'Sorteando os 5 valores: ')
    for nu in num:
        print(nu, end=' ')
        sleep(0.3)
    print('Pronto!')


def somapar(*n):
    sp = 0
    for num in n:
        print(f'somando os valores da lista {num} temos: ', end='')
        for nu in num:
            if nu % 2 == 0:
                sp += nu
    print(sp)


num = list()
sorteia(num)
somapar(num)