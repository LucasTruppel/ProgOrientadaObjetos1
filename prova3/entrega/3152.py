# -*- coding: utf-8 -*-

maior_area = -1
for i in range(0, 2):  # Loop para testar os dois terrenos.
    # Entrada dos pontos e conversão para inteiro.
    x1, y1 = [int(k) for k in input().split()]
    x2, y2 = [int(k) for k in input().split()]
    x3, y3 = [int(k) for k in input().split()]
    x4, y4 = [int(k) for k in input().split()]

    # Área é calculada por meio do determinante dos pontos.
    det = abs(x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1 - (y1 * x2 + y2 * x3 + y3 * x4 + y4 * x1))  # Det em módulo.
    area = det / 2  # Formula da área.
    if area >= maior_area:  # Verifica se é a maior área. O >= garante que, em caso de empate, o segundo é escolhido.
        maior_area = area
        terreno = i  # Indicação de qual terreno é o maior.

# Baseado na indicação de terreno, o terreno de maior área é impresso na tela.
if terreno == 0:
    print('terreno A')
else:
    print('terreno B')
