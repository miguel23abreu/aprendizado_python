print('{:=^40}'.format('AMERICANAS'))
vp = float(input('O total das suas compras: R$'))
print('O total das suas compras é de R${}'.format(vp))
print('digite:'
      '\n[1] para pagamento a vista no dinheiro ou cheque'
      '\n[2] para pagamento a vista no cartão'
      '\n[3] para pagamento parcelado')
fp = int(input('Qual a sua forma de pagamento? '))
if fp == 1:
    print('Ok, você terá 10% de desconto e o seu produto saíra por R${:.2f} no total'.format(vp - (vp*10/100)))
elif fp == 2:
    print('Ok, você terá 5% de desconto e seu produto custará R${:.2f} no total'.format(vp - (vp*5/100)))
elif fp == 3:
    print('Certo, você pode parcelar em até 2x sem juros, acima disto você poderá parcela em até 12x'
          ' com juros')
    p = int(input('Em quantas vezes você deseja parcelar? '))
    if p <= 2:
        total = vp
        print('Ok, você pagará o produto em {}x sem juros e o total das parcela é de R${:.2f} no total'.format(p, vp / p))
    elif p > 2:
        total = vp + (vp*20/100)
        print('Ok, você pagará o produto em {}x com juros de 20% em cada parcela, o subtotal será de R${:.2f} por parcela'
              ''.format(p, (vp + (vp*20/100)) / p))
    print('O total será de R${:.2f} no final'.format(total))
else:
    print('''ERRO!
OPÇÃO INVÁLIDA DE PAGAMENTO!!''')