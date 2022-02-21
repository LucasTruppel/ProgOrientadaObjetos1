entrada = input().split()
quantidade_pedras, quantidade_sapos =[int(i) for i in entrada]
pedras = [0] * quantidade_pedras
for sapo in range(0, quantidade_sapos):
    entrada = input().split()
    posicao_inicial, distancia_pulo = [int(j) for j in entrada]
    for posicao in range(posicao_inicial - 1, quantidade_pedras, distancia_pulo):
        pedras[posicao] = 1
    for posicao in range(posicao_inicial - 1, -1, -distancia_pulo):
        pedras[posicao] = 1
for k in pedras:
    print(k)
