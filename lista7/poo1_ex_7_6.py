while True:
    ordem = int(input())
    if ordem == 0:
        break
    elif ordem == 1:
        print('  1')
        print()
    else:
        matriz = [None] * ordem
        for i in range(0, ordem):
            matriz[i] = [0] * ordem

        for k in range(1, ordem // 2 + 1):
            for i in range(-1 + k, ordem + 1 - k):
                matriz[i][k - 1] = k
                matriz[i][ordem - k] = k
            for j in range(k, ordem - k):
                matriz[k - 1][j] = k
                matriz[ordem - k][j] = k
        if ordem % 2 != 0:
            matriz[ordem // 2][ordem // 2] = k + 1

        for i in range(0, ordem):
            for j in range(0, ordem-1):
                print('%3d ' % matriz[i][j], end='')
            print('%3d' % matriz[i][j+1], end='')
            print('')
        print()
