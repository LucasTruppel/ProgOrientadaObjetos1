while True:
    entrada = input().split()
    if entrada == ['0', '0']:
        break
    quantidade_participantes, quantidade_problemas = [int(i) for i in entrada]

    matriz = [None] * quantidade_participantes
    problemas = [0] * quantidade_problemas
    participantes = [0] * quantidade_participantes
    for i in range(0, quantidade_participantes):
        entrada = input().split()
        matriz[i] = [int(k) for k in entrada]

    for i in range(0, quantidade_participantes):
        for j in range(0, quantidade_problemas):
            problemas[j] += matriz[i][j]
            participantes[i] += matriz[i][j]

    quantidade_caracteristicas = 0
    if quantidade_problemas not in participantes:
        quantidade_caracteristicas += 1
    if 0 not in problemas:
        quantidade_caracteristicas += 1
    if quantidade_participantes not in problemas:
        quantidade_caracteristicas += 1
    if 0 not in participantes:
        quantidade_caracteristicas += 1

    print(quantidade_caracteristicas)
