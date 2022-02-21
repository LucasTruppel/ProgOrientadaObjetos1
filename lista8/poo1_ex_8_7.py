while True:
    try:
        linhas, colunas = [int(k) for k in input().split()]
        matriz = [None] * linhas
        for i in range(0, linhas):
            matriz[i] = input().split()

        for i in range(0, linhas):
            for j in range(0, colunas):
                if matriz[i][j] == '1':
                    i_treinador, j_treinador = i, j
                elif matriz[i][j] == '2':
                    i_pokemon, j_pokemon = i, j

        tempo = abs(i_treinador - i_pokemon) + abs(j_treinador - j_pokemon)
        print(tempo)
    except EOFError:
        break
