# -*- coding: utf-8 -*-

"""
A base do código é um loop que avalia se o tipo do valor é verba oferecida ou gasto. Baseado no tipo, o valor é
adicionado no respectivo somatório. De acordo com a avaliação do maior somatório, uma mensagem é impressa na tela.
"""
numero_valores = int(input())  # Entrada da quantidade de valores.
verba_oferecida = 0
gastos = 0
for valores in range(1, numero_valores + 1):
    tipo, valor = input().split()
    valor = int(valor)
    if tipo == 'V':
        verba_oferecida = verba_oferecida + valor  # Somatório de verba oferecida.
    else:
        gastos = gastos + valor  # Somatório de gastos.
if verba_oferecida >= gastos:  # Verba suficiente.
    print('A greve vai parar.')
else:  # Verba insuficiente.
    print('NAO VAI TER CORTE, VAI TER LUTA!')
