# -*- coding: utf-8 -*-

# Entrada dos dados. Transforma as entradas em listas.
numeros_flavinho = input().split()
numeros_sorteados = input().split()
acertos = 0
for i in range(0, 6):  # Loop para contar o número de acertos
    if numeros_sorteados[i] in numeros_flavinho:  # Verifica se cada número sorteado está nos numeros do Flavinho
        acertos += 1

# Com base no número de acertos, mensagens diferentes são imprimidas na tela
if acertos < 3:
    print('azar')
elif acertos == 3:
    print('terno')
elif acertos == 4:
    print('quadra')
elif acertos == 5:
    print('quina')
else:
    print('sena')
