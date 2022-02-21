# -*- coding: utf-8 -*-

# Entrada de dados. Preço em reais, quantidade de parcelas.
preco = int(input())
quantidade_parcelas = int(input())

base_parcela = preco // quantidade_parcelas  # Preço base para cada parcela, dividido igualmente.
resto = preco % quantidade_parcelas  # Quanto faltou após a divisão igual de parcelas.
parcelas = [base_parcela] * quantidade_parcelas  # Lista de parcelas.
for parcela in range(0, len(parcelas)):  # Loop que adiciona o valor que faltou às primeiras parcelas.
    if parcela < resto:
        parcelas[parcela] = parcelas[parcela] + 1
    print(parcelas[parcela])  # Impressão na tela de cada parcela.
