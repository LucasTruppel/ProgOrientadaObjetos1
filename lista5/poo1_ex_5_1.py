while True:
    numero_amostras = int(input())
    if numero_amostras == 0:
        break
    entrada = input().split()
    amostras = [int(amostra) for amostra in entrada]
    numero_picos = 0

    # Primeira amostra
    if amostras[0] > amostras[1] and amostras[0] > amostras[numero_amostras-1]:
        numero_picos = numero_picos + 1
    elif amostras[0] < amostras[1] and amostras[0] < amostras[numero_amostras-1]:
        numero_picos = numero_picos + 1

    # Ultima amostra
    if amostras[numero_amostras-1] > amostras[numero_amostras-2] and amostras[numero_amostras-1] > amostras[0]:
        numero_picos = numero_picos + 1
    elif amostras[numero_amostras-1] < amostras[numero_amostras-2] and amostras[numero_amostras-1] < amostras[0]:
        numero_picos = numero_picos + 1

    # Outras amostras
    for i in range(1, numero_amostras - 1):
        if amostras[i] > amostras[i-1] and amostras[i] > amostras[i + 1]:
            numero_picos = numero_picos + 1
        elif amostras[i] < amostras[i-1] and amostras[i] < amostras[i + 1]:
            numero_picos = numero_picos + 1

    print(numero_picos)
