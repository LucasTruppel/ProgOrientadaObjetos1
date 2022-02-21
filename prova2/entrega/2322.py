# -*- coding: utf-8 -*-

# Entrada de dados.
quantidade_pecas = int(input())
entrada = input().split()
pecas = [int(i) for i in entrada]  # Armazena as pecas em uma lista e converte seu valor para inteiro.

# O Loop testa todos os números de peça possíveis até encontrar a faltante.
for i in range(1, quantidade_pecas + 1):
    if i not in pecas:  # Se o número não está na lista de peças, a peça faltante é impressa e o loop é encerrado.
        print(i)
        break
