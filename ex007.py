kp = float(input('quantos km você percorreu com este carro?'))
d = float(input('e quantos dias você ficou com este carro?'))
dp = d * 60
kmp = kp * 0.15
tp = dp + kmp
print('você terá de pagar R${:.2f} pelos dias com o carro e R${:.2f} pelos km rodados, dando no total R${:.2f}'
      .format(dp, kmp, tp))