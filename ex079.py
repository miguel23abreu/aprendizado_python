matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = stc = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite o valor na posição [{l}, {c}]:'))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
print('=-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^4}]', end=' ')
    stc += matriz[l][2]
    print()
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif mai < matriz[1][c]:
        mai = matriz[1][c]
print('=-'*30)
print(f'A soma dos valores da terceira coluna é de: {stc}')
print(f'A soma dos valores pares da matriz é de: {spar}')
print(f'O maior valor da segunda linha é: {mai}')
