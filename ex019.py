nome = str(input('digite o seu nome completo:')).strip().title().split()
cores = {'limpa':'\033[m', 'roxo':'\033[35m', 'cinza':'\033[37m'}
print('O seu primeiro nome é:{}{}{} '.format(cores ['roxo'],nome[0], cores['limpa']))
print('O seu último nome é:{}{}{} '.format(cores ['cinza'],nome[len(nome)-1], cores ['limpa']))
