numero_celulas = int(input())
celulas = []
for i in range(0, numero_celulas):
    celula = int(input())
    celulas.append(celula)

if numero_celulas == 1:
    print(celulas[0])
else:
    print(celulas[0] + celulas[1])
    for j in range(1, numero_celulas - 1):
        print(celulas[j - 1] + celulas[j] + celulas[j + 1])
    print(celulas[numero_celulas - 2] + celulas[numero_celulas - 1])
