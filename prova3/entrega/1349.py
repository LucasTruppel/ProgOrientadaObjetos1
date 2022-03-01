# -*- coding: utf-8 -*-

while True:
    tamanho = int(input())  # Entrada da ordem das matrizes.
    if tamanho == 0:  # Encerra o código.
        break

    # Entrada da matriz da imagem padrão.
    matriz_padrao = [None] * tamanho
    for i in range(0, tamanho):
        matriz_padrao[i] = [int(k) for k in input().split()]

    # Entrada da matriz da imagem do scanner.
    matriz = [None] * tamanho
    for i in range(0, tamanho):
        matriz[i] = [int(k) for k in input().split()]

    # Nesse loop serão testados os 8 casos possíveis de matriz. Podemos rotacionar a matriz, gerando 4 casos.
    # Além disso, cada um desses casos pode ser revertido, totalizando 8 casos distintos.
    maior_pixels = 0
    for k in range(0, 4):

        # Rotaciona a matriz em 90 graus no sentido horário.
        if k != 0:  # Na primeira iteração não acontece, para testar a matriz original.
            # Criação da nova matriz.
            nova_matriz = [None] * tamanho
            for i in range(0, tamanho):
                nova_matriz[i] = [None] * tamanho

            # Recebe elementos da matriz anterior de modo a rotacioná-la.
            for i in range(0, tamanho):
                for j in range(0, tamanho):
                    nova_matriz[j][tamanho - 1 - i] = matriz[i][j]
            matriz = nova_matriz  # Matriz recebe a nova matriz.

        # Criação da matriz reversa, para também avaliar esse caso.
        matriz_reversa = []
        for i in range(0, tamanho):
            linha = matriz[i]
            copia_linha = linha.copy()
            copia_linha.reverse()
            matriz_reversa.append(copia_linha)

        # Conta a quantidade de pixels da matriz que estão de acordo com a matriz padrão.
        pixels = 0
        for i in range(0, tamanho):
            for j in range(0, tamanho):
                if abs(matriz[i][j] - matriz_padrao[i][j]) <= 100:
                    pixels += 1

        # Conta a quantidade de pixels da matriz reversa que estão de acordo com a matriz padrão.
        pixels_reversa = 0
        for i in range(0, tamanho):
            for j in range(0, tamanho):
                if abs(matriz_reversa[i][j] - matriz_padrao[i][j]) <= 100:
                    pixels_reversa += 1

        # Testa se as quantidades contadas de pixels na matriz e matriz reversa é maior que a maior armazenada.
        if pixels > maior_pixels:
            maior_pixels = pixels
        if pixels_reversa > maior_pixels:
            maior_pixels = pixels_reversa

    # Calcula a porcentagem de precisão e imprime na tela.
    precisao = maior_pixels / (tamanho * tamanho) * 100
    print(f'{precisao:.2f}')
