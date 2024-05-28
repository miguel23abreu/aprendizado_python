def ficha(nome=0, gols=0):
    gols = 0
    nome = str(input('Nome do jogador: ')).strip()
    if nome == '':
        nome = '<Desconhecido>'
    gols = str(input('Número de gols: '))
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'


print(ficha())