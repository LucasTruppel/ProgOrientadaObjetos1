import math
N = int(input())
for numero in range(1, N + 1):
    X = int(input())
    raiz = int(math.sqrt(X))
    tipo = 'Prime'
    for valor in range(2, raiz + 1):
        if X % valor == 0:
            tipo = 'Not Prime'
            break
    print(tipo)
