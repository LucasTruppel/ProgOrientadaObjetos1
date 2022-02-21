entrada = input().split()
elevador = 0
situacao = 'N'
leituras, capacidade = [int(i) for i in entrada]
for leitura in range(1, leituras + 1):
    entrada = input().split()
    egressos, ingressos = [int(j) for j in entrada]
    elevador = elevador - egressos + ingressos
    if elevador > capacidade:
        situacao = 'S'
print(situacao)
