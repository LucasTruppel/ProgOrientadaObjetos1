# Dados do problema:
# Título: Ilhas Isoladas
# Origem: Por João Marcos Salvanini Bellini de Moraes, IFSULDEMINAS Brazil
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/2492

while True:
    quantidade_conexoes = int(input())
    if quantidade_conexoes == 0:
        break

    tipo = 'Invertible.'
    funcao = {}
    for i in range(0, quantidade_conexoes):
        x, y = input().split(' -> ')
        if x in funcao:
            tipo = 'Not a function.'
        elif y in funcao.values() and tipo != 'Not a function.':
            tipo = 'Not invertible.'
        funcao[x] = y
    print(tipo)
