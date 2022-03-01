# -*- coding: utf-8 -*-

quantidade_registros = int(input())  # Quantidade de registros na folha.
alunos = [0] * 1000001  # Uma lista que cada posição representa um aluno. Como o número máximo de registro é 100000 e o
# 0 é número válido, multiplica-se por 1000001 para criar a lista.

for i in range(0, quantidade_registros):  # Loop para avaliar cada registro.
    numero = int(input())  # Entrada do registro.
    alunos[numero] = 1  # Quando um número de aluno é identificado, sua posição na lista recebe 1.
    # No caso de repetição de um aluno, a posição recebe 1 novamente, não interferindo no resultado.

total_alunos = alunos.count(1)  # Conta a quantidade de 1 na lista para obter o total de alunos.
print(total_alunos)  # Imprime na tela o total de alunos.
