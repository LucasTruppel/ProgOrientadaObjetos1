entrada = input().split()
dinheiro_inicial, quantidade_transacoes = [int(i) for i in entrada]
dinheiro_jogadores = [dinheiro_inicial, dinheiro_inicial, dinheiro_inicial]

for i in range(0, quantidade_transacoes):
    operacao = input().split()
    for i in range(0, len(operacao)):
        if operacao[i] == 'D':
            operacao[i] = '0'
        elif operacao[i] == 'E':
            operacao[i] = '1'
        elif operacao[i] == 'F':
            operacao[i] = '2'

    if operacao[0] == 'C':
        dinheiro_jogadores[int(operacao[1])] = dinheiro_jogadores[int(operacao[1])] - int(operacao[2])
    elif operacao[0] == 'V':
        dinheiro_jogadores[int(operacao[1])] = dinheiro_jogadores[int(operacao[1])] + int(operacao[2])
    else:
        dinheiro_jogadores[int(operacao[1])] = dinheiro_jogadores[int(operacao[1])] + int(operacao[3])
        dinheiro_jogadores[int(operacao[2])] = dinheiro_jogadores[int(operacao[2])] - int(operacao[3])

print(*dinheiro_jogadores)
