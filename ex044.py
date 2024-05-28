ac =0
n = int(input('digite um número? '))
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;31m', end=' ')
        ac += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} é divisível {} vezes'.format(n,ac))
if ac == 2:
    print('\033[mE por isso ele é considerado um número PRIMO')
else:
    print('\033[mE é por isso que ele não é PRIMO')
