entrada = input().split()
quantidade_jogadores, quantidade_partidas = [int(i) for i in entrada]
jogadores = 0
for i in range(0, quantidade_jogadores):
    partidas = input().split()
    if '0' not in partidas:
        jogadores += 1
print(jogadores)
