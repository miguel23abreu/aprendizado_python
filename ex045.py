nof = str(input('digite um nome ou frase: ')).strip().upper()
nofs = nof.split()
nofsj = ''.join(nofs)
nofsji = nofsj[::-1]
#nofsji = ''
print('A frase que você digitou é: {}'.format(nofsj))
#for letra in range(len(nofsj) - 1, -1, -1):
#    nofsji = nofsji + nofsj[letra]
#print(nofsji)
print('E o seu inverso é {}'.format(nofsji))
if nofsj == nofsji:
    print('E esta frase é um palíndromo')
else:
    print('E esta frase não é um palíndromo')

