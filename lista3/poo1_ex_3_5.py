N = int(input())
for i in range(1, N + 1):
    X = int(input())
    if X == 0:
        print('NULL')
    else:
        if X % 2 == 0:
            tipo = 'EVEN'
        else:
            tipo = 'ODD'
        if X > 0:
            sinal = 'POSITIVE'
        else:
            sinal = 'NEGATIVE'
        print(tipo, sinal)
