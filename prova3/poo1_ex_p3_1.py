# -*- coding: utf-8 -*-

# Entrada da operação a ser realizada.
operacao = input()

# Criação da matriz e entrada dos elementos.
matriz = [None] * 12  # Linhas.
for i in range(0, 12):
    matriz[i] = [None] * 12  # Colunas.
for i in range(0, 12):
    for j in range(0, 12):
        matriz[i][j] = float(input())  # Entrada dos elementos.

# Loop para alcançar os valores na parte inferior da matriz.
soma = 0
for i in range(7, 12):
    for j in range(12 - i, i):
        soma += matriz[i][j]  # Soma os valores desejados.
media = soma / 30  # Calcula a média.

# Baseado na operação inserida na entrada, imprime a soma ou a média dos  valores.
if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{media:.1f}')
