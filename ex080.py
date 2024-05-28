from random import randint
from time import sleep
print('='*30)
print(F'{"JOGO DA MEGASENA":^30}')
print('='*30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
palpite = []
print(f'SORTEANDO OS SEUS JOGOS...')
print('-'*30)
sleep(0.5)
for c in range(0, jogos):
    while len(palpite) < 6:
        num = randint(1, 61)
        if not num in palpite:
            palpite.append(num)
    palpite.sort()
    print(f'jogo {c + 1} = {palpite}')
    palpite.clear()
    sleep(1)
print('-'*3)
print(f'{" BOA SORTE! ":=^30}')
