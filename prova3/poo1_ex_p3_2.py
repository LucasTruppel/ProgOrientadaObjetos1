# -*- coding: utf-8 -*-

quantidade_instanscias = int(input())  # Entrada da quantidade de instâncias.
for instancia in range(0, quantidade_instanscias):  # Loop para cada instância.
    dimensao, entradas = [int(k) for k in input().split()]  # Dimensão da matriz e quantidade de entradas != 0.

    # Como a maior parte dos valores serão 0, não é necessário criar uma matriz e armazená-la, então usamos um
    # dicionário.
    # Nesse dicionário as chaves serão a posicão (i, j) na matriz e o valor é o valor nessa posição na matriz,
    # considerando apenas os valores diferentes de 0.
    valores = {}
    for entrada in range(0, entradas):  # Loop para alcançar cada entrada.
        numero_matriz, i, j, valor = [int(k) for k in input().split()]  # Informações da entrada.
        if (i, j) not in valores:  # Se ainda não há um valor naquela posição, adiciona a posição no dicionário.
            valores[(i, j)] = valor
        else:  # Caso já tenha a posição no dicionário, o valor é somado ao existente.
            valores[(i, j)] += valor

    posicoes = sorted(valores)  # Lista com as chaves do dicionário em ordem.
    # Loop para alcançar cada posição.
    for k in range(0, len(posicoes)):
        i, j = posicoes[k]  # Pega a posição da lista que representa a posição na matriz soma.
        valor = valores[(i, j)]  # Pega o valor no dicionário referente a essa posição.
        print(i, j, valor)  # Imprime cada posição e seu respectivo valor.
    if instancia != quantidade_instanscias - 1:  # Imprime linha em branco entre as instâncias.
        print()
