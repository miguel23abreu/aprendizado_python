vc = float(input('Qual o valor da casa que você pretende comprar? R$'))
sc = float(input('Qual o seu salário mensal? R$'))
qa = int(input('Em quantos anos você pretende pagar o ímovel? '))
qam = qa * 12
print('Para pagar a casa em {} anos será necessário '
     'fazer o pagamento mensal de R${:.2f} por {} meses'.format(qa,vc/qam,qam))
if (vc/qam) > (sc*30/100):
    print('Desculpe mas não vamos poder fazer o empréstimo pelo motivo do seu salário de R${} não ser suficiente'.format(sc))
else:
    print('Ok, o banco lhe fará o empréstimo!')
