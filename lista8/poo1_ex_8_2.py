quantidade_matrizes = int(input())
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for instancia in range(1, quantidade_matrizes + 1):
    matriz = [None] * 9
    for i in range(0, 9):
        matriz[i] = [int(k) for k in input().split()]

    valido = 'SIM'

    for i in range(0, 9):
        linha = sorted(matriz[i])
        if linha != numeros:
            valido = 'NAO'

    for j in range(0, 9):
        coluna = []
        for i in range(0, 9):
            coluna.append(matriz[i][j])
        coluna.sort()
        if coluna != numeros:
            valido = 'NAO'

    posicoes = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
    for posicao in posicoes:
        quadrado = []
        for i in range(posicao[0], posicao[0] + 3):
            for j in range(posicao[1], posicao[1] + 3):
                quadrado.append(matriz[i][j])
        quadrado.sort()
        if quadrado != numeros:
            valido = 'NAO'

    print(f'Instancia {instancia}')
    print(valido)
    print()
