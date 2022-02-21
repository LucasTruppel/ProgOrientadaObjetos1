entrada = input().split()
dias, saldo = [int(i) for i in entrada]
movimentacao = int(input())
saldo = saldo + movimentacao
menor_saldo = saldo
for dia in range(2, dias + 1):
    movimentacao = int(input())
    saldo = saldo + movimentacao
    if saldo < menor_saldo:
        menor_saldo = saldo
print(menor_saldo)
