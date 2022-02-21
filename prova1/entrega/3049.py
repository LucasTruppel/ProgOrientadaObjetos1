# -*- coding: utf-8 -*-

# Entrada de dados.
distancia_baixo = int(input())  # Distância de baixo a partir do lado esquerdo (em cm)
distanccia_cima = int(input())  # Distância de cima a partir do lado esquerdo (em cm)

# A porcenteagem de Felix é dada pela área do trapézio de bases distancia_baixo e distanccia_cima e altura 70cm, divida
# pela área do retângulo de base 160cm e altura 70cm.
porcentagem_felix = (distancia_baixo + distanccia_cima) / 320  # Fórmula simplificada matematicamente
porcentagem_marzia = 1 - porcentagem_felix  # Porcentagem de Marzia será o complemento da porcentagem de Felix

# Impressão na tela da maior porcentagem ou do indicativo de perda da nota.
if porcentagem_felix > porcentagem_marzia:
    print('1')
elif porcentagem_felix < porcentagem_marzia:
    print('2')
else:
    print('0')
