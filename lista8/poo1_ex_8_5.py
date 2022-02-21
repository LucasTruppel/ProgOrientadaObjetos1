entrada = input().split()
largura_salao, comprimento_salao = [int(i) for i in entrada]
entrada = input().split()
i_inicial, j_inicial = [int(i) - 1 for i in entrada]

matriz = [None] * largura_salao
for i in range(0, largura_salao):
    matriz[i] = input().split()

i, j = i_inicial, j_inicial

while True:
    matriz[i][j] = '2'
    i_cima, i_baixo, i_direita, i_esquerda = i - 1, i + 1, i, i
    j_cima, j_baixo, j_direita, j_esquerda = j, j, j + 1, j - 1
    if i_cima >= 0 and matriz[i_cima][j_cima] == '1':
        i = i_cima
        j = j_cima
    elif i_baixo < largura_salao and matriz[i_baixo][j_baixo] == '1':
        i = i_baixo
        j = j_baixo
    elif j_direita < comprimento_salao and matriz[i_direita][j_direita] == '1':
        i = i_direita
        j = j_direita
    elif j_esquerda >= 0 and matriz[i_esquerda][j_esquerda] == '1':
        i = i_esquerda
        j = j_esquerda
    else:
        break

print(i + 1, j + 1)
