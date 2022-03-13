quantidade_candidatos = int(input())
dic_abates = {}
dic_mortes = {}
maior_poder = 0
possiveis_vencedores = []

for i in range(0, quantidade_candidatos):
    nome, poder, abates, mortes = input().split()
    poder = int(poder)
    abates = int(abates)
    mortes = int(mortes)

    if poder > maior_poder:
        maior_poder = poder
        possiveis_vencedores = [nome]
        dic_abates[nome] = abates
        dic_mortes[nome] = mortes
    elif poder == maior_poder:
        possiveis_vencedores.append(nome)
        dic_abates[nome] = abates
        dic_mortes[nome] = mortes

possiveis_vencedores_anterior = possiveis_vencedores.copy()
possiveis_vencedores = []
maior_abates = 0
for nome in possiveis_vencedores_anterior:
    if dic_abates[nome] > maior_abates:
        maior_abates = dic_abates[nome]
        possiveis_vencedores = [nome]
    elif dic_abates[nome] == maior_abates:
        possiveis_vencedores.append(nome)

possiveis_vencedores_anterior = possiveis_vencedores.copy()
possiveis_vencedores = []
menor_mortes = 101
for nome in possiveis_vencedores_anterior:
    if dic_mortes[nome] < menor_mortes:
        menor_mortes = dic_mortes[nome]
        possiveis_vencedores = [nome]
    elif dic_mortes[nome] == menor_mortes:
        possiveis_vencedores.append(nome)

melhor_nome = possiveis_vencedores[0]
for nome in possiveis_vencedores:
    if nome < melhor_nome:
        melhor_nome = nome
print(melhor_nome)
