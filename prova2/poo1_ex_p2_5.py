# -*- coding: utf-8 -*-

while True:  # Loop para receber os casos de teste.
    quantidade_comandos = int(input())  # Entrada da quantidade de comandos a serem executados.
    if quantidade_comandos == 0:  # Se for 0, o programa é encerrado.
        break
    entrada = input().split()  # Entrada das posições iniciais, armazenamento em uma lista e conversão para inteiro.
    posicoes = [int(i) for i in entrada]

    soma = 0  # Armazena a quantidade de vezes que o botão foi pressionado.
    # Loop para avaliar cada comando executado.
    for i in range(0, len(posicoes)):
        posicao_comando = posicoes[0]  # Comando atual.
        soma += posicao_comando  # O botão será pressionado o número de vezes da posição do comando atual.
        posicoes.remove(posicao_comando)  # Após executado, o comando é removido da lista.
        for j in range(0, len(posicoes)):  # Loop para alterar a posição dos comandos.
            # Se existir outro do comando recém executado, ele é deslocado para primeira posição.
            if posicoes[j] == posicao_comando:
                posicoes[j] = 1
            else:  # Os demais comandos aumentam uma unidade na posição.
                posicoes[j] += 1
    print(soma)  # Soma total é impressa na tela.
