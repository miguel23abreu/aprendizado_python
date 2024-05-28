jogador = dict()
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for partidasi in range(0, partidas):
    gols.append(int(input(f'    quantos gols foram feitos na partida {partidasi}: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('=-' * 40)
print(jogador)
print('=-'*40)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('=-'*40)
print(f'O jogador {jogador["nome"]} jogos {partidas} partidas no total')
for pos, jogadas in enumerate (jogador['gols']):
    print(f'    > Na partida {pos}, fez {jogadas} gols')
print('=-'*40)
print(f'>> Totalizando {jogador["total"]} gols <<')
