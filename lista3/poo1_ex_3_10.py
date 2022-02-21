N = int(input())
for numero in range(1, N + 1):
    entrada = input().split()
    X, Y = [int(i) for i in entrada]
    if X == Y:
        print('0')
        continue
    if X > Y:
        maior = X
        menor = Y
    else:
        maior = Y
        menor = X
    soma = 0
    for impar in range(menor + 1, maior):
        if impar % 2 != 0:
            soma = soma + impar
    print(soma)
