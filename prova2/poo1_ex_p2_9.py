# -*- coding: utf-8 -*-

while True:  # Loop para receber cada caso de teste.
    try:
        texto = input()  # Entrada do texto.
        novo_texto = ''
        for j in range(0, len(texto) - 1):  # Loop para cada caracter do texto.
            caracter = texto[j]
            proximo_caracter = texto[j+1]
            # É avaliado se o caracter é um espaço e se o próximo é ponto ou vírgula. Caso não, o novo texto o recebe.
            if not(caracter == ' ' and (proximo_caracter == ',' or proximo_caracter == '.')):
                novo_texto = novo_texto + caracter  # Desse modo, quando ocorre espaço indesejado, ele não é adicionado.
        novo_texto = novo_texto + texto[-1]  # O último caracter é adicionado fora do loop, pois não há um seguinte.
        print(novo_texto)  # Impressão do novo texto.
    except EOFError:  # Quando acabam os casos de teste, o programa é encerrado.
        break
