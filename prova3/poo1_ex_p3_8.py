# -*- coding: utf-8 -*-

while True:
    try:
        linhas, colunas = [int(k) for k in input().split()]  # Entrada das dimensões da matriz.
        soma = 0
        for i in range(0, linhas):  # Loop para alçançar todas as linhas.
            linha = input().split()  # Entrada das linhas.
            for j in range(0, colunas):  # Loop para alcançar todos elementos de uma linha.
                # Como queremos a soma, basta acrescentar o contador. Não há necessidade de armazenar a matriz.
                soma += int(linha[j])

        # Calculo das sacas e litros, utilizando divisão inteira e resto.
        sacas = soma // 60
        litros = soma % 60

        # Impressão na tela do resultado.
        print(f'{sacas} saca(s) e {litros} litro(s)')

    except EOFError:
        break
