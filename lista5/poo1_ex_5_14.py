teste = 0
while True:
    teste = teste + 1
    entrada = input().split()
    if entrada == ['0', '0']:
        break
    quantidade_aeroportos, quantidade_voos = [int(i) for i in entrada]

    aeroportos = []
    movimento = []
    for i in range(1, quantidade_aeroportos+1):
        aeroportos.append(i)
        movimento.append(0)

    for voo in range(1, quantidade_voos+1):
        entrada = input().split()
        aeroporto1, aeroporto2 = [int(i) for i in entrada]
        movimento[aeroporto1 - 1] = movimento[aeroporto1 - 1] + 1
        movimento[aeroporto2 - 1] = movimento[aeroporto2 - 1] + 1

    maior = max(movimento)
    maior_aeroporto = []
    j = 1
    while maior in movimento:
        posicao = movimento.index(maior)
        maior_aeroporto.append(posicao + j)
        movimento.remove(maior)
        j = j + 1
    maior_aeroporto.sort()

    print(f'Teste {teste}')
    maior_aeroporto.sort()
    print(' '.join(map(str, maior_aeroporto)) + ' ')
    print()
