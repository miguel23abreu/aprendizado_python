from time import sleep
def contador(i, f, p):
    if p == 0:
        p = 1
    if i < 0 and p < 0:
        p = p + (-p-p)
    if i > f and p > 0:
        p = p + (-p-p)
    print('='*30)
    print(f'Contando de {i} a {f} de {p} em {p}: ')
    if f <= 0:
        for c in range(i, f-1, p):
            print(c, end=' ')
            sleep(0.3)
    if f > 0:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.3)
    print('FIM!')


print('='*30)
print('Contando de 1 a 10: ')
sleep(1)
for c in range(1, 11):
    print(c, end=' ')
    sleep(0.3)
print('FIM!')
print('TEMPO!')
sleep(1)
print('='*30)
print('Contado de 10 a 0 de 2 em 2: ')
sleep(1)
for c in range(10, 0-1, -2):
    print(c, end=' ')
    sleep(0.3)
print('FIM!')
print('TEMPO!')
print('='*30)
sleep(1)
print('Agora é sua vez de decidir como vai ser a contagem !')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)