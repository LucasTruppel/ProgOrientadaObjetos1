# -*- coding: utf-8 -*-

"""
O código tem 4 loops. Um loop while é usado para ler cada conjunto de teste. Dentro desse loop while tem dois loops for.
O primerio loop for serve para ler as pontuações das partidas. O segundo loop serve para calcular o saldo de gols em
todos os períodos possíveis. Para que isso seja possível, dentro desse segundo loop for tem outro loop for. Enquanto
o algoritmo avalia todos os períodos possíveis, ele vai testando se o saldo de gols do período é o maior até o momento.
Assim, após o teste de todos os períodos possíveis, o período com o maior saldo de gols e o saldo de gols desse período
estarão armazenados em variáveis. Por fim, esse período é impresso na tela. Após isso, o ciclo se repete para o próximo
caso de teste ou o programa é encerrado, dependendo da entrada do usuário.
"""

numero_teste = 0  # Contador do número do caso de teste.
while True:  # Loop para cada caso de teste
    numero_teste = numero_teste + 1
    numero_partidas = int(input())  # Entrada da quantidade de partidas.
    if numero_partidas == 0:  # Caso a entrada seja 0, o programa é encerrado.
        break

    # Entrada dos placares das partidas.
    saldo_gols_por_partida = []  # Essa lista armazenará o saldo de gols de cada partida.
    for partida in range(0, numero_partidas):
        entrada = input().split()
        gols_time, gols_advsersario = [int(gol) for gol in entrada]
        saldo_gols_partida = gols_time - gols_advsersario  # Saldo de gols de uma partida.
        saldo_gols_por_partida.append(saldo_gols_partida)

    # Nesses dois loops serão testados todos os períodos possíveis. Uma estrutura de decisão testa cada período para
    # verificar se ele tem o maior saldo de gols até o momento.
    maior_saldo_gols_periodo = 0  # Armazenará o saldo de gols do período de maior saldo de gols.
    periodo = [0, 0]  # Armazenará o período de maior saldo de gols.
    for i in range(0, numero_partidas):  # Esse loop serva para determinar a partida inicial do próximo loop.
        saldo_gols_periodo = 0
        for j in range(i, numero_partidas):  # Testa todos os períodos possíveis para uma partida inicial fixa.
            saldo_gols_periodo = saldo_gols_periodo + saldo_gols_por_partida[j]
            # Testa se o saldo de gols do período é maior do que o já armazenado. Caso sim, o atualiza.
            if saldo_gols_periodo > maior_saldo_gols_periodo:
                maior_saldo_gols_periodo = saldo_gols_periodo
                periodo = [i + 1, j + 1]
            # No caso de saldos de gols iguais, testa se o período é maior. Caso sim, o atualiza.
            elif saldo_gols_periodo == maior_saldo_gols_periodo and (j + 1 > periodo[1] - periodo[0]):
                maior_saldo_gols_periodo = saldo_gols_periodo
                periodo = [i + 1, j + 1]

    # Imprime o número do caso de teste e o período de maior saldo de gols.
    print('Teste %d' % numero_teste)
    if maior_saldo_gols_periodo > 0:  # Saldo de gols positivo.
        print(periodo[0], periodo[1])
    else:  # Se o saldo de gols do melhor período é menor ou igual a zero, a resposta é nenhum.
        print('nenhum')
    print()
