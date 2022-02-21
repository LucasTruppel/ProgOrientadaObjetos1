# -*- coding: utf-8 -*-

# Entrada de dados.
entrada = input().split()
quantidade_alunos, minimo_alunos = [int(i) for i in entrada]
horarios = input().split()  # Horários de chegada dos alunos são armazenados em uma lista.

# Loop que verifica o horário que cada aluno chegou e acrescenta o contador caso tenha chegado dentro do horário.
quantidade_pontuais = 0
for i in range(0, quantidade_alunos):
    if int(horarios[i]) <= 0:
        quantidade_pontuais += 1

# Verifica se a quantidade de alunos que chegou no horário é suficiente para o treinamento e imprime na tela a resposta.
if quantidade_pontuais >= minimo_alunos:
    print('YES')
else:
    print('NO')
