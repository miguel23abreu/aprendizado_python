frase = str(input('digite um frase : ')).upper().strip()
cores = {'limpa':'\033[m', 'cinza':'\033[37m', 'amarelo':'\033[33m', 'vermelho':'\033[31m'}
print('A letra "A" aparece {}{}{} vezes'.format(cores ['amarelo'],frase.count('A'), cores ['limpa']))
print('Ela aparece na primeira vez na posição {}{}{}'.format(cores ['cinza'],frase.find('A')+1, cores ['limpa']))
print('A ultima vez que a letra "A" aparece é na posição {}{}{}'.format(cores ['vermelho'],frase.rfind('A')+1,cores ['limpa']))
