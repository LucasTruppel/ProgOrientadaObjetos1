# -*- coding: utf-8 -*-

# Entrada, conversão para int e armazenamento dos dados.
entrada = input().split()
quantidade_numeros, minimo, maximo = [int(i) for i in entrada]
entrada = input().split()
numeros = [int(i) for i in entrada]  # Os numeros ficam em uma lista.

# Um loop dentro do outro para avaliar todos os pares possíveis.
quantidade_pares = 0
for i in range(0, quantidade_numeros):
    numero = numeros[i]
    # O segundo loop começa do i + 1 para que não ocorra a repetição desnecessária de pares.
    for j in range(i + 1, quantidade_numeros):
        soma = numero + numeros[j]
        if minimo <= soma <= maximo:  # Verifica se a soma está no intervalo desejado.
            quantidade_pares += 1  # Caso esteja no intervalo, o contador é incrementado.

# A quantidade de pares é impressa na tela.
print(quantidade_pares)
