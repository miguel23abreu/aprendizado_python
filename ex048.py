hmnome = ''
hmv = 0
mn20 = 0
midade = 0
for p in range(1, 5):
    print(10*'-', '{}° pessoa'.format(p), 10*'-')
    nome = str(input('NOME:')).strip()
    idade = int(input('IDADE:'))
    sexo = str(input('SEXO [M/F]:')).upper().strip()
    if sexo == 'F' and idade < 20:
        mn20 += 1
    midade += idade
    if sexo == 'M' and p == 1:
        hmv = idade
        hmnome = nome
    if sexo == 'M' and idade > hmv:
        hmv = idade
        hmnome = nome
print('\033[31mA média da idade das pessoas é de {}'.format(midade/4))
print('\033[33mA quantidade de mulheres que tem tem menos de 20 anos é de {}'.format(mn20))
print('\033[mO homem mais velho se chama {} e ele tem {} anos'.format(hmnome,hmv))
