# -*- coding: utf-8 -*-

# Entrada de dados. Idade em anos.
idade1 = int(input())
idade2 = int(input())

# Estrutura de decisão baseada nas idades. Imprime se a dupla pode ou não entrar no cinema.
if idade1 < 6 or idade2 < 6:  # Caso alguém tenha menos de 6 anos, a dupla não pode entrar.
    print('NO')
else:
    if idade1 >= 18 or idade2 >= 18:  # Caso alguém tenha pelo menos de 18 anos, a dupla pode entrar.
        print('YES')
    elif idade1 >= 14 and idade2 >= 14:  # Caso ambos tenham pelo menos de 14 anos, a dupla pode entrar.
        print('YES')
    else:  # Caso a dupla não esteja inserida nas condições anteriores, não pode entrar.
        print('NO')
