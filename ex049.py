sexo = str(input('qual o seu sexo? [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('\033[31mSEXO INVÁLIDO! DIGITE NOVAMENTE! '))
print('sexo {} registrado com sucesso!'.format(sexo))