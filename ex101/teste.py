from ex101 import moeda

moe = float(input('digite o valor da moeda: R$'))
print(f'- A metade de {moeda.moeda(moe)} é {moeda.metade(moe, form=True)}')
taxa = int(input('qual será o valor da taxa? '))
print(f'- O aumento de {taxa}% sobre o valor de {moeda.moeda(moe)} é de {moeda.aumentar(moe, taxa, form=True)}')
print(f'- O desconto de 25% sobre o valor de {moeda.moeda(moe)} é de {moeda.diminuir(moe,25, form=True)}')