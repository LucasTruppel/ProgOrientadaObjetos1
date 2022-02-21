from collections import Counter

ordem = int(input())
matriz = [None] * ordem
for i in range(0, ordem):
    matriz[i] = [int(k) for k in input().split()]
linhas = []
colunas = []

for i in range(0, ordem):
    soma = 0
    for j in range(0, ordem):
        soma += matriz[i][j]
    linhas.append(soma)

for j in range(0, ordem):
    soma = 0
    for i in range(0, ordem):
        soma += matriz[i][j]
    colunas.append(soma)

quantidade = Counter(linhas).most_common(2)
soma_certa = quantidade[0][0]
soma_errada = quantidade[1][0]
linha_errada = linhas.index(soma_errada)
coluna_errada = colunas.index(soma_errada)
numero_errado = matriz[linha_errada][coluna_errada]
numero_certo = soma_certa + numero_errado - soma_errada

print(numero_certo, numero_errado)
