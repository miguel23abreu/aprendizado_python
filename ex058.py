s = c = 0
while True:
    n = int(input('digite um número [999 para parar]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'foram digitados no total {c} números e a soma deles foi de {s}')