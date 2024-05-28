a = float(input('Qual a sua altura?m '))
p = float(input('Qual o seu peso?kg '))
imc = p / (a**2)
if imc < 18.5:
    print('O seu imc é de {:.1f} e você está abaixo do peso!'.format(imc))
elif imc < 25:
    print('O seu imc é de {:.1f} e você está no peso ideal!'.format(imc))
elif imc < 30:
    print('O seu imc é de {:.1f} e você está com sobrepeso'.format(imc))
elif imc < 40:
    print('O seu imc é de {:.1f} e você está obeso'.format(imc))
elif imc > 40:
    print('O seu imc é de {:.1f} e você está com obesidade mòrbida'.format(imc))