# -*- coding: utf-8 -*-

# Entrada de dados. Quantidade de bolinhas e galhos da árvore.
bolinhas = int(input())
galhos = int(input())

# Calculo da quantidade de galhos e impressão da saída.
galhos_com_bolinha = galhos // 2  # Divisão inteira garante que seja arredondado para baixo.
if galhos_com_bolinha <= bolinhas:  # Bolinhas suficientes.
    print('Amelia tem todas bolinhas!')
else:  # Faltam bolinhas.
    bolinhas_faltantes = galhos_com_bolinha - bolinhas
    print('Faltam %d bolinha(s)' % bolinhas_faltantes)
