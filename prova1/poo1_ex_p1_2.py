# -*- coding: utf-8 -*-

import math

"""
Como precisamos descobrir o primo mais próximo de dois números, foi criada uma função que, dado um número, ela retorna
o primo mais próximo e menor ou igual a esse número. A função tem um loop que começa no número dado e vai
diminuindo 1. Dentro desse loop há outro loop que testa se o número é divisível por algum número do intervalo. Caso não
seja, o número é primo. Uma variável armazena a informação se o número é primo ou composto. Quando o número é primo, o 
loop é quebrado e o primo mais próximo é retornado pela função.
"""


def primo_proximo(n):
    for numero in range(n, 1, -1):
        tipo = 'primo'
        raiz = int(math.sqrt(numero))
        # Um número é primo quando ele não é divisível por nenhum número entre 2 e sua raiz quadrada.
        for valor in range(2, raiz + 1):
            if numero % valor == 0:  # Caso seja encontrado um divisor, entra no if.
                tipo = 'composto'  # Tipo do número é composto
                break  # Esse loop é quebrado. O outro loop vai pro próximo número.
        if tipo == 'primo':  # Testa se o número recebeu 'composto' no loop anterior. Caso não, é primo.
            p = numero
            break  # Achado o primo mais próximo, o loop é quebrado.
    return p


# Entrada dos números do usúario
entrada = input().split()
N, M = [int(i) for i in entrada]  # N é o número de Juilherme e M é o número de Jogério.

# A função é chamada para o números dados de entrada, então a resposta é calculada e impressa na tela.
P1 = primo_proximo(N)
P2 = primo_proximo(M)
resposta = P1 * P2
print(resposta)
