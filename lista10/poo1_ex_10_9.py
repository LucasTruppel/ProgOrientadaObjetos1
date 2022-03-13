# Dados do problema:
# Título: Número Solitário
# Origem: Por Gabriel Duarte, UNIFESO Brazil
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/2091

while True:
    quantidade_numeros = int(input())
    if quantidade_numeros == 0:
        break

    dicionario = {}
    numeros = [int(k) for k in input().split()]
    for numero in numeros:
        if numero not in dicionario:
            dicionario[numero] = 1
        else:
            dicionario[int(numero)] += 1

    for numero in dicionario:
        if dicionario[numero] % 2 != 0:
            print(numero)
            break
