d = float(input('qual será a distáncia da sua viagem em \033[1;33mkm\033[m? '))
#print('o custo será de R${:.2f}'.format(d*0.50) if d <= 200 else 'o custo da viagem será de R${:.2f}'.format(d*0.45))
de = d * 0.50 if d <= 200 else d * 0.45
#if d <= 200:
#    de = d * 0.50
    #print('O seu percuso será de {:.2f}km e o custo da sua viagem será de R${:.2f}'.format(d, (d*0.50)))
#else:
#    de = d * 0.45
    #print('O seu percuso será de {:.2f}km e o custo da sua viagem será de R${:.2f}'.format(d, (d*0.45)))
print ('A sua viagem de {:.2f}km custará R$\033[31m{:.2f}\033[m'.format(d, de))
print('Tenha uma boa viagem')
