while True:
    try:
        linhas, colunas = [int(i) for i in input().split()]
        matriz = [None] * linhas
        for i in range(0, linhas):
            matriz[i] = input().split()

        for i in range(0, linhas):
            linha = ''
            for j in range(0, colunas):
                if matriz[i][j] == '1':
                    linha = linha + '9'
                else:
                    contador = 0
                    i_cima, i_baixo, i_direita, i_esquerda = i - 1, i + 1, i, i
                    j_cima, j_baixo, j_direita, j_esquerda = j, j, j + 1, j - 1

                    if i_cima >= 0 and matriz[i_cima][j_cima] == '1':
                        contador += 1
                    if i_baixo < linhas and matriz[i_baixo][j_baixo] == '1':
                        contador += 1
                    if j_direita < colunas and matriz[i_direita][j_direita] == '1':
                        contador += 1
                    if j_esquerda >= 0 and matriz[i_esquerda][j_esquerda] == '1':
                        contador += 1

                    linha = linha + str(contador)

            print(linha)

    except EOFError:
        break
