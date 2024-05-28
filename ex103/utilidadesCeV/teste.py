from ex103.utilidadesCeV import moeda
from ex103.utilidadesCeV import dado
n = dado.leiadinheiro('Digite o valor: R$')
print(moeda.resumo(n, 13, 17))
