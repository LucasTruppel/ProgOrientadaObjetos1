# -*- coding: utf-8 -*-

# Lista com os estados do norte.
estados_norte = ['roraima', 'acre', 'amapa', 'amazonas', 'para', 'rondonia', 'tocantins']
estado = input()  # Entrada do estado.
if estado in estados_norte:  # Verifica se o estado está na lista e imprime se é do Norte ou de Outra região.
    print('Regiao Norte')
else:
    print('Outra regiao')
