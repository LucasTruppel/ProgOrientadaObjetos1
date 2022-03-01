# -*- coding: utf-8 -*-

# Entrada da quantidade de cadeiras e fileiras e do espaço necessário entre os alunos de mesmo tipo de prova.
cadeiras, fileiras, espaco = [int(k) for k in input().split()]

# Contrução da matriz dos alunos.
matriz = [None] * cadeiras
for i in range(0, cadeiras):
    matriz[i] = [int(k) for k in input().split()]

valido = True  # Indica se é um caso válido.

# Verifica se a matriz atende o requisito de não haver alunos em fileiras consecutivas.
primeira_fileira = True  # Indica se é a primeira fileira sendo avaliada.
for j in range(0, fileiras):  # Avalia cada fileira.
    fileira_vazia = True  # Indica se a fileira é vazia.
    for i in range(0, cadeiras):
        if matriz[i][j] != 0:  # Se for encontrado um valor diferente de 0, então a fileira não é vazia.
            fileira_vazia = False
            break
    if primeira_fileira:  # Quando é a primeira fileira avaliada, não temos uma fileira anterior para comparar.
        primeira_fileira = False
    # Caso encontre duas fileiras consecutivas com alunos, a matriz é inválida.
    elif (not fileira_vazia) and (not fileira_anterior_vazia):
        valido = False
        break
    fileira_anterior_vazia = fileira_vazia  # Indica se a fileira anterior é vazia, será utilizado na próxima iteração.

# Caso atenda o primeiro requisito, testa se os alunos de mesmo tipo de prova estão de acordo com a distância mínima.
if valido:
    for j in range(0, fileiras):  # Avalia cada fileira.
        primeiro1 = True  # Indica se é o primeiro aluno da fileira com o tipo 1 de prova a ser avaliado.
        primeiro2 = True  # Indica se é o primeiro aluno da fileira com o tipo 2 de prova a ser avaliado.
        for i in range(0, cadeiras):
            if matriz[i][j] == 1:  # Prova do tipo 1.
                if primeiro1:  # Se é o primeiro, não tem com quem comparar.
                    i1_anterior = i
                    primeiro1 = False
                else:
                    if i - i1_anterior > espaco:  # Verifica se atende a distância mínima entre o atual e o anterior.
                        i1_anterior = i
                    else:  # Caso não atenda, a matriz não é válida.
                        valido = False
                        break
            elif matriz[i][j] == 2:  # Prova do tipo 2.
                if primeiro2:  # Se é o primeiro, não tem com quem comparar.
                    i2_anterior = i
                    primeiro2 = False
                else:
                    if i - i2_anterior > espaco:  # Verifica se atende a distância mínima entre o atual e o anterior.
                        i2_anterior = i
                    else:  # Caso não atenda, a matriz não é válida.
                        valido = False
                        break
        if not valido:  # Se a matriz não é válida, não precisa mais verificar.
            break

# Imprime na tela se é válida ou não.
if valido:
    print('S')
else:
    print('N')
