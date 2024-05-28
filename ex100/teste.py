from ex100 import moeda

moe = float(input('digite o valor da moeda: R$'))
print(f'- A metade de {moeda.moeda(moe)} é de {moeda.moeda(moeda.metade(moe))}')
taxa = int(input('qual será o valor da taxa? '))
print(f'- O aumento de {taxa}% sobre o valor de {moeda.moeda(moe)} é de {moeda.moeda(moeda.aumentar(moe, taxa))}')