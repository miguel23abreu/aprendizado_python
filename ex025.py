n1 = float(input('digite o primeiro número: ' ))
n2 = float(input('digite o segundo número: '))
n3 = float(input('digite o terceiro número: '))
#man = n1 > n2 and n3 or n2 > n1 and n3 or n3 > n1 and n2
#men = n1 < n2 and n3 or n2 < n1 and n3 or n3 < n1 and n2

# DECIDINDO MAIOR NÚMERO
if n1 > n2 and n1 > n3:
    maior = n1
   #print('O maior número dos trés é {}'.format(n1))
if n2 > n1 and n2 > n3:
    maior = n2
    #print('O maior número dos trés é {}'.format(n2))
if n3 > n1 and n3 > n2:
    maior = n3
    #print('O maior número dos trés é {}'.format(n3))

# VERIFICANDO O MENOR NÚMERO
if n1 < n2 and n1 < n3:
    menor = n1
    #print('{} é o menor dos trés números'.format(n1))
if n2 < n1 and n2 < n3:
    menor = n2
    #print('{} é o menor dos trés números'.format(n2))
if n3 < n1 and n3 < n2:
    menor = n3
cores = {'limpa':'\033[m', 'vermelho':'\033[31m', 'azul':'\033[34m', 'roxo':'\033[35m'}
print('{}{}{} é o menor dos trés números'.format(cores ['vermelho'], menor, cores['limpa']))
print('{}{}{} é o maior dos trés números'.format(cores ['vermelho'], maior, cores['limpa']))





