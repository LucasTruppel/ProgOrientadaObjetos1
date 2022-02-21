while True:
    quantidade_questoes = int(input())
    if quantidade_questoes == 0:
        break

    alternativas = ['A', 'B', 'C', 'D', 'E']
    for questao in range(0, quantidade_questoes):
        resposta = input().split()
        alternativas_marcadas = 0

        for alternativa in range(0, 5):
            resposta[alternativa] = int(resposta[alternativa])
            if resposta[alternativa] <= 127:
                alternativa_certa = alternativas[alternativa]
                alternativas_marcadas = alternativas_marcadas + 1

        if alternativas_marcadas == 1:
            print(alternativa_certa)
        else:
            print('*')
