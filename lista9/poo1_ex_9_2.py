while True:
    try:
        ordem = int(input())
        matriz = [None] * ordem
        for i in range(0, ordem):
            matriz[i] = ['0'] * ordem

        for i in range(0, ordem):
            for j in range(0, ordem):
                if ordem//3 <= i < ordem - ordem//3 and ordem//3 <= j < ordem - ordem//3:
                    matriz[i][j] = '1'
                elif i == j:
                    matriz[i][j] = '2'
                elif i + j == ordem - 1:
                    matriz[i][j] = '3'
        matriz[ordem//2][ordem//2] = '4'

        for i in range(0, ordem):
            linha = ''.join(matriz[i])
            print(linha)
        print()

    except EOFError:
        break
