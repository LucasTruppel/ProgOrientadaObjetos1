# -*- coding: utf-8 -*-

# Entrada de dados.
entrada = input().split()
comprimento_fita, quantidade_gotas = [int(i) for i in entrada]
entrada = input().split()
posicao_gotas = [int(i) for i in entrada]  # Posição das gotas é armazenada em uma lista.
tempos = []  # Lista onde serão adicionados os tempos em dias.

# Tempo para que o reagente chegue ao início da fita. Como a gota se desloca 1 posição por dia, basta subtrair 1 da
# posição da primeira gota para obter o tempo.
tempo_inicio = posicao_gotas[0] - 1
tempos.append(tempo_inicio)  # Tempo para chegar no início é adicionado a lista de tempos.

# Tempo para que as duplas de gotas consecutivas se encontrem. Já que as duas se deslocam, o tempo de encontro deve
# considerar os dois deslocamentos.
if quantidade_gotas > 1:  # Para que essa situação ocorra, precisa-se de mais de uma gota.
    diferenca_posicoes = []
    for i in range(1, quantidade_gotas):  # Loop utilizado para avaliar todas as duplas de gotas consecutivas.
        diferenca_posicoes.append(posicao_gotas[i] - posicao_gotas[i - 1])
    # A maior diferença entre posições de gotas consecutivas determinará o tempo para preencher o meio da fita.
    maior_diferenca = max(diferenca_posicoes)
    # O tempo para preencher o meio da fita é igual a divisão inteira da maior diferença de posições por 2. A divisão
    # inteira é utilizada pois arredonda para baixo, obtendo o tempo certo no caso da maior_diferenca ser ímpar.
    tempo_meio = maior_diferenca // 2
    tempos.append(tempo_meio)  # Tempo para preencher o meio é adicionado à lista de tempos.

# Tempo para que o reagente chegue ao final da fita. Como a gota se desloca 1 posição por dia, subtraindo o comprimento
# da fita pela posição da última gota obtem-se o tempo.
tempo_final = comprimento_fita - posicao_gotas[-1]
tempos.append(tempo_final)  # Tempo para chegar no final é adicionado a lista de tempos.

# O tempo para preenchimento total da fita será o maior tempo entre os 3 tempos calculados anteriomente.
print(max(tempos))  # Impressão na tela do tempo para preenchimento total da fita.
