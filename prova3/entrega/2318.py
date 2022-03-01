# -*- coding: utf-8 -*-

'''
Alguns casos de quadrados mágicos precisam ser avaliados de modo diferente do que outros. Quando a diagonal principal ou
a diagonal secundária é composta apenas por 0, não é possível descobrir a soma certa de modo direto. Nesses casos, é
necessário criar um sistema de equações para descobrir as incógnitas. Em todas outras possibilidades é possível
descobrir a soma certa logo de início, pois com certeza haverá uma linha, coluna ou diagonal sem nenhum termo 0. Assim,
o código utiliza estratégias diferentes para cada situação. No segundo modo, primeiro descobre-se a soma certa, testando
as linhas, colunas e/ou diagonais. Após isso, calcula-se a quantidade de 0 em cada linha e coluna e a soma atual em cada
linha e coluna. Por fim, procura as linhas ou colunas com apenas um termo 0 e calcula qual deve ser o termo para que
esteja de acordo com a soma certa e a soma atual, então substitui o termo na matriz. Este processo se repete até que
não sobrem 0 na matriz.
'''

# Criação da matriz e entrada de seus elementos.
matriz = [None] * 3
for i in range(0, 3):
    matriz[i] = [int(k) for k in input().split()]

# Situação em que a diagonal principal é composta apenas por 0. Calcula-se os 3 termos faltantes por meio de um sistema
# de equações, em que os 0 viram incógnitas.
if matriz[0][0] == 0 and matriz[1][1] == 0 and matriz[2][2] == 0:

    # Soma das linhas.
    linha1 = matriz[0][0] + matriz[0][1] + matriz[0][2]
    linha2 = matriz[1][0] + matriz[1][1] + matriz[1][2]
    linha3 = matriz[2][0] + matriz[2][1] + matriz[2][2]

    # Calculo dos termos faltantes e substituição na matriz.
    matriz[0][0] = (linha3 - linha1 + linha2) // 2
    matriz[2][2] = linha2 - matriz[0][0]
    matriz[1][1] = linha1 - matriz[2][2]

# Situação em que a diagonal secundária é composta apenas por 0. Calcula-se os 3 termos faltantes por meio de um sistema
# de equações, em que os 0 viram incógnitas.
elif matriz[0][2] == 0 and matriz[1][1] == 0 and matriz[2][0] == 0:

    # Soma das linhas.
    linha1 = matriz[0][0] + matriz[0][1] + matriz[0][2]
    linha2 = matriz[1][0] + matriz[1][1] + matriz[1][2]
    linha3 = matriz[2][0] + matriz[2][1] + matriz[2][2]

    # Calculo dos termos faltantes e substituição na matriz.
    matriz[0][2] = (linha3 - linha1 + linha2) // 2
    matriz[2][0] = linha2 - matriz[0][2]
    matriz[1][1] = linha1 - matriz[2][0]

# Todos os casos restantes. Nesses é possível descobrir a soma certa logo de início por alguma linha/coluna/diagonal.
else:

    # Descobre a soma certa, primeiro avalia as linhas.
    soma = 0
    numeros_contados = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if matriz[i][j] == 0:
                break
            soma += matriz[i][j]
            numeros_contados += 1
        if numeros_contados == 3:  # Caso tenha somado 3 termos diferentes de 0, é porque achou a soma certa.
            break
        else:
            soma = 0
            numeros_contados = 0

    # Caso não encontre a soma certa nas linhas, tenta as colunas.
    if soma == 0:
        for j in range(0, 3):
            for i in range(0, 3):
                if matriz[i][j] == 0:
                    break
                soma += matriz[i][j]
                numeros_contados += 1
            if numeros_contados == 3:
                break
            else:
                soma = 0
                numeros_contados = 0

    # Caso não consiga a soma certa nem nas linhas, nem nas colunas, tenta pela diagonal principal ou secundária.
    if soma == 0:
        if matriz[0][0] != 0 and matriz[1][1] != 0 and matriz[2][2] != 0:  # Principal.
            soma = matriz[0][0] + matriz[1][1] + matriz[2][2]
        elif matriz[0][2] != 0 and matriz[1][1] != 0 and matriz[2][0] != 0:  # Secundária.
            soma = matriz[0][2] + matriz[1][1] + matriz[2][0]

    # Após descobrir a soma certa, utiliza esse loop para descobrir os valores faltantes. Se repete até que não tenham
    # valores 0 na matriz.
    quantidade_zeros = 3  # Contador de 0 começa com um valor qualquer para entrar no loop.
    while quantidade_zeros != 0:

        # Esse loop conta a quantidade de zeros em cada linha e colunas. Conta a soma atual em cada linha e coluna.
        # Também verifica a quantidade de 0 na matriz.
        linhas_zeros = [0, 0, 0]  # Quantos zeros em cada linha.
        soma_linhas = [0, 0, 0]  # Soma atual de cada linha.
        colunas_zeros = [0, 0, 0]  # Quantos zeros em cada coluna.
        soma_colunas = [0, 0, 0]  # Soma atual em cada coluna.
        quantidade_zeros = 0  # Quantidade de zeros na matriz.
        for i in range(0, 3):
            for j in range(0, 3):
                if matriz[i][j] == 0:
                    linhas_zeros[i] += 1
                    colunas_zeros[j] += 1
                    quantidade_zeros += 1
                else:
                    soma_linhas[i] += matriz[i][j]
                    soma_colunas[j] += matriz[i][j]

        # Troca os 0 pelo termo certo nas linhas e/ou colunas com apenas um 0.
        # O valor certo será a soma certa menos a soma atual.
        for i in range(0, 3):
            for j in range(0, 3):
                if matriz[i][j] == 0:
                    if linhas_zeros[i] == 1:
                        matriz[i][j] = soma - soma_linhas[i]
                    elif colunas_zeros[j] == 1:
                        matriz[i][j] = soma - soma_colunas[j]

# Imprime na tela a matriz quadrado mágico.
print(f'{matriz[0][0]} {matriz[0][1]} {matriz[0][2]}')
print(f'{matriz[1][0]} {matriz[1][1]} {matriz[1][2]}')
print(f'{matriz[2][0]} {matriz[2][1]} {matriz[2][2]}')
