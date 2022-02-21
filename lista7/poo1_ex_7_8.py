quantidade_numeros = int(input())
numeros = input().split()
multiplos2 = 0
multiplos3 = 0
multiplos4 = 0
multiplos5 = 0

for i in range(0, quantidade_numeros):
    numero = int(numeros[i])
    if numero % 2 == 0:
        multiplos2 += 1
        if numero % 4 == 0:
            multiplos4 += 1
    if numero % 3 == 0:
        multiplos3 += 1
    if numero % 5 == 0:
        multiplos5 += 1

print(f'{multiplos2} Multiplo(s) de 2')
print(f'{multiplos3} Multiplo(s) de 3')
print(f'{multiplos4} Multiplo(s) de 4')
print(f'{multiplos5} Multiplo(s) de 5')
