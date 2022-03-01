# -*- coding: utf-8 -*-

quantidade_zero_anterior = - 1  # Quantidade de zeros na linha anterior. Começa negativo para primeira iteração.
escada = 'S'  # Tipo da matriz. 'S' se é escada e 'N' se não for.

# Entrada da quantidade de linhas e colunas, cria a matriz e entrada dos elementos.
linhas, colunas = [int(k) for k in input().split()]
matriz = [None] * linhas
for i in range(0, linhas):
    matriz[i] = input().split()

# Loop para avaliar cada linha em relação a linha anterior.
for i in range(0, linhas):
    quantidade_zero = 0  # Contador da quantidade de zeros da linha antes de um termo não igual a zero.
    for j in range(0, colunas):
        if matriz[i][j] != '0':  # Para quando chega em um termo não igual a zero.
            break
        quantidade_zero += 1
    # Compara a quantidade de zeros da linha atual com a linha anterior.
    # Caso seja uma linha apenas de 0, não quebra a regra.
    if quantidade_zero_anterior >= quantidade_zero and matriz[i] != ['0'] * colunas:
        escada = 'N'  # Se quebrar a regra, a variável recebe o indicador negativo e encerra a verificação.
        break
    quantidade_zero_anterior = quantidade_zero  # Armazena a quantidade de zeros para próxima iteração.

print(escada)  # Imprime na tela o resultado da classificação da matriz.
