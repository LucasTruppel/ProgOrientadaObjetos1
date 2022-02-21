# -*- coding: utf-8 -*-

# Entrada de dados
idade_monica = int(input())
idade_filho1 = int(input())
idade_filho2 = int(input())

idade_filho3 = idade_monica - idade_filho1 - idade_filho2  # Cálculo da idade do terceiro filho
idade_filhos = [idade_filho1, idade_filho2, idade_filho3]  # Lista com as idades dos filhos
print(max(idade_filhos))  # Imprime o maior valor da lista, que é a idade do filho mais velho
