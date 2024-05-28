jogadores = list()
jogador = dict()
gols = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    gols.clear()
    for partidasi in range(0, partidas):
        gols.append(int(input(f'    quantos gols foram feitos na partida {partidasi}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    son = ' '
    while not son in 'sSnN':
        son = str(input('deseja continuar? [S/N]')).strip().upper()[0]
    if son == 'N':
        break
print('=-'*40)
print(f'COD.', end=' ')
for i in jogador.keys():
    print(f'{i:<12}', end=' ')
print()
print('-'*40)
for pos, jogador in enumerate(jogadores):
    print(f'{pos:<4}', end=' ')
    for v in jogador.values():
        print(f'{str(v):<12}', end=' ')
    print()
while True:
    print('-'*40)
    dadosjogador = int(input('deseja ver os dados de qual jogador? [999 interromper]'))
    if dadosjogador == 999:
        print('FINALIZANDO...')
        break
    if dadosjogador <= len(jogadores) - 1:
        print('-'*40)
        print(f'===Dados das partidas do jogador {jogadores[dadosjogador]["nome"]}===')
        for p, j in enumerate(jogadores[dadosjogador]['gols']):
            print(f'    Na partida {p} fez {j} gols', end=' ')
            print()
        print(f'Totalizando {jogadores[dadosjogador]["total"]} gols')
    if dadosjogador > len(jogadores) - 1:
        print('\033[31mERRO!CÓDIGO INVÁLIDO! TENTE NOVAMENTE!\033[m')