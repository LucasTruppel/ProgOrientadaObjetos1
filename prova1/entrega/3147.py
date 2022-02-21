# -*- coding: utf-8 -*-

# Entrada de dados. H, E, A, O, W e X representam o número do exército de humanos, elfos, anões, orcs, wargs e águias,
# respectivamente.
entrada = input().split()
H, E, A, O, W, X = [int(i) for i in entrada]

# Soma dos exércitos e impressão do exército vencedor.
exercito_bem = H + E + A + X
exercito_mal = O + W
if exercito_bem >= exercito_mal:  # Caso os números empatem, o exércicto do bem vence.
    print('Middle-earth is safe.')
else:
    print('Sauron has returned.')
