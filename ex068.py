dados = ('PÃO DE FORMA', 5.50,
         'PASTEL DE FRANGO', 2.50,
         'PASTA DE DENTE', 3.50,
         'ARROZ 1KG', 4.01,
         'FEIJÃO 1KG', 5.48,
         'BISCOITO OREO', 2.50,
         'LASANHA 4Q', 14.89,
         'DESODORANTE', 6.00)
print('='*40)
print(f'{"TABELA DE PREÇOS":^40}')
print('='*40)
for pos in range(0, len(dados)):
    if pos % 2 == 0:
        print(f'{dados[pos]:.<40}', end='')
    if pos % 2 == 1:
        print(f'R${dados[pos]:>7.2f}')
print('='*40)