# -*- coding: utf-8 -*-

quantidade_criancas = int(input())  # Entrada da quantiade de crianças
quantidade_carrinhos = 0
quantidade_bonecas = 0

# Loop recebe as informações de cada criança e acrescenta o contador do brinquedo referente ao gênero da criança.
for i in range(0, quantidade_criancas):
    nome, genero = input().split()  # Entrada do nome e gênero de cada criança
    if genero == 'M':
        quantidade_carrinhos += 1
    else:
        quantidade_bonecas += 1

# Imprime na tela a quantiade de cada brinquedo
print(f'{quantidade_carrinhos} carrinhos')
print(f'{quantidade_bonecas} bonecas')
