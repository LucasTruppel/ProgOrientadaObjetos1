while True:
    try:
        quantidade_botas = int(input())
        esquerdo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        direito = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        pares = 0
        for i in range(0, quantidade_botas):
            tamanho, pe = input().split()
            if pe == 'E':
                esquerdo[int(tamanho) - 30] = esquerdo[int(tamanho) - 30] + 1
            else:
                direito[int(tamanho) - 30] = direito[int(tamanho) - 30] + 1
        for k in range(0, 31):
            if esquerdo[k] == direito[k]:
                pares = pares + esquerdo[k]
            elif esquerdo[k] > direito[k]:
                pares = pares + direito[k]
            else:
                pares = pares + esquerdo[k]
        print(pares)
    except EOFError:
        break
