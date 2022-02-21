# -*- coding: utf-8 -*-

import collections

# Entrada dos dados.
quantidade_questoes = int(input())
gabarito_desafo = input()  # Respostas de Desafortunado.
quantidade_colegas = int(input())

# Nessa lista cada elemento será uma string que representará as alternativas marcadas por todos alunos naquela questão.
# A lista é criada com um loop para ser usada posteriormente.
questoes = []
for i in range(0, quantidade_questoes):
    questoes.append('')

# Nesse loop o gabarito de cada aluno será lido e separado entre os elementos da lista (cada elemento é uma questão).
for i in range(0, quantidade_colegas):
    gabarito = input()  # Entrada do gabarito de cada aluno.
    for j in range(0, quantidade_questoes):  # Loop para cada questão.
        # A resposta só será armazenada se for diferente da resposta de Desafortunado, pois ele errou todas.
        if gabarito[j] != gabarito_desafo[j]:
            questoes[j] = questoes[j] + gabarito[j]  # Resposta é adicionada a string de sua questão

# Para obter a maior soma de nota possível, basta analisar quantas vezes foi marcada a alternativa mais marcada de cada
# questão.
soma = 0
for i in range(0, quantidade_questoes):
    if questoes[i] != '':  # Evita que a string vazia cause um erro, no caso de todos marcarem a alternativa errada.
        # Para obter quantas vezes a alternativa mais comum foi marcada, utiliza-se most_common do módulo collections.
        soma = soma + collections.Counter(questoes[i]).most_common(1)[0][1]
print(soma)  # No final a soma é impressa.
