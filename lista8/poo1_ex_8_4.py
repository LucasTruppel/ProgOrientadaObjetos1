quantidade_testes = int(input())
for teste in range(1, quantidade_testes + 1):
    linhas, colunas, i_soco, j_soco = [int(k) for k in input().split()]
    matriz = [None] * linhas
    for i in range(0, linhas):
        matriz[i] = [int(k) + 1 for k in input().split()]

    i_soco, j_soco = i_soco - 1, j_soco - 1

    for i in range(0, linhas):
        for j in range(0, colunas):
            dano = 9 - max(abs(i_soco - i), abs(j_soco - j))
            if dano > 0:
                matriz[i][j] += dano

    print(f'Parede {teste}:')
    for i in range(0, linhas):
        linha = str(matriz[i][0])
        for j in range(1, colunas):
            linha = linha + ' ' + str(matriz[i][j])
        print(linha)
