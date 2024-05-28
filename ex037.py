from time import sleep
from random import choice
ppt = str(input('PEDRA,PAPEL OU TESOURA? '))
op = choice(['PEDRA','PAPEL','TESOURA'])
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('O JOGADOR ESCOLHEU {} E A MAQUÍNA ESCOLHE {}'.format(ppt,op) )
print('E O VENCEDOR É...')
sleep(2)
if ppt != 'PEDRA' or ppt != 'TESOURA' or ppt != 'PAPEL':
    print('OPS! NÃO FOI PÓSSIVEL JOGAR O JOGO PORQUE A OPÇÃO DO JOGADOR É INVÁLIDA')
elif ppt == op:
    print('EMPATE!')
elif ppt == 'TESOURA' and op == 'PAPEL' or ppt == 'PEDRA' and op == 'TESOURA' or ppt == 'PAPEL' and op == 'PEDRA':
    print('O JOGADOR!')
else:
    print('A MAQUÍNA!')