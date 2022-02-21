# -*- coding: utf-8 -*-

# Entrada de dados. Quantidade dos ingredientes: xícaras de farinha, ovos e colheres de sopa.
entrada = input().split()
quantidade_farinha, quantidade_ovos, quantidade_leite = [int(i) for i in entrada]

# Divisão dos ingredientes em relação ao necessário para um bolo.
divisao_farinha = quantidade_farinha // 2
divisao_ovos = quantidade_ovos // 3
divisao_leite = quantidade_leite // 5

# Lista de quantos bolos da para fazer com cada ingrediente.
bolo = [divisao_farinha, divisao_ovos, divisao_leite]
quantidade_bolos = min(bolo)  # A quantidade de bolos é determinada pelo ingrediente com a menor divisão.
print(quantidade_bolos)  # Impressão quantidade de bolos.
