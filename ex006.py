c = float(input('qual a temperatura em celsius?'))
#f = c * 1.8 + 32
#obs:é possível utilizar esta fórmula acima
f = c * 9 / 5 + 32
print('a temperatura em celsius é {}°c e em fahrenheit fica {:.1f}°f'.format(c, f))