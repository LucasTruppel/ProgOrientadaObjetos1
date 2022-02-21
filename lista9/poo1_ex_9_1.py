while True:
    ordem = int(input())
    if ordem == 0:
        break
    elif ordem == 1:
        print('1')
        print()
    else:
        matriz = [None] * ordem
        for i in range(0, ordem):
            matriz[i] = [0] * ordem

        for i in range(0, ordem):
            for j in range(0, ordem):
                matriz[i][j] = 2**(i+j)

        maior = matriz[ordem-1][ordem-1]
        tamanho = len(str(maior))

        for i in range(0, ordem):
            primeiro_numero = str(matriz[i][0])
            tamanho_pri_num = len(primeiro_numero)
            linha = ' ' * (tamanho - tamanho_pri_num) + primeiro_numero
            for j in range(1, ordem):
                numero = str(matriz[i][j])
                tamanho_numero = len(numero)
                linha = linha + ' ' * (tamanho - tamanho_numero + 1) + numero
            print(linha)
        print()
