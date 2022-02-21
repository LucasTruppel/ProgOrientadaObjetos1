while True:
    quantidade_partidas = int(input())
    if quantidade_partidas == 0:
        break
    partidas = input().split()
    vitorias_maria = partidas.count('0')
    vitorias_joao = quantidade_partidas - vitorias_maria
    print(f'Mary won {vitorias_maria} times and John won {vitorias_joao} times')
