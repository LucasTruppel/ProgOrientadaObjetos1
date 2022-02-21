teste = 0
while True:
    teste = teste + 1
    quantidade_rodadas = int(input())
    if quantidade_rodadas == 0:
        break
    total_figurinhas_aldo = 0
    total_figurinhas_beto = 0
    for rodada in range(1, quantidade_rodadas + 1):
        entrada = input().split()
        figurinhas_aldo, figurinhas_beto = [int(i) for i in entrada]
        total_figurinhas_aldo = total_figurinhas_aldo + figurinhas_aldo
        total_figurinhas_beto = total_figurinhas_beto + figurinhas_beto
    print('Teste %d' % teste)
    if total_figurinhas_aldo > total_figurinhas_beto:
        print('Aldo')
        print()
    else:
        print('Beto')
        print()
