from time import sleep
from operator import itemgetter
from random import randint
pos = 1
jogadores = {'jogador1':randint(1,6), 'jogador2':randint(1,6), 'jogador3':randint(1,6), 'jogador4':randint(1,6)}
ranking = {}
print('=-'*35)
for k,v in jogadores.items():
    print(f'O dado do {k} deu {v}')
    sleep(1)
print('=-'*35)
print(f'{"== RANKING DOS JOGADORES ==":^4}')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True )
for pos, v in enumerate(ranking):
    print(f'{pos+1}° lugar = {v[0]} com {v[1]}')
    sleep(1)