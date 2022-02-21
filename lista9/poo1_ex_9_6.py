quantidade_bolas = int(input())
matriz = [None] * quantidade_bolas
matriz[0] = input().split()
for i in range(1, quantidade_bolas):
    matriz[i] = [None] * (quantidade_bolas - i)

for i in range(1, quantidade_bolas):
    for j in range(0, quantidade_bolas - i):
        if matriz[i-1][j] == matriz[i-1][j+1]:
            matriz[i][j] = '1'
        else:
            matriz[i][j] = '-1'

if matriz[quantidade_bolas-1][0] == '-1':
    print('branca')
else:
    print('preta')
