# -*- coding: utf-8 -*-

comprimento, largura, quantidade_soldados = [int(k) for k in input().split()]  # Entrada informações.
habilidade1 = 0  # Habilidade do exército 1.
habilidade2 = 0  # Habilidade do exército 2.

for i in range(0, quantidade_soldados):  # Loop para verificar cada soldado.
    x, y, habilidade = [int(k) for k in input().split()]  # Entrada posição e habilidade do soldado.
    # Cálculo do y do rio para o mesmo valor x do soldado. A equação do rio é y_rio = (largura/comprimento) * x_rio.
    y_rio = (largura / comprimento) * x
    if y > y_rio:  # Caso o soldado esteja acima da altura do rio, ele é do exército 1.
        habilidade1 += habilidade  # Soma a habilidade do soldado à habilidade do seu exército.
    else:  # Caso o soldado esteja abaixo da altura do rio, ele é do exército 2.
        habilidade2 += habilidade  # Soma a habilidade do soldado à habilidade do seu exército.

# Imprime a habilidade dos exército.
print(habilidade1, habilidade2)
