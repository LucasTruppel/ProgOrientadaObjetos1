# -*- coding: utf-8 -*-

teste = 0
while True:  # Loop para cada caso de teste.
    teste += 1  # Contador do teste.
    entrada = input().split()  # Entrada da quantidade de medições e o tamanho dos intervalos em minutos.
    if entrada == ['0', '0']:  # Caso ambos sejam 0, o programa é encerrado.
        break
    quantidade_medicoes, tempo_media = [int(i) for i in entrada]

    # Entrada das medições da temperatura. As temperaturas são convertidas para inteiro e armazenadas em uma lista.
    medicoes = []
    for i in range(0, quantidade_medicoes):
        medicao = int(input())
        medicoes.append(medicao)

    # Para deteminar a menor e a maior média é mais eficiente primeiro determinar a menor soma e a maior soma de
    # temperaturas e calcular as médias apenas no final.
    # A primeira soma é calculada separada para podermos comparar posteriormente.
    soma = 0
    for i in range(0, tempo_media):  # A quantidade de temperaturas somadas depende do intervalo de tempo da média.
        soma += medicoes[i]
    menor_soma = maior_soma = soma  # Como é a primeira soma, por enquanto ela é tanto a menor quanto a maior soma.

    # Esse loop avaliará as outras possibilidades de somas.
    for i in range(tempo_media, quantidade_medicoes):
        # Para avaliar a próxima soma, basta subtrair a primeira temperatura da soma anterior e adicionar a próxima
        # temperatura da lista, pois os termos do meio continuarão os mesmos.
        soma += medicoes[i] - medicoes[i - tempo_media]
        # Avalia se a nova soma bate o recorde de maior ou menor soma.
        if soma > maior_soma:
            maior_soma = soma
        if soma < menor_soma:
            menor_soma = soma

    # Tendo a menor e maior soma, calcula-se as médias. Transforma o resulta em inteiro, truncando a média.
    minimo = int(menor_soma/tempo_media)
    maximo = int(maior_soma/tempo_media)

    # Impressão na tela do número do caso de teste e da menor e maior média.
    print(f'Teste {teste}')
    print(minimo, maximo)
    print()
