from random import randint
print('JOGO DA ADVINHAÇÃO!')
print('O SEU OPONENTE SERÁ A IA, BOA SORTE!')
comp = randint(0, 10)
player = int(input('DIGITE O SEU NÚMERO: '))
tentativas = 1
while player != comp:
    if player != comp:
        player = int(input(
            'OPA! NÃO FOI ESSE NÚMERO QUE EU PENSEI, FOI O {} E VOCÊ ESCOLHEU {}, DIGITE NOVAMENTE: '.format(comp, player)))
        comp = randint(0, 10)
        tentativas += 1
if tentativas == 1:
    print('VOCÊ É ACERTOU DE PRIMEIRA! PARABÉNS! ')
else:
    print('''finalmente você acertou depois de {} tentativas!
o número que eu escolhi foi {} e você o mesmo'''.format(tentativas, comp))
