# -*- coding: utf-8 -*-

"""
O código tem 2 loops. Um loop while é usado para ler cada conjunto de teste. Dentro desse loop while tem um loop for que
recebe os placares das partidas, calcula o saldo de gols e avalia o melhor período. Por fim, esse período é impresso na
tela. Após isso, o processo se repete para o próximo caso de teste ou o programa é encerrado, dependendo da entrada do
usuário.
"""

numero_teste = 0  # Contador do número do caso de teste.
while True:  # Loop para cada caso de teste
    numero_teste = numero_teste + 1
    numero_partidas = int(input())  # Entrada da quantidade de partidas.
    if numero_partidas == 0:  # Caso a entrada seja 0, o programa é encerrado.
        break

    # Valores iniciais para as variáveis utilizadas no loop a seguir.
    saldo_gols = 0
    partida_inicial = 1
    melhor_saldo_gols = -1
    melhor_partida_inicial = 1
    melhor_partida_final = 1
    # Loop para entrada dos placares dos jogos e avaliação do melhor período.
    for partida in range(1, numero_partidas + 1):
        entrada = input().split()
        gols_time, gols_advsersario = [int(gol) for gol in entrada]
        saldo_gols = saldo_gols + gols_time - gols_advsersario  # Saldo de gols total até o momento.

        # Estrutura de decisão que avalia o saldo de gols para descobrir o melhor período.
        if saldo_gols < 0:  # Nesse caso, o melhor período, caso exista, com certeza estará após o período já avaliado.
            saldo_gols = 0  # Como o saldo de gols é negativo, não se deve contar as partidas já avaliadas.
            partida_inicial = partida + 1
        elif (saldo_gols > melhor_saldo_gols) or (saldo_gols == melhor_saldo_gols and
                                                  (partida - partida_inicial >
                                                   melhor_partida_final - melhor_partida_inicial)):
            # Caso o saldo de gols for maior ou igual (mas com período maior), o período será armazenado como o melhor.
            melhor_saldo_gols = saldo_gols
            melhor_partida_inicial = partida_inicial
            melhor_partida_final = partida  # A partida final é a partida atual do loop.

    # Imprime o número do caso de teste e o período de maior saldo de gols.
    print('Teste %d' % numero_teste)
    if melhor_saldo_gols > 0:  # Saldo de gols positivo.
        print(melhor_partida_inicial, melhor_partida_final)
    else:  # Se o saldo de gols do melhor período é menor ou igual a zero, a resposta é nenhum.
        print('nenhum')
    print()
