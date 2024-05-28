#N = int(input('digite um número:'))
#NA = N - 1
#NS = N + 1
#print('o número escolhido foi {} e seu antecessor é {} e o seu sucessor é {}'.format(N,(N-1),(N+1) ))

#N = int(input('digite um número:'))
#print('o numero escolhido foi {}.'
#      '\n o seu dobro é {}.'
#      '\n o seu triplo é {}.'
#      '\n e sua raiz quadrada é {:.3f}'
#      .format(N, (N*2),(N*3),pow(N, (1/2))))

#n1 = float(input('digite a primeira nota:'))
#n2 = float(input('digite a segunda nota:'))
#m = (n1 +n2) / 2
#print('a primeira nota é {:.1f} a segunda é {:.1f} e a na média fica {:.1f}'.format(n1,n2,m))

#m = int(input('digite um valor para ser medido em m:'))
#km = m / 1000
#hm = m / 100
#dam = m / 10
#dm = m * 10
#cm = m * 100
#mm = m * 1000
#print('o valor em m é {}m'
#      '\nem km é {}km'
#      '\nem hm é {}hm'
#      '\nem dam é {}dam'
#      '\nem dm é {}dm'
#      '\nem cm é {}cm'
#      '\ne em mm é {}mm'.format(m,km,hm,dam,dm,cm,mm))

#n = int(input('digite um numero para formar a sua taboada: '))
#print('-' * 14)
#print('{} x {:2} = {}'
#      '\n{} x {:2} = {}'
#      '\n{} x {:2} = {}'
#      '\n{} x {:2} = {}'
#      '\n{} x {:2} = {}'
#      '\n{} x {:2} = {}'
#      '\n{} x {:2} = {}'
#      '\n{} x {:2} = {}'
#      '\n{} x {:2} = {}'
#      '\n{} x {} = {}'.format(n,1,n*1,n,2,n*2,n,3,n*3,n,4,n*4,n,5,n*5,n,6,n*6,n,7,n*7,n,8,n*8,n,9,n*9,n,10,n*10))
#print('-' * 14)

#d = float(input('digite quanto de dinheiro tem na sua carteira:'))
#dd = d / 5.24
#de = d / 6.37
#dl = d / 7.32
#print('o dinheiro convertido de real para dólar é US${:.2f}'
#      '\npra euro fica £{:.2f}'
#      '\ne para libra é €{:.2f}'.format(dd,de,dl))

#a = float(input('digite a medida da altura:'))
#l = float(input('digite a medida da largura:'))
#ar = a * l
#tn = (1/2) * ar
#print('a medida da altura é {:.2f}m e da largura é {:.2f}m '
#      '\nsendo a area de {:.2f}m² e a quantidade nécessaria para pintar toda a parede é de {:.2f}l'.format(a,l,ar,tn))

#pd = float(input('digite o preço do produto: R$'))
#print('o preço do produto é de R${} e com 5% de desconto ele fica por R${}'.format(pd,pd - (pd*5/100)))

#sa = float(input('digite o sálario do fúncionario: R$'))
#saa = sa + (sa*15/100)
#print('o sálario do fúncionario é de R${:.2f} e com acréscimo fica R${:.2f}'.format(sa,saa))

#produto = float(input('digite o preço do produto: R$'))
#produtocd = produto - (produto * 10/100)
#print('o produto a vista fica R${} e a prazo fica R${} parcelado em até 12x sem juros'.format(produtocd, produto))

print('CALCÚLO DE PA!')
p = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))
mais = 10
tf = 0
total = 0
while mais != 0:
    total = total + mais
    while tf < total:
        tf += 1
        print('{} '.format(p), end='')
        if tf < total:
            print(' >> ', end='')
        p += r
    print('pausa')
    mais = int(input('quantos termos você desaja colocar a mais? '))
print('fim')