linhas, colunas = [int(k) for k in input().split()]
matriz = [None] * linhas
for i in range(0, linhas):
    matriz[i] = [int(k) for k in input().split()]

maior_quantidade = 0

for i in range(0, linhas):
    soma = 0
    for j in range(0, colunas):
        soma += matriz[i][j]
    if soma > maior_quantidade:
        maior_quantidade = soma

for j in range(0, colunas):
    soma = 0
    for i in range(0, linhas):
        soma += matriz[i][j]
    if soma > maior_quantidade:
        maior_quantidade = soma

print(maior_quantidade)
