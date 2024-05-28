def linha():
    print('-'*35)


import moeda

m = float(input('digite um valor: R$'))
print(f'-O valor escolhido foi R${m:.2f}')
dobro = moeda.dobro(m)
metade = moeda.metade(m)
print(f'-O valor dobrado é R${dobro:.2f}')
print(f'-O valor na metade é R${metade:.2f}')
linha()
taxa_au = float(input('Qual a taxa para aumentar? '))
aumentar = moeda.aumentar(m, taxa_au)
print(f'-O valor aumentado em {taxa_au}% fica R${aumentar:.2f}')
linha()
taxa_di = float(input('Quanto será o desconto? '))
diminuir = moeda.diminuir(m, taxa_di)
print(f'-O valor com desconto de {taxa_di}% fica R${diminuir:.2f}')