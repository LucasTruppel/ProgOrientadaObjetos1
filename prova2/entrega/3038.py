# -*- coding: utf-8 -*-

# Primeira lista armazena os simbolos e na segunda lista suas respectividas vogais na mesma posição.
simbolos = ['@', '&', '!', '*', '#']
vogais = ['a', 'e', 'i', 'o', 'u']
while True:  # Loop para receber cada caso de texto.
    try:
        texto = input()  # Entrada do texto.
        novo_texto = ''
        for j in range(0, len(texto)):  # Loop para cada caracter do texto.
            caracter = texto[j]
            if caracter in simbolos:  # Se o caracter está na lista de simbolos ele é trocado pela sua respectiva vogal.
                posicao = simbolos.index(caracter)  # Descobre a posicao do simbolo na lista.
                novo_texto = novo_texto + vogais[posicao]  # Adiciona o caracter ao novo texto.
            else:  # Se o caracter não é vogal, ele é diretamente adicionado no novo texto.
                novo_texto = novo_texto + caracter
        print(novo_texto)  # Impressão do novo texto.
    except EOFError:  # Quando acabam os casos de teste, o programa é encerrado.
        break
