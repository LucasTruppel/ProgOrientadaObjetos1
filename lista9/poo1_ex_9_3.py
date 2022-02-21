while True:
    linhas, colunas, coluna_inicial = [int(k) for k in input().split()]
    if linhas == colunas == coluna_inicial == 0:
        break
    matriz = [None] * linhas
    for i in range(0, linhas):
        matriz[i] = [int(k) for k in input().split()]

    explode = False
    posicao = coluna_inicial - 1
    for i in range(0, linhas):
        j_direita = colunas - 1
        for j in range(posicao, colunas - posicao):
            if matriz[i][j] != 0:
                j_direita = j
                break

        j_esquerda = 0
        for j in range(posicao, -1, -1):
            if matriz[i][j] != 0:
                j_esquerda = j
                break

        deslocamento = matriz[i][j_esquerda] - matriz[i][j_direita]
        posicao = posicao + deslocamento
        if matriz[i][posicao] != 0:
            explode = True
            break

    if explode:
        print(f'BOOM {i+1} {posicao+1}')
    else:
        print(f'OUT {posicao+1}')
