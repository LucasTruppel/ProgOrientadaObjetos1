# -*- coding: utf-8 -*-

quantidade_salas = int(input())  # Entrada da quantidade de salas.
salas = [int(k) for k in input().split()]  # Entrada dos números de vidas das salas. Convertidos pra int na lista.

soma = 0
maior_soma = 0
# Loop para avaliar as somas de vidas.
for i in range(0, quantidade_salas):
    soma += salas[i]  # Incrementa o contador da soma com o valor da sala.
    # Caso a soma seja negativa, não faz sentido contar aquelas salas, pois a maior soma com certeza não conterá essas
    # salas. Então a soma é zerada, para contar a partir da próxima sala na próxima iteração.
    if soma < 0:
        soma = 0
    # Caso a soma seja maior que a maior soma armazenada, o novo valor de soma é armazenado na variável de maior soma.
    elif soma > maior_soma:
        maior_soma = soma

print(maior_soma)  # Após avaliar todas as situações necessárias, a maior soma é impressa na tela.
