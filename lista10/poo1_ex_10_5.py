# Dados do problema:
# Título: Jogo do Bicho
# Origem: Por Ricardo Anido Brasil
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1483

while True:
    entrada = input()
    if entrada == '0 0 0':
        break
    valor, numero_escolhido, numero_sorteado = entrada.split()
    valor = float(valor)

    while len(numero_escolhido) < 7:
        numero_escolhido = '0' + numero_escolhido
    while len(numero_sorteado) < 7:
        numero_sorteado = '0' + numero_sorteado

    dicionario = {}
    i = 0
    for j in range(0, 25):
        for k in range(1, 5):
            dicionario[k + i] = i
        i = i + 4
    dicionario[0] = 96

    if numero_escolhido[3:] == numero_sorteado[3:]:
        valor = valor * 3000
    elif numero_escolhido[4:] == numero_sorteado[4:]:
        valor = valor * 500
    elif numero_escolhido[5:] == numero_sorteado[5:]:
        valor = valor * 50
    elif dicionario[int(numero_escolhido[5:])] == dicionario[int(numero_sorteado[5:])]:
        valor = valor * 16
    else:
        valor = 0

    print(f'{valor:.2f}')
