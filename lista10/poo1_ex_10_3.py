# Dados do problema:
# Título: Composição de Jingles
# Origem: Por Ines Kereki Uruguai
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1430

notas = {'W': 1, 'H': 0.5, 'Q': 0.25, 'E': 0.125, 'S': 0.0625, 'T': 0.03125, 'X': 0.015625}
while True:
    compassos = input().split('/')
    if compassos == ['*']:
        break
    compassos = compassos[1:-1]
    compassos_validos = 0
    for compasso in compassos:
        soma = 0
        for letra in compasso:
            soma += notas[letra]
        if soma == 1:
            compassos_validos += 1
    print(compassos_validos)
