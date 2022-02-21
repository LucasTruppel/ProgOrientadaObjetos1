# -*- coding: utf-8 -*-

import math

"""
O codigo é formado bassicamente por dois loops. O primeiro é para cada caso de teste e o segundo é para cada bola dentro
de um caso de teste. As coordenadas da bola branca são inseridas pelo usuário. Depois as coordenadas des outras bolas 
são inseridadas pelo usuário, dentro do loop de bolas. Para cada bola não branca, a distância entre ela e a bola branca
é calculada pela fórmula matématica da distância entre dois pontos. Quando a distância de uma bola é menor do que a da
anterior e o erro está dentro do aceito, seu número é armazenado na variável menor_bola. No final do caso de teste, 
é impresso o número da bola com a menor distância.
"""
numero_testes = int(input())
for teste in range(1, numero_testes + 1):
    quantidade_bolas = int(input())

    # Coordenada da bola branca
    bola_branca = input().split()
    Xb, Yb = [int(i) for i in bola_branca]

    # Coordenada das bolas coloridas
    for bola in range(1, quantidade_bolas + 1):
        bola_colorida = input().split()
        X, Y = [int(j) for j in bola_colorida]
        distancia = math.sqrt((Xb - X) ** 2 + (Yb - Y) ** 2)
        if bola == 1:  # Como essa é a primeira bola, ela automaticamente é a bola com a menor distância.
            menor_distancia = distancia
            menor_bola = bola
        else:  # A partir da segunda bola a distância e o erro são avaliados.
            erro = abs(menor_distancia - distancia)
            if (distancia < menor_distancia) and (erro >= 0.01):
                # No caso de empate, não entra no if. Assim, a variável menor_bola fica com a bola de menor número.
                menor_distancia = distancia
                menor_bola = bola
    print(menor_bola)
