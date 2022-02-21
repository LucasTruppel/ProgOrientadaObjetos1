n = 0
while True:
    n = n + 1
    numero_regioes = int(input())
    if numero_regioes == 0:
        break
    for regiao in range(1, numero_regioes + 1):
        entrada = input().split()
        X, Y, U, V = [int(i) for i in entrada]
        if regiao == 1:
            Xi, Yi, Ui, Vi = X, Y, U, V
        else:
            if Xi <= X:
                Xi = X
            if Yi >= Y:
                Yi = Y
            if Ui >= U:
                Ui = U
            if Vi <= V:
                Vi = V
    print('Teste %d' % n)
    if (Xi < Ui) and (Yi > Vi):
        print(Xi, Yi, Ui, Vi)
        print()
    else:
        print('nenhum')
        print()
