fileiras = int(input())
i_inicial, j_inicial = [int(k) - 1 for k in input().split()]

camisas = [None] * fileiras
bandeira = [None] * fileiras
for i in range(0, fileiras):
    camisas[i] = [int(k) for k in input().split()]
    bandeira[i] = ['A'] * fileiras

bandeira[i_inicial][j_inicial] = 'L'
cont_bandeiras = 1
alunos_pendentes = [(i_inicial, j_inicial)]

while alunos_pendentes != []:
    (i, j) = alunos_pendentes.pop(0)
    i_cima, i_baixo, i_direita, i_esquerda = i - 1, i + 1, i, i
    j_cima, j_baixo, j_direita, j_esquerda = j, j,   j + 1, j - 1

    if i_cima >= 0 and bandeira[i_cima][j_cima] == 'A' and camisas[i_cima][j_cima] >= camisas[i][j]:
        alunos_pendentes.append((i_cima, j_cima))
        bandeira[i_cima][j_cima] = 'L'
        cont_bandeiras += 1

    if i_baixo < fileiras and bandeira[i_baixo][j_baixo] == 'A' and camisas[i_baixo][j_baixo] >= camisas[i][j]:
        alunos_pendentes.append((i_baixo, j_baixo))
        bandeira[i_baixo][j_baixo] = 'L'
        cont_bandeiras += 1

    if j_direita < fileiras and bandeira[i_direita][j_direita] == 'A' and camisas[i_direita][j_direita] >= camisas[i][j]:
        alunos_pendentes.append((i_direita, j_direita))
        bandeira[i_direita][j_direita] = 'L'
        cont_bandeiras += 1

    if j_esquerda >= 0 and bandeira[i_esquerda][j_esquerda] == 'A' and camisas[i_esquerda][j_esquerda] >= camisas[i][j]:
        alunos_pendentes.append((i_esquerda, j_esquerda))
        bandeira[i_esquerda][j_esquerda] = 'L'
        cont_bandeiras += 1

print(cont_bandeiras)
