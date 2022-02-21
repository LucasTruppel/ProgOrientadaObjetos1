entrada = input().split()
quantidade_postos, distancia_atleta = [int(i) for i in entrada]
entrada = input().split()
postos = [int(j) for j in entrada]
situacao = 'S'
if 42195 - postos[quantidade_postos-1] > distancia_atleta:
    situacao = 'N'
else:
    for k in range(1, quantidade_postos):
        if postos[k] - postos[k - 1] > distancia_atleta:
            situacao = 'N'
            break
print(situacao)
    