while True:
    entrada = input().split()
    if entrada == ['0', '0', '0']:
        break
    pontos, medicoes, comprimento = [int(i) for i in entrada]
    medicao_anterior = input().split()
    tamanho = [int(i) for i in medicao_anterior]
    contador = 0
    for j in range(1, medicoes):
        medicao = input().split()
        for k in range(0, pontos):
            if medicao[k] == '0':
                if medicao_anterior[k] == '1' and tamanho[k] >= comprimento:
                    contador = contador + 1
                tamanho[k] = 0
            else:
                tamanho[k] = tamanho[k] + 1
        medicao_anterior = medicao
    for i in range(0, pontos):
        if tamanho[i] >= comprimento:
            contador = contador + 1
    print(contador)
