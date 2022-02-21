while True:
    try:
        linhas, colunas = [int(i) for i in input().split()]
        matriz = [None] * linhas
        for i in range(0, linhas):
            matriz[i] = input().split()

        encontrou = False
        for i in range(0, linhas):
            for j in range(0, colunas):
                if matriz[i][j] == 'X':
                    encontrou = True
                    break
            if encontrou:
                break

        comando = ''
        direcao = 'B'
        while True:
            matriz[i][j] = '2'
            i_cima, i_baixo, i_direita, i_esquerda = i - 1, i + 1, i, i
            j_cima, j_baixo, j_direita, j_esquerda = j, j, j + 1, j - 1
            if i_cima >= 0 and matriz[i_cima][j_cima] == '0':
                i = i_cima
                j = j_cima
                if direcao == 'R':
                    comando += 'L '
                elif direcao == 'L':
                    comando += 'R '
                comando += 'F '
                direcao = 'C'
            elif i_baixo < linhas and matriz[i_baixo][j_baixo] == '0':
                i = i_baixo
                j = j_baixo
                if direcao == 'R':
                    comando += 'R '
                elif direcao == 'L':
                    comando += 'L '
                comando += 'F '
                direcao = 'B'
            elif j_direita < colunas and matriz[i_direita][j_direita] == '0':
                i = i_direita
                j = j_direita
                if direcao == 'C':
                    comando += 'R '
                elif direcao == 'B':
                    comando += 'L '
                comando += 'F '
                direcao = 'R'
            elif j_esquerda >= 0 and matriz[i_esquerda][j_esquerda] == '0':
                i = i_esquerda
                j = j_esquerda
                if direcao == 'C':
                    comando += 'L '
                elif direcao == 'B':
                    comando += 'R '
                comando += 'F '
                direcao = 'L'
            else:
                comando += 'E'
                break

        print(comando)

    except EOFError:
        break
