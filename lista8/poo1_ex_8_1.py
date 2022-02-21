matriz = [None] * 12
for i in range(0, 12):
    matriz[i] = [None] * 12

operacao = input()
for i in range(0, 12):
    for j in range(0, 12):
        matriz[i][j] = float(input())

soma = 0
for j in range(7, 12):
    for i in range(12 - j, j):
        soma += matriz[i][j]
media = soma / 30

if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{media:.1f}')
