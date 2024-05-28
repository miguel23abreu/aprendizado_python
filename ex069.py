nomes = ('MIGUEL', 'POKEMON', 'PYTHON', 'CURSO', 'CORRA', 'HELICOPTERO',
         'CANHAO', 'MUNIÇAO', 'CHAINSAW')
for nomes in nomes:
    print(f'\nNa palavra {nomes} tem ', end='')
    for letra in nomes:
        if letra in 'AEIOU':
            print(letra, end=' ')
