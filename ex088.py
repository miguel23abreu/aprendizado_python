def area(a, b):
    s = a * b
    print(f'O terreno tem {a}x{b}m², oq dá em aréa {s}m²')
def lin(msg):
    print('-'*30)
    print(msg)
    print('-'*30)


lin('   CONTROLE DE TERRENO')
l = int(input('Largura: (m)'))
c = int(input('Comprimento: (m)'))
area(l, c)
