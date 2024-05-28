from time import sleep
carro = float(input('qual a velocidade que estava o carro? '))
if carro > 80:
    print('EI VOCÊ!PARE AGORA O SEU VEÍCULO!')
    sleep(1)
    print('VOCÊ ULTRAPASSOU O LIMITE DE \033[36mVELOCIDADE\033[m QUE FOI DE \033[35m{}km/h\033[m E TERÁ UMA MULTA DE \033[34mR${:.2f}\033[m!'.format(carro,(carro-80)*7))
    sleep(1)
    print('CERTO, AGORA VÁ E DIRIJA COM CUIDAD0!!')
else:
    print('...')