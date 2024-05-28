from datetime import datetime
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('ano de nascimento: '))
pessoa['sexo'] = str(input('sexo[M/F]: ')).upper().strip()[0]
pessoa['idade'] = datetime.now().year - nasc
pessoa['ctps'] = int(input('carteira de trabalho (0 não tem): '))
if pessoa['ctps'] > 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    if pessoa['sexo'] in 'mM':
        pessoa['aposentadoria'] = pessoa['idade'] + (pessoa['contratação'] + 35) - datetime.now().year
    if pessoa['sexo'] in 'fF':
        pessoa['aposentadoria'] = pessoa['idade'] + (pessoa['contratação'] + 30) - datetime.now().year
print('='*35)
for k, v in pessoa.items():
    print(f' - {k} tem valor {v}')
