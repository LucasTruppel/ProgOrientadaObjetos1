# -*- coding: utf-8 -*-

quantidade_figurinhas = int(input())  # Quantidade total de figurinhas.
figurinhas = [0] * 301  # Cada posição dessa lista representa um número de figurinha.
diferentes = 0
repetidas = 0
for i in range(0, quantidade_figurinhas):  # Loop para avaliar cada figurinha.
    figurinha = int(input())  # Entrada do número da figurinhas.
    if figurinhas[figurinha] == 0:  # Se não apareceu nenhuma dessa figurinha ainda, aumenta o contador de diferentes.
        diferentes += 1
        figurinhas[figurinha] = 1  # 1 representa que a figurinha já apareceu, 0 representa que não aparececeu ainda.
    else:
        repetidas += 1  # Caso o valor na posição não seja 0, aumenta o contador de repetidas.

# Imprime na tela os contadores.
print(diferentes)
print(repetidas)
