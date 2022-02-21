teste = 1
while True:
    N = int(input())
    if N == -1:
        break
    else:
        i = 1
        j = 2
        for numero in range(1, N+2):
            k = j * j
            j = j + i
            i = i * 2
        print('Teste %d' % teste)
        print(k)
        print()
        teste = teste + 1
