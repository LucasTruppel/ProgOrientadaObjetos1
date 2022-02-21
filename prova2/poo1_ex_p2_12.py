# -*- coding: utf-8 -*-

from collections import Counter  # Counter será utilizado para contar a quantidade de cada carta de modo mais fácil.

quantidade_testes = int(input())  # Entrada da quantidade de testes.
for teste in range(1, quantidade_testes + 1):  # Loop para cada caso de teste.
    # Entrada das cartas e armazenamento em uma lista. Cartas transformadas para int e organizadas em ordem decrescente.
    entrada = input().split()
    cartas = [int(j) for j in entrada]
    cartas.sort()
    cartas.reverse()
    # O Counter cria uma lista de tuplas. O primeiro elemento de cada tupla é a carta e o segundo a sua quantidade.
    cartas_quantidade = Counter(cartas).most_common(5)

    # A estrutura de decisão determina qual a combinação das cartas para determinar a pontuação.
    if cartas[0] == cartas[1] + 1 and cartas[0] == cartas[2] + 2 and cartas[0] == cartas[3] + 3 and \
            cartas[0] == cartas[4] + 4:  # Cartas em sequência.
        pontuacao = cartas[4] + 200
    elif cartas_quantidade[0][1] == 4:  # Uma quadra.
        pontuacao = cartas_quantidade[0][0] + 180
    elif cartas_quantidade[0][1] == 3:  # Uma trinca. Para trincas têm duas situações possíveis.
        if cartas_quantidade[1][1] == 2:  # Trinca e um par.
            pontuacao = cartas_quantidade[0][0] + 160
        else:  # Apenas uma trinca, sem um par.
            pontuacao = cartas_quantidade[0][0] + 140
    elif cartas_quantidade[0][1] == 2:  # Caso a melhor combinação seja um par, têm duas possibilidades.
        if cartas_quantidade[1][1] == 2:  # Dois pares.
            pontuacao = 3 * cartas_quantidade[0][0] + 2 * cartas_quantidade[1][0] + 20
        else:  # Apenas um par.
            pontuacao = cartas_quantidade[0][0]
    else:  # Se não ocorreu nenhuma das combinações anteriores, não há pontuação.
        pontuacao = 0

    # Impressão do número do caso de teste e da pontuação.
    print(f'Teste {teste}')
    print(pontuacao)
    print()
